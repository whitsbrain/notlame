import os
import shutil


root_path = r"M:\Music\Various Artists"

with open("dest_dirsa.txt") as read_file1:
    for dd in read_file1:
            dd = dd.rstrip("\n")
            file_path = root_path + "\\" + (dd)
            print(file_path)
            # print(os.getcwd())
            
            try:
                shutil.copy('poster_Lost-vol-171-180.jpg', file_path)
                print("File copied successfully.")
            
            # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            
            # If there is any permission issue
            except PermissionError:
                print("Permission denied.")
            
            # For other errors
            except:
                print("Error occurred while copying file.")
