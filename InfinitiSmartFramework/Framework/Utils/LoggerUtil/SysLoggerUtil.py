import logging
import os
import subprocess

class SystemLogger:
    def __init__(self, log_filename='system_log.txt'):
        """
        Initializes the SystemLogger instance.
        
        Parameters:
            log_filename (str): The name of the file where log messages will be saved.
                                Defaults to 'system_log.txt'.
        
        Description:
            Sets up logging configuration to capture log messages in a variable
            and a file. Initializes an empty list to store log messages and configures
            the logger with a custom handler to capture these messages.
        """
        self.log_filename = log_filename
        self.log_messages = []
        
        # Set up logging configuration
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger()
        
        # Add a custom handler to capture log messages in a variable
        self.log_handler = logging.StreamHandler(self)
        self.logger.addHandler(self.log_handler)
    
    def write(self, message):
        """
        Captures a log message and stores it in the log_messages list.
        
        Parameters:
            message (str): The message to be logged.
        
        Description:
            Appends the log message to the log_messages list and logs the
            message using the logger. The logger writes the message to the 
            log handler, which captures it in the variable.
        """
        self.log_messages.append(message)
        self.logger.handlers[0].stream = self.log_messages
        self.logger.info(message)
    
    def flush(self):
        """
        Placeholder method required by logging.StreamHandler.
        
        Description:
            This method does nothing and is included to satisfy the
            requirements of the logging.StreamHandler interface.
        """
        pass
    
    def save_log_to_file(self):
        """
        Saves the collected log messages to a file.
        
        Description:
            Opens the specified log file in write mode and writes all
            the log messages stored in the log_messages list to the file.
        """
        with open(self.log_filename, 'w') as log_file:
            log_file.write('\n'.join(self.log_messages))
    
    def open_log_file(self):
        """
        Saves log messages to a file and opens the file.
        
        Description:
            Calls save_log_to_file to write log messages to the specified log file.
            Opens the log file using the default application for text files based on
            the operating system.
        """
        # Save log messages to file
        self.save_log_to_file()
        
        # Open the log file
        if os.name == 'nt':  # For Windows
            os.startfile(self.log_filename)
        elif os.name == 'posix':  # For Unix-like systems
            subprocess.call(('xdg-open', self.log_filename))
        else:
            print(f"Unsupported OS: {os.name}")

    def __call__(self):
        """
        Opens the log file when the class instance is called as a function.
        
        Description:
            Calls the open_log_file method to save and open the log file
            when the instance of SystemLogger is invoked directly.
        """
        self.open_log_file()

### Example usage ###

# if __name__ == "__main__":
#     """
#     Demonstrates the usage of the SystemLogger class.
    
#     Description:
#         Creates an instance of SystemLogger, logs some messages, and opens the log file.
#     """
#     logger = SystemLogger()
    
#     logger.write("Starting the process...")
#     logger.write("Process running...")
#     logger.write("Process completed successfully.")
    
#     # When you want to open the log file
#     logger()
