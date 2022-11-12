import zipfile
import os

def temp_dir():
    source_path = r"M:\Temp"
    dest_path = r"M:\Music\Various Artists"

    with open("source_zips.txt") as read_file1:
        with open("dest_dirs.txt") as read_file2:
            for sz, dd in zip(read_file1, read_file2):
                sz = sz.rstrip("\n")
                dd = dd.rstrip("\n")
                with zipfile.ZipFile(source_path + "\\" + (sz), "r") as zip_ref:
                    zip_ref.extractall(dest_path + "\\" + (dd))


def downloads_dir():
    source_path = os.path.join(os.environ.get("HOME"), "Downloads")
    dest_path = r"M:\Temp"

    with open("source_zips.txt") as read_file1:
        with open("dest_dirs.txt") as read_file2:
            for sz, dd in zip(read_file1, read_file2):
                sz = sz.rstrip("\n")
                dd = dd.rstrip("\n")
                print(dd)
                with zipfile.ZipFile(source_path + "\\" + (sz), "r") as zip_ref:
                    zip_ref.extractall(dest_path + "\\" + (dd))


def artists_dir():
    path = r"M:\Temp"
    dotz = ".z"
    with open("source_zipsa.txt") as read_file1:
        for sz in read_file1:
            sz = sz.rstrip("\n")
            with zipfile.ZipFile(path + "\\" + (sz), "r") as zip_ref:
                index = sz.rfind(dotz)
                splitat = index
                dirname = sz[:splitat]
                finaldir = (path + "\\" + dirname)
                os.mkdir(finaldir)
                zip_ref.extractall(finaldir)
                print("Files have been unzipped to directory:", finaldir)

artists_dir()
