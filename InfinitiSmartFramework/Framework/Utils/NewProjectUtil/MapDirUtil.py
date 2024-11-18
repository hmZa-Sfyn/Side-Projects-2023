""" This module provides file structure mapping to the program """
from genericpath import isfile
import os , colorama , string , random , math , time , datetime
from LoggerUtil import LoggerUtil as println

def MapDir(Project_type,version):
    map_dir = f".././fwFileStructure/{Project_type}/{version}"
    Map(map_dir,0)
    
def Map(map_dir,indent):

    for _ in os.listdir(map_dir):
        #println.Logger.Output(_)
        s_item = f"{map_dir}/{_}"
        if os.path.isfile(s_item):
            println.Logger.Output(" "*indent+f"└───{_}")
        elif os.path.isdir(s_item):
            println.Logger.Output(" "*indent+f"└───{_}")
            Map(s_item,indent+2)
        
    return "nothing"
    



