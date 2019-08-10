import os
import shutil
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

    # This will walk the files for
    for filename in files:
        # Read the destination from the files name
        # Agreement-civic-other_info.txt  --> Move to Agreement(dir level 1),Civic(dir level 2) directory

        # get string from first index to last instance of '-' (rfind gets last instance)
        transfer_to = filename[0:filename.rfind("-")+1]

        # convert "-" to "\"
        transfer_to = transfer_to.replace("-", "/")

        # Move file from source to destination
        # TO DO: this cannot handle subdirectories
        from_file = dirpath+filename
        to_file = to_dir+transfer_to[0]+"/"+transfer_to+timestamp+filename

        try:
            os.makedirs(to_dir+transfer_to[0]+"/"+transfer_to)
        except OSError:
            print("Diretory already exists")
        else:
            print("Directory Created")

        shutil.move(from_file, to_file)
        f.write(from_file+"|"+to_file+"\n")


f.close()
