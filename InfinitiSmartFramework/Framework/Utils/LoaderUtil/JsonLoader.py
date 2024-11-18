""" Module for loading json """

import json

def Load(file_path):
    with open(file_path , "r"):
        res = json.load()
    return res