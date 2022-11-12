import os
import re

# For Various Artists, the source_path is source_path = r"M:\Music\Various Artists".  The title of the various
# artists album just needs to be added in the dest_dirs.txt file.  If you are doing a single band's album,
# you need to just include the directory path for the artist\album in dest_dirs.txt
source_path = r"M:\Music"

# This function will try to strip everything before the first dash ("index") in a file name.  It will add a space
# before the dash to prepare for an addition of a file number ("count"). The file name format that this function
# is building looks like my preferred format of "01 - filename.mp3"
def if_dash_in_name():
    dash = "-"
    with open("dest_dirsa.txt") as read_file1:
        for rf in read_file1:
            rf = rf.rstrip("\n")
            print(rf)
            file_path = source_path + "\\" + (rf)
            files = os.listdir(file_path)
            count = 0
            for i in files:
                count = count + 1
                index = i.rfind(dash)
                splitat = index
                artist, orig_title = i[:splitat], i[splitat:]
                try:
                    title, audiofile = orig_title.rsplit(".", 1)
                except ValueError as v:
                    print(f"There's probably no dash in filename {i}")
                if title[0] != " ":
                    title = " " + title
                if title[-1] == " ":
                    title = title.rstrip(title[-1])
                if title[2] != " ":
                    title = title[0:2] + " " + title[2:]
                new_title = str(count).zfill(2) + title + "." + audiofile
                os.rename(file_path + "\\" + (i), file_path + "\\" + (new_title))
                print(new_title)
                # hit_file.write(new_title)


# This function will remove any leading spaces before the filename.  For example, if a file name looks like
# 01 -  filename.mp3", this will allow only one space between the dash and first character of the file name.
def remove_extra_spaces():
    with open("dest_dirsa.txt") as read_file1:
        for rf in read_file1:
            rf = rf.rstrip("\n")
            print(rf)
            file_path = source_path + "\\" + (rf)
            files = os.listdir(file_path)
            for i in files:
                print(i)
                title, audiofile = i.rsplit(".", 1)
                track, title = title.split("-")
                if title[1] == " ":
                    new_title = title[1:]
                    final_title = track + "-" + new_title + "." + audiofile
                    os.rename(file_path + "\\" + (i), file_path + "\\" + (final_title))
                    print(final_title)


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

# if_dash_in_name()
# remove_extra_spaces()
no_dash_in_name()
