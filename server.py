import socket

def start_server():
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)

    print("Server is up and running. Waiting for a connection...")

    client_socket, client_address = server_socket.accept()
    print(f"Connected to client at {client_address}")

    while True:
        
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print("Client has left the chat.")
            break
        print(f"Client: {message}")

        reply = input("You: ")
        client_socket.send(reply.encode('utf-8'))
        if reply.lower() == 'exit':
            print("You have left the chat.")
            break

   
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
