import socketserver
import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class ClientHandler(socketserver.BaseRequestHandler):

    def handle(self):
        public_key = "public_key.key"
        private_key = "private_key.pem"
        encrypted_key = self.request.recv(4096).strip()
        print("Received encrypted key from client.\n")
        print("Implement decryption of data: " + encrypted_key.decode() + "\n")  # Convert bytes to string
        
        with open(private_key, "rb") as key_file:  # Added missing comma
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        # Decode the received Base64 data back to binary
        print("With base64: ")
        print(encrypted_key)
        print("\n")
        encrypted_key = base64.b64decode(encrypted_key)
        print("After decoding base64: ")
        print(encrypted_key)
        print("\n")
        symmetric_key = private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("Symmetric key: ")
        print(symmetric_key)
        print("\n")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            server_ip = "192.168.1.7"  # Replace with the server's IP address
            port = 8080
            sock.connect((server_ip, port))
            sock.sendall(symmetric_key)
        
if __name__ == "__main__":
    HOST, PORT = "192.168.1.7", 8888

    tcpServer =  socketserver.TCPServer((HOST, PORT), ClientHandler)
    print("Server started. Waiting for connections...")
    try:
        tcpServer.serve_forever()
    except: 
        print("There was an error")
