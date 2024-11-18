import os , colorama , string , random , math , time , datetime , subprocess

from AnimationUtil import LoaderUtil as LoaderAnimation
from NewProjectUtil import MapDirUtil as MapDir
from NewProjectUtil import CopyDirUtil as CopyDir
#from CommandLineUtil import CommandLineUtil as Cmdln
from CommandLineUtil import CommandLineUtil2 as Cmdln

#LoaderAnimation.load_animation(0.1,10)

#print(MapDir.MapDir("Simple-Project","1.0.1"))

# src_dir = "E:/enchant/sbin/InfinitiSmartFramework/Framework/"
# dst_dir = "F:/"

# if CopyDir.check_dir(src_dir):
#     CopyDir.copy_directory(src_dir, dst_dir)
# else:
#     print(f"Directory {src_dir} does not exist.")

# Create an instance of EasyCommandLineTool
cmdtool = Cmdln.EasyCommandLineTool("Infiniti Framework Commandline (Cmdln) v1.0.1")
cmdtool.serve()