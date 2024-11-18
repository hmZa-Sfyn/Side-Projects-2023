""" This module provides logger util to the program """
import os , colorama , string , random , math , time , datetime
from turtle import color

class Colors:
    # ANSI escape codes for colors
    reset = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    bright_black = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"

class Logger:
    def __call__(log_text):
        print(colorama.Fore.LIGHTBLUE_EX,log_text,colorama.Fore.RESET)
        
    def Success(log_text):
        print(colorama.Fore.GREEN,log_text,colorama.Fore.RESET)
        
    def Error(log_text):
        print(colorama.Fore.LIGHTRED_EX,log_text,colorama.Fore.RESET)
        
    def Warning(log_text):
        print(colorama.Fore.LIGHTYELLOW_EX,log_text,colorama.Fore.RESET)
        
    def Output(log_text):
        print(colorama.Fore.LIGHTCYAN_EX,log_text,colorama.Fore.RESET)
        
class Display:
    def Table(datax,heading):
        h1 = heading
        x = 1
        data = []
        
        data = datax

        print(f"{Colors.bright_black}╭──────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮")
        print(f"{Colors.bright_black}│ {Colors.bright_magenta}####{Colors.reset} {Colors.bright_black}│{Colors.reset} {Colors.bright_magenta}{h1:<129}{Colors.reset} {Colors.bright_black} │")
        print(f"{Colors.bright_black}├──────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤")
        for _ in range(len(data)):


            ido = ""

            print(f"{Colors.bright_black}│ {Colors.bright_magenta}{x:<4}{Colors.reset} {Colors.bright_black}│{Colors.reset} {Colors.bright_magenta}{data[_]:<129}{Colors.reset} {Colors.bright_black} │")
            
            x = x +1
        print(f"{Colors.bright_black}╰──────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯")