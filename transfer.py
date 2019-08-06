import os
import shutil
import re
import dirconfig as cfg
from pathlib import Path
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
timestamp = now.strftime("%d%m%Y%H%M%S")

# load from configuration file
# conf = {'from_dir': 'yy', 'to_dir': 'xx'}
from_dir = cfg.conf['from_dir']
to_dir = cfg.conf['to_dir']

# Open log file
f = open("transfer.log", "a+")


# This will walk the from main directory, then walk sub directories
for dirpath, dirnames, files in os.walk(from_dir):
    print(f'Found: {dirpath}')

    # This will walk the files for
    for filename in files:
        # Read the destination from the files name
        # Agreement-civic-other_info.txt  --> Move to Agreement(dir level 1),Civic(dir level 2) directory

        # regex strng before the last "-"
        transfor_to = re.search("(?s:.*)-", filename).group(0)
        # convert "-" to "\"
        transfor_to = transfor_to.replace("-", "\\")

        # Move file from source to destination
        # TO DO: this cannot handle subdirectories
        from_file = dirpath+filename
        to_file = to_dir+transfor_to[0]+"\\"+transfor_to+timestamp+filename
        print(from_file)
        print(to_file)

        try:
            os.makedirs(to_dir+transfor_to[0]+"\\"+transfor_to)
        except OSError:
            print("Diretory already exists")
        else:
            print("Directory Created")

        shutil.move(from_file, to_file)
        f.write(from_file+"|"+to_file+"\n")


f.close()
