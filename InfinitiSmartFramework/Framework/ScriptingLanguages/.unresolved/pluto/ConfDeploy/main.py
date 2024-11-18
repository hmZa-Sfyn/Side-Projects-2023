### HELLO FROM NUPYTHON ###

PlutoPath = "E:/enchant/sbin/InfinitiSmartFramework/Framework/ScriptingLanguages/pluto/sbin/ipm.py"
import os
import sys

"""
Main
----

Command line interface.
"""


try:
    argv2 = sys.argv[1]
    #print(argv2)
    argv1 = argv2.replace("//","/")
    os.system(f'python {PlutoPath} lun {sys.argv[1]}')
except Exception as exxx :
    print(exxx)