import zipfile
import os

source_path = os.path.join(os.environ.get("HOME"), "Downloads")
dest_path = r"E:\Media\Music\Various Artists"

with open("source_zips.txt") as read_file1:
    with open("dest_dirs.txt") as read_file2:
        for sz, dd in zip(read_file1, read_file2):
            sz = sz.rstrip("\n")
            dd = dd.rstrip("\n")
            with zipfile.ZipFile(source_path + "\\" + (sz), "r") as zip_ref:
                zip_ref.extractall(dest_path + "\\" + (dd))
