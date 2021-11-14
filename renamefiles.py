import sys
import requests

print(sys.version)
print(sys.path)
print(sys.executable)
r = requests.get("https://wordpress.com")
print(r.status_code)

# count = 0
# dash = "-"
# with open("nlfiles25.txt", "r") as read_file:
#     with open("renamed_nlfiles25.txt", "w") as hit_file:
#         for i in read_file:
#             count = count + 1
#             index = i.rfind(dash)
#             splitat = index
#             artist, orig_title = i[:splitat], i[splitat:]
#             title, mp3 = orig_title.split(".")
#             if title[0] != " ":
#                 title = " " + title
#             if title[-1] == " ":
#                 title = title.rstrip(title[-1])
#             if title[2] != " ":
#                 title = title[0:2] + ' ' + title[2:]
#             new_title = str(count).zfill(2) + title + "." + mp3
#             hit_file.write(new_title)
# def insert_space(string, integer):
#     return string[0:integer] + ' ' + string[integer:]
