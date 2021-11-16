import zipfile
import os

path = r'C:\Users\wbeeh\Downloads'

os.chdir(path)

with zipfile.ZipFile(r'C:\Users\wbeeh\Downloads\Lost+&+Forgotten+-+Volume+26.zip', 'r') as zip_ref:
    zip_ref.extractall(path)

