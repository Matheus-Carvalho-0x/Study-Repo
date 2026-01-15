"""
In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
# To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")
# The code above is the same as:
f = open("demofile.txt", "rt")

# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt")
print(f.read())

# Note: You should always close your files. In some cases, due to buffering, changes made to a file may
# not show until you close the file.

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
with open("demofile.txt") as f:
    print(f.read(5))
# You can return one line by using the readline() method.
# By looping through the lines of the file, you can read the whole file, line by line:
with open("demofile.txt") as f:
    for x in f:
        print(x)

# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
# os.remove("demofile.txt")
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
# To delete an entire folder, use the os.rmdir() method.
# Note: You can only remove empty folders.
