import os
import time
import random
import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init()

def validate_parameters(how_much_time, how_much_ticks):
    """
    Validates the parameters for the loading animation.
    
    Parameters:
        how_much_time (float): The delay time between each tick of the animation.
        how_much_ticks (int): The total number of ticks for the animation.
    
    Description:
        Ensures the delay time is a positive float and the number of ticks is a positive integer.
    
    Raises:
        ValueError: If the parameters are not valid.
    """
    if not isinstance(how_much_time, (int, float)) or how_much_time <= 0:
        raise ValueError("how_much_time must be a positive number.")
    if not isinstance(how_much_ticks, int) or how_much_ticks <= 0:
        raise ValueError("how_much_ticks must be a positive integer.")

def load_animation(how_much_time, how_much_ticks):
    """
    Displays a loading animation in the terminal.
    
    Parameters:
        how_much_time (float): The delay time between each tick of the animation.
        how_much_ticks (int): The total number of ticks for the animation.
    
    Description:
        Displays a rotating line animation with color for the specified duration.
        Uses carriage return to overwrite the animation characters in place.
    """
    validate_parameters(how_much_time, how_much_ticks)
    
    animation_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴']
    colors = [Fore.WHITE, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    
    for _ in range(how_much_ticks):
        for char in animation_chars:
            color = Fore.WHITE
            print( color + char *1 + Style.RESET_ALL, end='\r', flush=True)
            time.sleep(how_much_time)
    
    # Clear the animation by overwriting with spaces
    print(' ' * (len(animation_chars[-1]) * 2), end='\r', flush=True)
    print(Fore.GREEN + "Loading complete!" + Style.RESET_ALL)

# Example usage:
if __name__ == "__main__":
    print("Starting the loading animation:")
    load_animation(0.1, 20)
    print("This is other text that stays on the screen.")
