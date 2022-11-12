import os
import shutil


def various_artists():
    source_path = r"M:\Music\Various Artists"

    with open("dest_dirs.txt") as read_file1:
        for dd in read_file1:
            dd = dd.rstrip("\n")
            try:
                os.chdir(source_path + "\\" + (dd))
                if os.path.isdir('__MACOSX'):
                    shutil.rmtree('__MACOSX')
                    print(dd, " - **DELETED** MACOSX directory")
                else:
                    print(dd, " - No MACOSX directory exists")
            except:
                print(dd, ' is not a directory')


def temp_dir():
    source_path = r"M:\Temp"

    with open("dest_dirs.txt") as read_file1:
        for dd in read_file1:
            dd = dd.rstrip("\n")
            try:
                os.chdir(source_path + "\\" + (dd))
                if os.path.isdir('__MACOSX'):
                    shutil.rmtree('__MACOSX')
                    print(dd, " - **DELETED** MACOSX directory")
                else:
                    print(dd, " - No MACOSX directory exists")
            except:
                print(dd, ' is not a directory')

temp_dir()
