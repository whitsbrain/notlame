import os
import shutil


root_path = r"E:\Media\Music\Various Artists"

with open("dest_dirs.txt") as read_file1:
    for dd in read_file1:
            dd = dd.rstrip("\n")
            file_path = root_path + "\\" + (dd)
            print(os.getcwd())
            shutil.copy('poster.jpeg', file_path)
