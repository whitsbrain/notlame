import os

source_path = r"E:\Media\Music\Various Artists"


def single_file():
    with open("dest_dirsa.txt") as read_file1:
        for rf in read_file1:
            rf = rf.rstrip("\n")
            print(rf)
            file_path = source_path + "\\" + (rf)
            files = os.listdir(file_path)
            count = 0
            for i in files:
                count = count + 1
                title, audiofile = i.split(".")
                new_title = str(count).zfill(2) + ' - ' + title + "." + audiofile
                os.rename(file_path + "\\" + (i), file_path + "\\" + (new_title))
                print(new_title)
                # hit_file.write(new_title)


single_file()
