import socket
import threading

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_host = '127.0.0.1'
server_port = 12345
client_socket.connect((server_host, server_port))

# Function to receive and display messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except Exception as e:
            print(f"Error receiving message from the server: {str(e)}")
            client_socket.close()
            break

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main client loop
while True:
    message = input()
    client_socket.send(message.encode())

# To use this chat application:

# 1. Start the server by running Chat Application(server).py.
# 2. Start multiple clients by running Chat Application(client).py in separate command-line windows.
# 3. Clients can send messages, and the server will broadcast them to all connected clients.