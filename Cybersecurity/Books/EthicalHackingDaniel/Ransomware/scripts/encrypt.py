from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa

symmetricKey  = Fernet.generate_key()

FernetInstance = Fernet(symmetricKey)

# Generate an RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Commonly used value for the public exponent
    key_size=2048,          # Adjust the key size as needed
    backend=default_backend()
)
public_key = private_key.public_key()

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

with open("encryptedSymmertricKey.key", "wb") as key_file:
        key_file.write(encryptedSymmetricKey)
        
filePath = "FIleToEncrypt.txt"

with open(filePath, "rb") as file:
    file_data = file.read()
    encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, "wb") as file:
    file.write(encrypted_data)
quit()
