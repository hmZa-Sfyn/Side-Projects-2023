import socket

def sender():
    receiver_ip = '192.168.0.141'  # Replace with the receiver's IP address
    port = 12345

    try:
        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender_socket.connect((receiver_ip, port))

        print("Type your messages. Type '-sys-cmd close connection -all_con_s' to close the connection.")
        while True:
            message = input("You: ")
            sender_socket.send(message.encode())
            if message == "-sys-cmd close connection -all_con_s":
                print("Closing the connection.")
                break

    except socket.error as e:
        print("Socket error:", e)
    except Exception as ex:
        print("An error occurred:", ex)
    finally:
        sender_socket.close()

if __name__ == "__main__":
    sender()
