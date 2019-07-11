import os
import time
import zipfile

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = [r'C:\Users\gachamnos\Dropbox (Persado Operations)\Tools', r'C:\Users\gachamnos\Dropbox (Persado Operations)\Personal']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = 'C:\Temp'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# 5. Take a comment from the user to
# create the name of the zip file
comment = raw_input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

# 6. Create the zip file
print('Creating {}...'.format(target))
zFile = zipfile.ZipFile(target, 'w')

# Compress and zip up each folder and its contents
for folder in source:
    for root, dirs, files in os.walk(folder):
        print('Adding files in {}...'.format(root))
        zFile.write(root)
        for file in files:
            zFile.write(os.path.join(root, file), compress_type=zipfile.ZIP_DEFLATED)

zFile.close()
print('\nBackup successful in {}!'.format(target))



