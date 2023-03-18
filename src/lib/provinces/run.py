import os

files = os.listdir()  # list all files in current directory
file_names = []  # create an empty list to hold the file names

for file in files:
    if os.path.isfile(file):  # check if the file is actually a file (not a directory)
        name = os.path.splitext(file)[0]  # get the file name without the extension
        file_names.append(name)  # add the file name to the list

# open a file for writing and write the file names as a JavaScript array
with open('file_names.js', 'w') as f:
    f.write('const fileNames = [')
    f.write(', '.join(f"'{name}'" for name in file_names))
    f.write('];')

print('File names saved to file_names.js')  # print a message indicating where the file names were saved
