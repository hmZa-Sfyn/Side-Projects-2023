# receiver_continuous_save_to_d.py

import os
import socket
import time

def receive_and_save_screenshot(connection, save_directory):
    # Receive screenshot data
    screenshot_data = connection.recv(1024)  # Adjust buffer size as needed

    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Save the received data as an image
    screenshot_filename = f'received_screenshot_{time.time()}.png'
    screenshot_path = os.path.join(save_directory, screenshot_filename)
    with open(screenshot_path, 'wb') as file:
        file.write(screenshot_data)

    print(f"Screenshot saved to: {screenshot_path}")

# Create a socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.193', 12345))  # Replace with your IP and port
s.listen(1)

save_directory = 'D:/received_screenshots'  # Change this to your desired directory

print("Waiting for a connection...")

while True:
    connection, address = s.accept()
    print(f"Connected to {address}")

    receive_and_save_screenshot(connection, save_directory)
    print("Screenshot received and saved.")
    print("------------------------------- S T A N D   B Y ------------------------------------")

    # Close the connection
    connection.close()
