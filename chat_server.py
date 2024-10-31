import socketserver
import threading

# List to keep track of all connected clients
clients = []

# Handler for each client connection
class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Register new client
        clients.append(self.request)
        print(f"New connection from {self.client_address}")

        try:
            while True:
                # Receive message from client
                message = self.request.recv(1024).decode('utf-8')
                if not message:
                    break

                print(f"Received message from {self.client_address}: {message}")
                self.broadcast_message(message)
        except ConnectionResetError:
            print(f"Connection lost with {self.client_address}")
        finally:
            # Remove the client when disconnected
            clients.remove(self.request)
            self.request.close()

    def broadcast_message(self, message):
        # Send the message to all clients except the sender
        for client in clients:
            if client != self.request:
                try:
                    client.sendall(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error sending message: {e}")

# Threaded TCP server to handle multiple clients
class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 12345
    server = ChatServer((HOST, PORT), ClientHandler)

    # Start server in a separate thread
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print(f"Chat server started on {HOST}:{PORT}")

    try:
        server_thread.join()  # Keep the server running
    except KeyboardInterrupt:
        print("Shutting down server.")
        server.shutdown()
