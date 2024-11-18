""" Command ine Commands Processing MODULE """ 

import os , colorama , string , random , math , time , datetime , subprocess , sys , argparse
from venv import logger
from warnings import catch_warnings
from re import A
from turtle import color
import shutil

import argparse
import subprocess
import json

import datetime
import colorama
import datetime
import colorama
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import CompleteStyle

from LoggerUtil import LoggerUtil as Logger
from LoaderUtil import JsonLoader as JsonLoader
from NewProjectUtil import CopyDirUtil as CopyDir

version = "1.2.3"
frameworks = os.listdir("E:/enchant/sbin/InfinitiSmartFramework/Framework/fwFileStructure") #JsonLoader.Load() #os.listdir("../fwFileStructure/")
langs = os.listdir("E:/enchant/sbin/InfinitiSmartFramework/Framework/ScriptingLanguages") #JsonLoader.Load() #os.listdir("../ScriptingLaguages/")
class EasyCommandLineTool:
    def __init__(self, description):
        self.desc = description
        # self.command_completer = WordCompleter(
        #     ['cli', 'project-types ls', 'conf-items ls', 'help new', 'help conf', 'new', 'conf', 'exit', 'quit'],
        #     ignore_case=True
        # )
            
    def print_gradient_ascii_art(self):
        # Example usage
#         ascii_art = f"""                           
# 8888888 888b    888 8888888888 8888888 888b    888 8888888 88888888888 8888888      8888888888 8888888b.         d8888 888b     d888 8888888888 888       888  .d88888b.  8888888b.  888    d8P  (V={version})
#   888   8888b   888 888          888   8888b   888   888       888       888        888        888   Y88b       d88888 8888b   d8888 888        888   o   888 d88P" "Y88b 888   Y88b 888   d8P   
#   888   88888b  888 888          888   88888b  888   888       888       888        888        888    888      d88P888 88888b.d88888 888        888  d8b  888 888     888 888    888 888  d8P    
#   888   888Y88b 888 8888888      888   888Y88b 888   888       888       888        8888888    888   d88P     d88P 888 888Y88888P888 8888888    888 d888b 888 888     888 888   d88P 888d88K     
#   888   888 Y88b888 888          888   888 Y88b888   888       888       888        888        8888888P"     d88P  888 888 Y888P 888 888        888d88888b888 888     888 8888888P"  8888888b    
#   888   888  Y88888 888          888   888  Y88888   888       888       888        888        888 T88b     d88P   888 888  Y8P  888 888        88888P Y88888 888     888 888 T88b   888  Y88b   
#   888   888   Y8888 888          888   888   Y8888   888       888       888        888        888  T88b   d8888888888 888   "   888 888        8888P   Y8888 Y88b. .d88P 888  T88b  888   Y88b  
# 8888888 888    Y888 888        8888888 888    Y888 8888888     888     8888888      888        888   T88b d88P     888 888       888 8888888888 888P     Y888  "Y88888P"  888   T88b 888    Y88b
#         """

        morechars = ["!","@","#","$","%","^","&","*","/?","\\?",":",";"]
        ascii_art = ''.join(random.choice(string.ascii_letters+string.hexdigits+string.octdigits+"\n"+string.digits+str(morechars)) for _ in range(200))
        
        # Define color gradient
        gradient = [colorama.Fore.BLUE,colorama.Fore.LIGHTBLUE_EX,colorama.Fore.LIGHTCYAN_EX]
    
        # Print ASCII art with gradient
        for i, line in enumerate(ascii_art.splitlines()):
            color = gradient[i % len(gradient)]
            print(color + line+colorama.Back.RESET)  

    def serve(self):
        # Initialize colorama
        colorama.init()

        # Print ASCII art with gradient
        self.print_gradient_ascii_art()

        # Reset colorama
        colorama.deinit()
        print(colorama.Fore.GREEN+self.desc+colorama.Fore.RESET)
        commands = sys.argv
        
        if len(commands) >= 2:
            self.pc(commands)
        else:
            self.serveforever()
            
                
    def serveforever(self):
        # custom_style = Style.from_dict({
        #     'prompt': 'ansiwhite',
        #     'time': 'ansiblue',
        #     'command': 'ansigreen',
        #     'error': 'ansired',
        #     'success': 'ansibrightgreen',
        #     'exit': 'ansired',
        # })

        # Initialize PromptSession with auto_suggest and history features
        #session = PromptSession(completer=self.command_completer, complete_style=CompleteStyle.READLINE_LIKE)

        while True:
            try:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                #print(colorama.Back.LIGHTBLUE_EX+colorama.Fore.LIGHTWHITE_EX+f" {current_time} !!"+colorama.Fore.RESET+colorama.Back.RESET)
                # prompt = [
                #     ('class:prompt', 'Inf'),
                #     ('class:command', ' % ')
                # ]
                # Display the prompt with color and style
                cmd = input(colorama.Back.LIGHTBLUE_EX+colorama.Fore.LIGHTWHITE_EX+f" {current_time} "+colorama.Fore.RESET+colorama.Back.RESET+colorama.Back.LIGHTWHITE_EX+colorama.Fore.LIGHTBLUE_EX+f" Inf{{{version}}} :="+colorama.Fore.RESET+colorama.Back.RESET+" ") #session.prompt(prompt, style=custom_style)
                commands = cmd.strip().split()

                if commands and commands[0].lower() in ['exit', 'quit']:
                    print(colorama.Fore.YELLOW + "Exiting..." + colorama.Fore.RESET)
                    break
                elif commands and commands[0].lower() in ['cls','clear']:
                    os.system("cls")

                if commands:
                    self.pc(commands)
            except (KeyboardInterrupt, EOFError):
                print(colorama.Fore.YELLOW + "\nExiting..." + colorama.Fore.RESET)
                break
            
    def pc(self,commands):
        try:
            if commands[0] == "FrameworkcliUtil.py":
                commands.remove("FrameworkcliUtil.py")
            else:
                pass
        
            if commands[0].lower() == "cli":
                self.serveforever()
            elif "exit " in commands[0].lower() or "quit " in commands[0].lower():
                exit()
            elif commands[0].lower() == "project-types":
                if commands[1]:
                    if commands[1] == "ls":
                        Logger.Display.Table(frameworks,"Project Types")
            elif commands[0].lower() == "conf-items":
                if commands[1]:
                    if commands[1] == "ls":
                        Logger.Display.Table(langs,"Items list")
            elif commands[0].lower() == "help":
                if len(commands) >= 2:
                    if commands[1] == "new":
                        commands = ["new $PROJECT_NAME $PROJECT_TYPE : Create a new project with name $PROJECT_NAME and type $PROJECT_TYPE in current dir.","new $PN $PT -loc $DIR_PATH : Create a new project with name $PN and type $PT in $DIR_PATH dir."]
                        Logger.Display.Table(commands,"`New` perimeter description & usage.")
                    elif commands[1] == "conf":
                        commands = ["conf $ITEM : Config an $ITEM in current dir.","conf $ITEM -loc $DIR_PATH: Config an $ITEM in $DIR_PATH dir."]
                        Logger.Display.Table(commands,"`Conf` perimeter description & usage.")
                else:
                    commands = ["new $PROJECT_NAME $PROJECT_TYPE : Create a new project with name $PROJECT_NAME and type $PROJECT_TYPE in current dir.","new $PN $PT -loc $DIR_PATH : Create a new project with name $PN and type $PT in $DIR_PATH dir."]
                    Logger.Display.Table(commands,"`New` perimeter description & usage.")
                    commands = ["conf $ITEM : Config an $ITEM in current dir.","conf $ITEM -loc $DIR_PATH: Config an $ITEM in $DIR_PATH dir."]
                    Logger.Display.Table(commands,"`Conf` perimeter description & usage.")
            elif commands[0].lower() == "new":
                project_name = commands[1]
            
                # ListFrameWORKS = ""
                # for _ in frameworks:
                #    ListFrameWORKS += F" {_}; "
                # print(colorama.Fore.LIGHTWHITE_EX+ListFrameWORKS+colorama.Fore.RESET)
                #Logger.Display.Table(frameworks,"Project Types")
            
                #project_type = input(colorama.Fore.GREEN + "Select Project-Type: " + colorama.Fore.RESET)
                project_type = commands[2]
                prj = False;
            
                if project_name != "":
                    if project_type in frameworks:
                        prj = True
                    else:
                        Logger.Logger.Error(f"! Please type a valid project type, `{project_type}` is not a valid Project type. Type `project-types ls` to list project types.")
                        #exit()
                    
                Logger.Logger.Success(f"Creating:\n  Project-name: `{project_name}` \n  Project-type: `{project_type}`")
            
                locat = "./"

                if commands[3]:
                    if commands[3].lower() == "-loc":
                        locat = commands[4]

                try:
                    if locat != "":
                        #os.system( f"cd {locat} && mkdir {project_name}" )
                        #try:
                            #print("1")
                            os.mkdir(f"{locat}/{project_name}")
                            CopyDir.copy_directory(f"E:/enchant/sbin/InfinitiSmartFramework/Framework/fwFileStructure/{project_type}/src/", f"{locat}/{project_name}")
                            Logger.Logger.Success(f"Created:\n  Project-name: `{project_name}` \n  Project-type: `{project_type}`\n  Project-Location: `{locat}`")
                            #exit()
                        # except:
                        #     print("2")
                        #     os.mkdir(f"{locat}{project_name}")
                        #     CopyDir.copy_directory(f"E:\enchant\sbin\InfinitiSmartFramework\Framework\fwFileStructure\{project_name}\src", f"{locat}{project_name}")
                        #     Logger.Logger.Success(f"Created:\n  Project-name: `{project_name}` \n  Project-type: `{project_type}`\n  Project-Location: `{locat}`")
                        #     exit()
                    else:
                        #print("3")
                        os.mkdir(f"{project_name}")
                        CopyDir.copy_directory(f"E:/enchant/sbin/InfinitiSmartFramework/Framework/fwFileStructure/{project_type}/src/", f"{project_name}")
                        Logger.Logger.Success(f"Created:\n  Project-name: `{project_name}` \n  Project-type: `{project_type}`\n  Project-Location: `{locat}`")
                        #exit()
                    
                except Exception as e:
                    Logger.Logger.Error(e)
            elif commands[0].lower() == "conf":
            
                # ListFrameWORKS = ""
                # for _ in frameworks:
                #    ListFrameWORKS += F" {_}; "
                # print(colorama.Fore.LIGHTWHITE_EX+ListFrameWORKS+colorama.Fore.RESET)
                #Logger.Display.Table(frameworks,"Project Types")
            
                #project_type = input(colorama.Fore.GREEN + "Select Project-Type: " + colorama.Fore.RESET)
                project_type = commands[1]
                project_name = project_type
                prj = False;
            
                if project_name != "":
                    if project_type in langs:
                        prj = True
                    else:
                        Logger.Logger.Error(f"! Please type a valid item name, `{project_type}` is not a valid item. Type `conf-items ls` to list project types.")
                        #exit()
                    
                Logger.Logger.Success(f"Configure:\n  Item-name: `{project_name}` \n  Item-type: `{project_type}`")
            
                locat = "./"

                if commands[2]:
                    if commands[2].lower() == "-loc":
                        locat = commands[3]

                try:
                    if locat != "":
                        #os.system( f"cd {locat} && mkdir {project_name}" )
                        #try:
                            #print("1")
                            os.mkdir(f"{locat}/{project_name}")
                            CopyDir.copy_directory(f"E:/enchant/sbin/InfinitiSmartFramework/Framework/ScriptingLanguages/{project_type}/ConfDeploy/", f"{locat}/{project_name}")
                            Logger.Logger.Success(f"Configured:\n  Item-name: `{project_name}` \n  Item-type: `{project_type}`\n  Location: `{locat}`")
                            #exit()
                        # except:
                        #     print("2")
                        #     os.mkdir(f"{locat}{project_name}")
                        #     CopyDir.copy_directory(f"E:\enchant\sbin\InfinitiSmartFramework\Framework\fwFileStructure\{project_name}\src", f"{locat}{project_name}")
                        #     Logger.Logger.Success(f"Created:\n  Project-name: `{project_name}` \n  Project-type: `{project_type}`\n  Project-Location: `{locat}`")
                        #     exit()
                    else:
                        #print("3")
                        os.mkdir(f"{project_name}")
                        CopyDir.copy_directory(f"E:/enchant/sbin/InfinitiSmartFramework/Framework/ScriptingLanguages/{project_type}/ConfDeploy/", f"{project_name}")
                        Logger.Logger.Success(f"Configured:\n  Item-name: `{project_name}` \n  Item-type: `{project_type}`\n  Location: `{locat}`")
                        #exit()    
                except Exception as e:
                    Logger.Logger.Error(e)
            else:
                Logger.Logger.Error(f"[!] No such command `{commands[0]}`")
        except Exception as exxxxx:
            Logger.Logger.Error(exxxxx)

                 
                



        


# # Handler function for the 'hello' command
# def handle_hello_command(args):
#     """
#     Handler function for the 'hello' command.
    
#     Parameters:
#         args: Parsed command-line arguments.
#     """
#     print("Hello, World!")

# # Handler function for the 'echo' command
# def handle_echo_command(args):
#     """
#     Handler function for the 'echo' command.
    
#     Parameters:
#         args: Parsed command-line arguments.
#     """
#     print(args.arguments)

# # Handler function for the 'system' command
# def handle_system_command(args):
#     """
#     Handler function for the 'system' command.
    
#     Parameters:
#         args: Parsed command-line arguments.
#     """
#     result = subprocess.run(args.arguments, shell=True)
#     if result.returncode != 0:
#         print(f"Command failed with return code {result.returncode}")

# # Create an instance of EasyCommandLineTool
# tool = EasyCommandLineTool("Simple Command-Line Tool")

# # Set handler functions for the commands
# tool.set_handler('hello', handle_hello_command)
# tool.set_handler('echo', handle_echo_command)
# tool.set_handler('system', handle_system_command)

# # Parse command-line arguments and execute the corresponding command
# tool.parse_args()
