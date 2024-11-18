import socket

# Define the server address and port
HOST = '192.168.0.141'  # Change this to the server's actual IP address if needed
PORT = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

try:
    try:
     while True:
        # Get input from the user
        command = input("Enter a command to execute: ")
        
        if command.lower() == "exit":
            break
        
        # Send the command to the server
        client_socket.send(command.encode())
        
        # Receive and display the response from the server
        response = client_socket.recv(1024).decode()
        print("Server response:", response)
    except:
     try:
      while True:
        # Get input from the user
        command = input("Enter a command to execute: ")
        
        if command.lower() == "exit":
            break
        
        # Send the command to the server
        client_socket.send(command.encode())
        
        # Receive and display the response from the server
        response = client_socket.recv(1024).decode()
        print("Server response:", response)
     except:
      try:
       while True:
        # Get input from the user
        command = input("Enter a command to execute: ")
        
        if command.lower() == "exit":
            break

        if command.lower() == "exit":
           print("WRITE SOMETHING PLEASE:..........")
           # Send the command to the server
           client_socket.send("nothing to write")
        else:
          # Send the command to the server
          client_socket.send(command.encode())
       
        
        # Receive and display the response from the server
        response = client_socket.recv(1024).decode()
        print("Server response:", response)
      except:
          print("MANY TRYED.. MOST OF THEM FAILED:....")
          # Send the command to the server
          client_socket.send("ERROR AT SENDER..........[DANGER]")
          client_socket.close()
except KeyboardInterrupt:
    pass

# Close the client socket
client_socket.close()
