# Exercise 29: What If

people = 20
cats = 30
dogs = 15

if people < cats:
	print 'Too many cats! The world is doomed!'

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs: 
	print "The world is drooled on!"

if people > dogs: 
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."

# 1) If-statment evaulates the variables. If they are true it will print
# if they are not true it won't print the statement.

# 2) Code under the if-statment needs to be indented to show 
# that it is part of the if-statment

# 3) If it wasn't indented the code would not run

# Changed the boolean statments

people = 100
dogs = 5
cats = 2

if people < cats:
	print "To many cats!!!"  

if people >= cats and dogs >= cats:
	print "The world is a wonderful place!"

if dogs != cats or cats != people:
	print "Obviously!"
