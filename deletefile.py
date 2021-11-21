import os


root_path = r"E:\Media\Music\Various Artists"

with open("dest_dirs.txt") as read_file1:
    for dd in read_file1:
            dd = dd.rstrip("\n")
            os.chdir(root_path + "\\" + (dd))
            print(os.getcwd())
            if os.path.isfile('poster.jpeg'):
                os.remove('poster.jpeg')
            else:
                print("No poster.jpeg file exists")
