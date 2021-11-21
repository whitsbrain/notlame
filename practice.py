import os

# os.chdir(r'E:\Temp')

# print(os.listdir())
# print(dir(os))
print(os.getcwd())
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)
