import os
import shutil

source_path = r"E:\Media\Music\Various Artists"

with open("dest_dirs.txt") as read_file1:
    for dd in read_file1:
        dd = dd.rstrip("\n")
        os.chdir(source_path + "\\")
        print(os.getcwd())
        os.mkdir(dd)
