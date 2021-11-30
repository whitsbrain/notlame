import os

source_path = r"E:\Media\Music\Various Artists"

with open("dest_dirs.txt") as read_file1:
    for dd in read_file1:
        dd = dd.rstrip("\n")
        dir_path = source_path + "\\" + (dd)
        for dirpath, dirnames, filenames in os.walk(dir_path):
            # print('Current Path:', dirpath)
            print("Directories:", dirnames)
            # print('Files:', filenames)
            if not dirnames:
                print("No folder exists")
            else:
                os.rmdir(dir_path + "\\" + dirnames[0])
