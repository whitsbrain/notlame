import zipfile
import os
import re


def create_dir_and_unzip():
    # This function assumes that the source of the zip files(s) will be in the HOME/Downloads directory and the destination directories
    # should be created in "M:\Music"
    source_path = os.path.join(os.environ.get("HOME"), "Downloads")
    dest_path = r"M:\Music"
    # dotz and dash are used to split the Bandcamp zip file into segments to create directories and unzip music files into the new directory
    dotz = ".z"
    dash = "-"
    # This is where the zip file name record(s) are read from. The .zip file names must first be manually added to the "source_zips.txt" file
    with open("source_zips.txt") as read_file1:
        for sz in read_file1:
            sz = sz.rstrip("\n")
            with zipfile.ZipFile(source_path + "\\" + (sz), "r") as zip_ref:
                # This section is where the .zip extention and location of a dash in the record are found
                index_dotz = sz.rfind(dotz)
                index_dash = sz.rfind(dash)
                splitdotz = index_dotz
                splitdash = index_dash
                # This line uses the location of the dot to split the file name from the extension (.zip)
                artist, zip_ext = sz[:splitdotz], sz[splitdotz:]
                # This line uses the location of the dash to split the artist name from the album name
                artist_new, album = artist[:splitdash], artist[splitdash:]
                # There's a space at the end of the artist name so it is stripped off here
                artist_new = artist_new.rstrip(" ")
                # This section creates a list from the album string using regex to break the string at the first alphanumeric character
                match = re.compile("[^\W\d]").search(album)
                title = [album[: match.start()], album[match.start() :]]
                # This line selects the second item in the list, which is the album name
                title = title[1]
                # This line creates a variable for the potential existance of the artist's directory
                check_artist_dir = dest_path + "\\" + artist_new
                # This section checks to see if the artist (artist_new) directory already exists and if True, changes the current working
                # directory to the artist's directory
                if os.path.exists(check_artist_dir):
                    current_directory = os.getcwd()
                    print("Your current working directory is %s" % current_directory)
                    try:
                        os.chdir(check_artist_dir)
                        print("The working directory has been changed!")
                        # print("WD: %s " % os.getcwd())
                    except NotADirectoryError:
                        print("You have not chosen a directory.")
                    except FileNotFoundError:
                        print("The folder was not found. The path is incorrect.")
                    except PermissionError:
                        print("You do not have access to this folder/file.")
                    finaldir = title
                    # This line creates the album subdirectory inside the artist directory
                    os.mkdir(finaldir)
                    # This line extracts the music files from the zip file
                    zip_ref.extractall(finaldir)
                    # This line creates a variable that is returned to use in "dash_in_name" function
                    rename_dir = check_artist_dir + "\\" + title
                else:
                    # If the artist directory doesn't exist, this line concatenates the destination path with the newly created variables
                    finaldir = dest_path + "\\" + artist_new + "\\" + title
                    # This line creates the album and artist directories
                    os.makedirs(finaldir)
                    # This line extracts the music files from the zip file
                    zip_ref.extractall(finaldir)
                    # This line creates a variable that is returned to use in "dash_in_name" function
                    rename_dir = finaldir
    return rename_dir


def dash_in_name(filesdir):
    # This line uses the directory passed from "create_dir_and_unzip" (where the music files were unzipped to)
    files = os.listdir(filesdir)
    count = 0
    # This line reads in all of the music files
    for i in files:
        print("Source file is :", i)
        # This section finds the second dash in the file name and also builds a count to use to number the music files
        occurrence = 2
        inilist = [d.start() for d in re.finditer(r"-", i)]
        if len(inilist) >= 2:
            count = count + 1
            artist, orig_title = (
                i[: inilist[occurrence - 1]],
                i[inilist[occurrence - 1] :],
            )
            # In case there are non-music files with the same dashed name format, this if statement will skip over them and not rename them
            if orig_title.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
                print(i, " is not a music file. Skipped.")
                continue
            # This section finds the first alphanumeric character, which cuts off all the leading numbers, dashes, and spaces
            match = re.compile("[^\W\d]").search(orig_title)
            dump_number, orig_title = [
                orig_title[: match.start()],
                orig_title[match.start() :],
            ]
            # This line names the count two digits long and changes title to my preferred format (EX: 01 - musicfile.ext)
            new_title = str(count).zfill(2) + " - " + orig_title
            # This line renames the file to my preferred format (EX: 01 - musicfile.ext)
            os.rename(filesdir + "\\" + (i), filesdir + "\\" + (new_title))
            print(" Created ", filesdir + "\\" + (new_title))
        else:
            # This line confirms that filenames without a dash are skipped over
            print(" No occurrence of a dash in", i.format(occurrence))


return_dir = create_dir_and_unzip()
dash_in_name(return_dir)
