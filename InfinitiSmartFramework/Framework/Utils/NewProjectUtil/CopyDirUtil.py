import os
import shutil

""" Module for copying files and folders to new project location """

def check_dir(directory):
    """
    Check if the given directory exists.
    
    :param directory: Path to the directory to check.
    :return: True if the directory exists, False otherwise.
    """
    return os.path.isdir(directory)

def copy_directory(src_directory, dst_directory):
    """
    Copy all contents from the source directory to the destination directory, including all subdirectories and files.
    
    :param src_directory: Path to the source directory.
    :param dst_directory: Path to the destination directory.
    """
    # Ensure destination directory exists
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    # Copy the entire directory tree
    for item in os.listdir(src_directory):
        src_path = os.path.join(src_directory, item)
        dst_path = os.path.join(dst_directory, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)
    return True
        #print(f"Copied {src_path} to {dst_path}")
