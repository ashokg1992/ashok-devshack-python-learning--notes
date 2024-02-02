# # DAY-6 | 
# # ================================= Socket Library  ===================================

# The Python `socket` library provides a set of tools for network communication.
# It allows programs to create and manage network connections for sending and receiving data over a network. Here are some key concepts and functions provided by the `socket` library:

#  +++++++++++++++++++++++++++++++++++  1. **Socket**: +++++++++++++++++++++++++++++++++++

# A socket is an endpoint for communication between two machines over a network. It can be used to establish connections, send and receive data, and close connections.

# +++++++++++++++++++++++++++++++++++  2. **Socket Types**:  +++++++++++++++++++++++++++++++++++

# Python's `socket` library supports various socket types, but the two most common are:
# 1.Stream Sockets 
# 2 . Datagram Sockets

# - 1.Stream Sockets (`socket.SOCK_STREAM`)**:
#           -These provide a reliable, connection-oriented communication channel. They use protocols like TCP (Transmission Control Protocol) and ensure that data is delivered in the order it was sent.

# - **Datagram Sockets (`socket.SOCK_DGRAM`)**:
#       -These are connectionless and provide an unreliable, message-oriented communication channel. They use protocols like UDP (User Datagram Protocol) and do not guarantee delivery order or delivery at all.

# +++++++++++++++++++++++++++++++++++  3. **Address Families**: +++++++++++++++++++++++++++++++++++ 

# The `socket` library supports different address families. The most commonly used are:

# - **IPv4 (`socket.AF_INET`)**: This is used for IPv4 addresses and provides a 32-bit address space.
# - **IPv6 (`socket.AF_INET6`)**: This is used for IPv6 addresses which have a much larger address space.

# +++++++++++++++++++++++++++++++++++  4. **Creating a Socket**: +++++++++++++++++++++++++++++++++++ 

 
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # # Create a socket object
 
#  +++++++++++++++++++++++++++++++++++ 5. **Binding a Socket**:   +++++++++++++++++++++++++++++++++++

# Before a socket can be used for communication, it needs to be bound to a specific address and port on the local machine.
 
server_address = ('localhost', 12345)
server_socket.bind(server_address)
 

#  +++++++++++++++++++++++++++++++++++ 6. **Listening and Accepting Connections**:  +++++++++++++++++++++++++++++++++++

# For a server, it needs to start listening for incoming connections. When a client tries to connect, the server uses `accept()` to establish a connection.


server_socket.listen(5)
client_socket, client_address = server_socket.accept()
 
# +++++++++++++++++++++++++++++++++++  7. **Connecting to a Server**: +++++++++++++++++++++++++++++++++++

# For a client, it needs to connect to a server using the server's address and port.

client_socket.connect(server_address)
 

# +++++++++++++++++++++++++++++++++++  8. **Sending and Receiving Data**: +++++++++++++++++++++++++++++++++++

# Once a connection is established, data can be sent and received using `send()` and `recv()`.


client_socket.send(data.encode())
received_data = client_socket.recv(1024)
 

# +++++++++++++++++++++++++++++++++++  9. **Closing a Socket**: +++++++++++++++++++++++++++++++++++

# After communication is complete, the sockets should be closed.


client_socket.close()
 

# +++++++++++++++++++++++++++++++++++  Client-Server COnnection using Socket Library +++++++++++++++++++++++++++++++++++

# Client-server connection using Python's `socket` library. This example demonstrates a basic TCP communication between a server and a client.

#  Server Code:

 
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # # Create a TCP/IP socket
server_address = ('localhost', 12345)     # # Define the server address and port
server_socket.bind(server_address)        # # Bind the socket to the server address and port
server_socket.listen(1)       # # Listen for incoming connections (maximum of 1 connection in the queue)
print(f"Server is listening on {server_address[0]}:{server_address[1]}")
client_socket, client_address = server_socket.accept()        # # Accept incoming connection

# # Receive and print data from the client
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")
message = "Hello, client! This is the server."        # # Send a response back to the client
client_socket.sendall(message.encode())
client_socket.close()  # # Close the sockets
server_socket.close()
 

# +++++++++++++++++++++++++++++++++++  Client Code: +++++++++++++++++++++++++++++++++++ 

 
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # # Create a TCP/IP socket
server_address = ('localhost', 12345)    # # Define the server address and port 
client_socket.connect(server_address)      # # Connect the socket to the server address and port
message = "Hello, server! This is the client."        # # Send data to the server
client_socket.sendall(message.encode())
data = client_socket.recv(1024)           # # Receive and print data from the server
print(f"Received: {data.decode()}")
client_socket.close()


# Here's how it works:

# 1. The server creates a TCP/IP socket and binds it to a specific address and port.
# 2. It listens for incoming connections using `server_socket.listen(1)`.
# 3. When a client attempts to connect, `server_socket.accept()` accepts the incoming connection and returns a new socket (`client_socket`) and the address of the client.
# 4. The server receives data from the client using `client_socket.recv(1024)`.
# 5. It then sends a response back to the client using `client_socket.sendall(message.encode())`.
# 6. Both the client and server close their respective sockets after the communication.

# Make sure to run the server code first, followed by the client code. You can adjust the address and port as needed for your specific use case.