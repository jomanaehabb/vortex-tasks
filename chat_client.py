import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("\n" + message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

if __name__ == "__main__":
    HOST, PORT = "localhost", 12345

    # Create a TCP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to chat server.")
    print("Type your messages below. Press Ctrl+C to exit.\n")

    # Start a thread to listen for incoming messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    try:
        while True:
            # Get message input from the user
            message = input()
            # Send message to the server
            client_socket.sendall(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("\nDisconnecting from chat server.")
    finally:
        client_socket.close()
