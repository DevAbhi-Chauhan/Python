import socket
import threading

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_host = '127.0.0.1'
server_port = 12345
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen()

# List to store connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting message to a client: {str(e)}")
                client.close()
                clients.remove(client)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error receiving message from a client: {str(e)}")
            break

# Main server loop
while True:
    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address[0]}:{client_address[1]}")
    clients.append(client_socket)

    # Start a thread to handle the client's messages
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

# To use this chat application:

# 1. Start the server by running Chat Application(server).py.
# 2. Start multiple clients by running Chat Application(client).py in separate command-line windows.
# 3. Clients can send messages, and the server will broadcast them to all connected clients.