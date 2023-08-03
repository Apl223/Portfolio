from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
import socket
import base64

symmetricKey = Fernet.generate_key()
FernetInstance = Fernet(symmetricKey)
print("Symmetric key: ")
print(symmetricKey)
print("\n")
# Generate an RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Commonly used value for the public exponent
    key_size=2048,          # Adjust the key size as needed
    backend=default_backend()
)
public_key = private_key.public_key()
# Serialize the private key
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
with open("private_key.pem", "wb") as key_file:
    key_file.write(pem_private_key)
with open("public_key.key", "wb") as key_file:
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    key_file.write(public_key_bytes)

with open("public_key.key", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
encryptedSymmetricKey = public_key.encrypt(
    symmetricKey,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Without base64:")
print(encryptedSymmetricKey)
print("\n")
encryptedSymmetricKeyBase64 = base64.b64encode(encryptedSymmetricKey)
print("With base64:")
print(encryptedSymmetricKeyBase64)
print("\n")
with open("encryptedSymmetricKey.key", "wb") as key_file:
    key_file.write(encryptedSymmetricKeyBase64)

filePath = "FileToEncrypt.txt"

with open(filePath, "rb") as file:
    file_data = file.read()
    encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, "wb") as file:
    file.write(encrypted_data)

def sendEncryptedKey(eKeyFilePath, hostname, port):
    with socket.create_connection((hostname, port)) as sock:
        with open(eKeyFilePath, "rb") as file:
            encrypted_symmetric_key = file.read()
        sock.sendall(encrypted_symmetric_key)


def receive_encrypted_key(server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('192.168.1.7', server_port))
        sock.listen(1)
        conn, addr = sock.accept()
        with conn:
            print("Received encrypted key from server.")
            encrypted_symmetric_key = conn.recv(4096)  # Adjust buffer size as needed
    print("Recieved key: ")
    print(encrypted_symmetric_key)
    print("\n")
    return encrypted_symmetric_key
    
    
def decryptFile(filePath, private_key_path, server_port):

    encrypted_symmetric_key = receive_encrypted_key(server_port)
    print("Recieved encrypted key: ")
    print(encrypted_symmetric_key)
    print("\n")
    fernet_instance = Fernet(symmetricKey)
    
    with open(filePath, "rb") as file:
        file_data = file.read()
        decrypted_data = fernet_instance.decrypt(file_data)
        print("Decrypted_data: ")
        print(decrypted_data)
        print("\n")

    with open(filePath, "wb") as file:
        file.write(decrypted_data)
        
def sendPrivateKey(private_key_path, hostname, port):
    with socket.create_connection((hostname, port)) as sock:
        with open(private_key_path, "rb") as key_file:
            private_key_data = key_file.read()
        sock.sendall(private_key_data)
        
hostname = "192.168.1.7"
port = 8888
other_port = 8080
eKeyFilePath = "encryptedSymmetricKey.key"
public_key_path = "public_key.key"
private_key_path = "private_key.pem"

sent = sendEncryptedKey(eKeyFilePath, hostname, port)
#sendPrivateKey(private_key_path, hostname, port)
#recieved = receive_encrypted_key(other_port)
decrypted = decryptFile(filePath, private_key_path, other_port)

quit()
