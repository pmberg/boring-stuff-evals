#Brief example script to take everything in the PWD and rename it to replace hyphens with underscores

import os, shutil
from pathlib import Path
h = Path.home()

print("Got here")

print(h)

for folder_name, subfolders, filenames in os.walk(h / 'OneDrive/Documents/Summer-2025-Internship/boring-stuff-evals'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)
        # Rename file hyphens to dashes:
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.replace('-', '_'))
   
    print('')
