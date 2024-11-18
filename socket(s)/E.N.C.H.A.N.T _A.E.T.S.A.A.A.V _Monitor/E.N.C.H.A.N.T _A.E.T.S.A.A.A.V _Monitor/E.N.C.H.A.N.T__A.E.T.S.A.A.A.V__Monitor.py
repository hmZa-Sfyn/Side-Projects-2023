
import socket
import matplotlib.pyplot as plt
import threading
from datetime import datetime
import time

# Global variables for monitoring
timestamps = []
connection_statuses = []

def update_chart():
    while True:
        plt.clf()  # Clear the previous chart
        plt.plot(timestamps, connection_statuses, marker='o')
        plt.xlabel('Time')
        plt.ylabel('Connection Status')
        plt.title('Server-Client Connection Status')
        plt.gcf().autofmt_xdate()
        plt.grid()
        plt.pause(5)  # Update the chart every 5 seconds

def run_monitor():
    monitor_thread = threading.Thread(target=update_chart)
    monitor_thread.daemon = True
    monitor_thread.start()

def monitor_connection():
    global timestamps, connection_statuses
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        try:
            client.connect(('127.0.0.1', 12345))  # Replace with the actual server IP and port
            connection_statuses.append(1)
        except ConnectionRefusedError:
            connection_statuses.append(0)
        finally:
            timestamps.append(datetime.now())
            time.sleep(5)  # Check connection status every 5 seconds

if __name__ == "__main__":
    run_monitor()
    monitor_connection()
