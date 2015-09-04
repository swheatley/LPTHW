# Exercise 38: Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song","Frisbee","Corn","Banana", "Girl","Boy"]

# While the length of stuff does not equal 10 this loop will continue
while len(stuff) != 10:
# Assign more_stuff.pop() which removes and returns the last object from the list more_stuff and is now stored in the variable next_one.
	next_one = more_stuff.pop()
# Printing the string "Adding to the screen, indicating the last list item stored into next_one which is "Boy" will be shown.
	print "Adding: ", next_one
# Adding to the newly created list next.one from...	
	stuff.append(next_one)
# This printed statement indicates there are ___ number of items now from the length of the stuff list
	print "There are %d items now." % len(stuff)
# Prints the entire 10 item list that is stored in the variable stuff
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print " ".join(stuff) # what? cool!
print "#".join(stuff[3:5]) # super stellar!