#Exercise 16: Reading and Writing Files
# Include test.txt when you run the program
# imports the method
from sys import argv

# argument variable (argv) is storing the script and filename.
script, filename = argv

# string printed out with variable filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Asking the user for input
raw_input("?")

print "Opening the file...."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()