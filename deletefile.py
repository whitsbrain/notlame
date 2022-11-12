import os


def various_artists():
    root_path = r"M:\Music\Various Artists"

    with open("dest_dirs.txt") as read_file1:
        for dd in read_file1:
            dd = dd.rstrip("\n")
            try:
                os.chdir(root_path + "\\" + (dd))
                print(os.getcwd())
                if os.path.isfile('.DS_Store'):
                    os.remove('.DS_Store')
                    print(dd, " .DS_Store file deleted")
                else:
                    print(dd, " No .DS_Store file exists")
            except:
                print(dd, ' is not a file')


def temp_dir():
    root_path = r"M:\Temp"

    with open("dest_dirs.txt") as read_file1:
        for dd in read_file1:
            dd = dd.rstrip("\n")
            try:
                os.chdir(root_path + "\\" + (dd))
                print(os.getcwd())
                if os.path.isfile('.DS_Store'):
                    os.remove('.DS_Store')
                    print(dd, " .DS_Store file deleted")
                else:
                    print(dd, " No .DS_Store file exists")
            except:
                print(dd, ' is not a file')

temp_dir()
