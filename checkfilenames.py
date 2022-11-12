import os

source_path = r"M:\Music\Various Artists"


def file_format_check():
    my_list = []
    with open("dest_dirs.txt") as read_file1:
        for dd in read_file1:
            dd = dd.rstrip("\n")
            dir_path = source_path + "\\" + (dd)
            for dirpath, dirnames, filenames in os.walk(dir_path):
                my_list.append((dirpath, filenames))
        return my_list


new_file = open("dir_scan.txt", "w")

for filename in file_format_check():
    new_file.write(str(filename))
    new_file.write("\n")

new_file.close()
