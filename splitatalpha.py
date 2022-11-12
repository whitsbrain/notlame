import os
import re

source_path = r"M:\Music"

# This function will split a file name at the first alphanumeric character.  For example, if the file name was
# like this: "[01] Lipstick", this function will split it at "L", and take "Lipstick" and prefix it with a count,
# so that files of an album are number to my preferred format of "03 - Lipstick".
# At of the last time I used this, it needed to be run after "renamefiles.py" so the original file name was
# spilt at the "-".  I want to try and include this file in a single function, but the files that I get from
# Bruce Brodeen (Not Lame, Power Pop Geek) have file names that are so goofy or varied, I just can't predict
# what the file names are going to be.
def if_bracket_in_name():
    with open("dest_dirsa.txt") as read_file1:
        for rf in read_file1:
            rf = rf.rstrip("\n")
            print(rf)
            file_path = source_path + "\\" + (rf)
            files = os.listdir(file_path)
            count = 0
            for i in files:
                count = count + 1
                print(i)
                match = re.compile("[^\W\d]").search(i)
                dump_number, title = [i[: match.start()], i[match.start() :]]
                new_title = str(count).zfill(2) + " - " + title
                os.rename(file_path + "\\" + (i), file_path + "\\" + (new_title))
                print(new_title)

# This function will split a file name at the first alphanumeric character.  For example, if the file name was
# like this: "01 Castles in Spain", this function will split it at "C", and take "Castles in Spain" and prefix it with a count,
# so that files of an album are number to my preferred format of "01 - Castles in Spain".
# I want to try and include this file in a single function, but the files that I get from
# Bruce Brodeen (Not Lame, Power Pop Geek) have file names that are so goofy or varied, I just can't predict
# what the file names are going to be.
def no_dash_in_name():
    with open("dest_dirsa.txt") as read_file1:
        for rf in read_file1:
            rf = rf.rstrip("\n")
            print(rf)
            file_path = source_path + "\\" + (rf)
            files = os.listdir(file_path)
            count = 0
            for i in files:
                count = count + 1
                print(i)
                match = re.compile("[^\W\d]").search(i)
                dump_number, title = [i[: match.start()], i[match.start() :]]
                new_title = str(count).zfill(2) + " - " + title
                os.rename(file_path + "\\" + (i), file_path + "\\" + (new_title))
                print(new_title)
                # splitat = index
                # artist, orig_title = i[:splitat], i[splitat:]

no_dash_in_name()
