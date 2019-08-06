# auto_transfer
Transfer files from a source to a destination directory based on file name structure. The script will create directories undeer the destination directory based on the characters between the delimiter "-" if it does not exist.  The files will be appended with a timestamp and moved to the destination directories.

example:
File name: under-this-directory-file1.txt
Destination: C:\under\this\directory\14022019010101under-this-directory-file1.txt

Logs: transfer.log

Configuration:
Create a configuration file called dirconfig.py.  This will store the source and destination directory.

conf = {'from_dir': 'xxx',
        'to_dir': 'yyy'}
        
from_dir - Source directory        
to_dir - Destination directory


