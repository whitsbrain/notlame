import os

source_path = r"E:\Media\Music\Various Artists"


def single_file():
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
                title, audiofile = orig_title.split(".")
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


single_file()
