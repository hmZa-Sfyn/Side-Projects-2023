import socket


def run_client_backup(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            try:
                data = input("Enter data to send (or 'exit' to quit): ")
                client.send(data.encode('utf-8'))
                if not data:
                    print("..Connection..R E L O A D..")
                elif data == 'exit':
                    break
                elif data.startswith('cmd:'):
                    response = client.recv(1024).decode('utf-8')
                    print("Shell command output:")
                    print(response)
                elif data.startswith('speak:'):
                    print("speaking...")
                else:
                    server_response = client.recv(1024).decode('utf-8')
                    print(server_response)
            except socket.error as send_err:
                print(f"Error sending data: {send_err}")
                print("E R R O R:...Fix needed.................................................../reload=false.failedtoconnect/...")
    
    except socket.error as connect_err:
        print(f"Error connecting to server: {connect_err}")
    
    finally:
        client.close()

def run_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            try:
                data = input("Enter data to send (or 'exit' to quit): ")
                client.send(data.encode('utf-8'))
                if not data:
                    print("..Connection..R E L O A D..")
                elif data == 'exit':
                    break
                elif data.startswith('cmd:'):
                    response = client.recv(1024).decode('utf-8')
                    print("Shell command output:")
                    print(response)
                elif data.startswith('speak:'):
                    print("speaking...")
                else:
                    server_response = client.recv(1024).decode('utf-8')
                    print(server_response)
            except socket.error as send_err:
                print(f"Error sending data: {send_err}")
                if send_err == "[WinError 10053] An established connection was aborted by the software in your host machine":
                    server_host = '192.168.0.141'  # Change to the server's IP address
                    server_port = 12346        # Change to the server's port
                    run_client_backup(server_host, server_port)
                else:
                    print("E R R O R:...Fix needed.................................................../reload=false.failedtoconnect/...")
    
    except socket.error as connect_err:
        print(f"Error connecting to server: {connect_err}")
    
    finally:
        client.close()

if __name__ == "__main__":
    server_host = '192.168.0.141'  # Change to the server's IP address
    server_port = 12345        # Change to the server's port
    run_client(server_host, server_port)
