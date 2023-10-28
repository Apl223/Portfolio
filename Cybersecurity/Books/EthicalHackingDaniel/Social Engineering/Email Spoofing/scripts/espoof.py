import sys
import socket

size = 1024

def sendMessage(smtpServer, port, fromAddress, toAddress, message):
    IP = smtpServer
    PORT = int(port)
    s = socket.create_connection((IP, PORT))  # Open socket on port

    print(s.recv(size).decode())  # Display response

    helo_command = f'HELO {fromAddress.split("@")[1]}\n'
    s.send(helo_command.encode())
    print(s.recv(size).decode())

    mail_from_command = f'MAIL FROM:<{fromAddress}>\n'
    s.send(mail_from_command.encode())
    print(s.recv(size).decode())

    rcpt_to_command = f'RCPT TO:<{toAddress}>\n'
    s.send(rcpt_to_command.encode())
    print(s.recv(size).decode())

    s.send(b"DATA\n")  # Send DATA
    print(s.recv(size).decode())

    s.send(f"{message}\n.\n".encode())  # Send email message and termination
    print(s.recv(size).decode())  # Display response

    s.send(b'QUIT\n')  # Send QUIT
    print(s.recv(size).decode())  # Display response

    s.close()

def main(args):
    if len(args) != 5:
        print("Usage: python script.py <smtpServer> <port> <fromAddress> <toAddress>")
        sys.exit(1)

    smtpServer = args[1]
    port = args[2]
    fromAddress = args[3]
    toAddress = args[4]
    message = """From: The Boss Lady <head@secret.gov>
    Subject: Hello SYS
    Click This link <a href="url">link text</a>
    Your Enemy, someone"""
    sendMessage(smtpServer, port, fromAddress, toAddress, message)

if __name__ == "__main__":
    main(sys.argv)

