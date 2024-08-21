import socket

def start_client():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    client_socket.connect(('127.0.0.1', 12345))

    print("Connected to the server. You can start chatting!")

   
    while True:
        
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            print("You have left the chat.")
            break

        
        reply = client_socket.recv(1024).decode('utf-8')
        if reply.lower() == 'exit':
            print("Server has left the chat.")
            break
        print(f"Server: {reply}")

    
    client_socket.close()

if __name__ == "__main__":
    start_client()
