# Exercise 30: Else and If

# numbers are assigned variable values
people = 30
cars = 40
trucks = 15

# if cars is greater than people it will print "We should take the cars" if its not
# it will print "We can't decide".
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide"

# if the trucks are greater than the cars it will evaluate and print the statment
# That's too many trucks.  If trucks are less than cars it will evaluate and print the statment
# "Maybe we could take the trucks."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide"

# if people are greater than trucks the program will evaluate and print the statment, "Alright 
# let's just take the trucks." if people are less than trucks the module will print out and evaluate
# the statement "Fine let's just stay home then."


if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."