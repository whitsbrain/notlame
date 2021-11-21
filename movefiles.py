import os
from pathlib import Path
import shutil

root_path = r"E:\Media\Music\Various Artists"

with open("dest_dirsa.txt") as read_file1:
    for dd in read_file1:
            dd = dd.rstrip("\n")
            os.chdir(root_path + "\\" + (dd))
            dd_subdir = os.listdir(root_path + "\\" + (dd))
            dd_source = dd_subdir[0]
            dd_orig = root_path + "\\" + dd +"\\" + (dd_source + "\\")
            dd_target = root_path + "\\" + (dd)
            # print('dd_orig is ', dd_orig)
            # print('dd_target is ', dd_target)
            for src_file in Path(dd_orig).glob('*.*'):
                shutil.move(src_file, dd_target)
