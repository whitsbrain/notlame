import os

os.chdir(r'M:\Temp')
wd = (os.getcwd())

directories = os.walk(wd)
dirpath, dirnames, filenames = next(directories)
print("Directory Path:", dirpath)
print("Directory Names:", dirnames)
with open ('zipnames.txt', 'w') as output_file:
    for f in filenames:
        print(f, file=output_file)
