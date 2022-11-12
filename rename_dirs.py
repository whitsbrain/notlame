import os
import string

basedir = 'M:/Temp'
dash = "-"

for fn in os.listdir(basedir):
  print(basedir, fn)
  if not os.path.isdir(os.path.join(basedir, fn)):
    print('not a dir')
    # continue # Not a directory
  else:
    index = fn.rfind(dash)
    splitat = index
    artist, orig_title = fn[:splitat], fn[splitat:]
    # artist_mod = artist.rstrip("\n")
    artist_low = string.capwords(artist)
    os.rename(os.path.join(basedir, fn),
            os.path.join(basedir, artist_low + " " + orig_title))
