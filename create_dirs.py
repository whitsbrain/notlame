import os
import shutil

source_path = r"M:\Music\Various Artists"

# For "Various Artists", if you have a file with the directory names already created ("dest_dirs.txt"), use this:
with open("dest_dirs.txt") as read_file1:
    for dd in read_file1:
        dd = dd.rstrip("\n")
        os.chdir(source_path + "\\")
        print(os.getcwd())
        os.mkdir(dd)

# let's create 40 directories. starting the count at 201
# count = 201
# while count < 241:
#     print(source_path)
#     # os.chdir(os.path.join(source_path, "\\"))
#     os.chdir(source_path + "\\")
#     newdir = (
#         "Vol." + " " + str(count) + " - Not Lame Lost & Forgotten Power Pop Collection"
#     )
#     print(newdir)
#     os.mkdir(newdir)
#     count = count + 1
