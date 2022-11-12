import os

def various_artists():
    source_path = r"M:\Music\Various Artists"

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
                    # os.rmdir(dir_path + "\\" + dirnames[0])
                    print('hi')


def temp_dir():
    source_path = r"M:\Temp"

    with open("dest_dirsa.txt") as read_file1:
        for dd in read_file1:
            dd = dd.rstrip("\n")
            dir_path = source_path + "\\" + (dd)
            print(dir_path)
            os.rmdir(dir_path)

temp_dir()
