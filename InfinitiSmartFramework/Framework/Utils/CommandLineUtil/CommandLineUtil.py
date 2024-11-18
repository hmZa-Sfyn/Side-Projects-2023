""" Command ine Commands Processing MODULE """ 

import os , colorama , string , random , math , time , datetime , subprocess , sys , argparse
from turtle import color


class CommandLineTool:
    def __init__(self, description):
        """
        Initializes the CommandLineTool instance.
        
        Parameters:
            description (str): Description of the command-line tool.
        """
        self.parser = argparse.ArgumentParser(description=description)
        self.subparsers = self.parser.add_subparsers(dest='command', help='Available commands')

    def add_command(self, command, help_message, handler):
        """
        Adds a command to the command-line tool.
        
        Parameters:
            command (str): The name of the command.
            help_message (str): Help message for the command.
            handler (function): The function to handle the command.
        """
        parser = self.subparsers.add_parser(command, help=help_message)
        parser.set_defaults(handler=handler)

    def parse_args(self):
        """
        Parses command-line arguments and executes the corresponding command handler.
        """
        args = self.parser.parse_args()
        if hasattr(args, 'handler'):
            args.handler(args)
        else:
            self.parser.print_help()

def handle_hello_command(args):
    """
    Handler function for the 'hello' command.
    
    Parameters:
        args: Parsed command-line arguments.
    """
    print("Hello, World!")

def handle_echo_command(args):
    """
    Handler function for the 'echo' command.
    
    Parameters:
        args: Parsed command-line arguments.
    """
    print(args.message)

def handle_system_command(args):
    """
    Handler function for the 'system' command.
    
    Parameters:
        args: Parsed command-line arguments.
    """
    result = subprocess.run(args.command, shell=True)
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}")

# Example usage:
# if __name__ == "__main__":
#     tool = CommandLineTool("Simple Command-Line Tool")
#     tool.add_command("hello", "Prints 'Hello, World!'", handle_hello_command)
#     tool.add_command("echo", "Echoes a message", handle_echo_command)
#     tool.add_command("system", "Executes a system command", handle_system_command)
#     tool.parse_args()