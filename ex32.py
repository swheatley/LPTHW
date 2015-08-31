# Exercise 32: Loops and Lists

# Lists are similar to Arrays

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty oranges
elements = []

#then use the range function to do 0 to 5 counts
for i in range (0, 6): # range() is a built in python funciton.  Used in for loops. Must be integers
	print "Adding %d to the list" % i
	#append is a function that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Element was: %d" % i

# Lists:
# most versatile datatype available
# Built-in List Functions & Methods:
		# List Functions
	# 1. cmp(list1, list2) - compares elements of both lists
	# 2. len(list) - gives the total length of the list
	# 3. max(list) - returns item from the list with max value
	# 4. min(list) - returns item from the list with min value
	# 5. list(seq)- converts a tuple into a list
		# List Methods
	# 1. list.append()- appends or adds object to list
	# 2. list.count()- returns count of how many times object occurs in list
	# 3. list.extend(seq) - appends the contents of seq to list
	# 4. list.index() - returns the lowest index in list that obj appears
	# 5. list.insert(index, obj) - inserts object obj into list at offset index
	# 6. list.pop(obj=list[-1])-removes and returns last object or obj from list
	# 7. list.remove(obj)- removes object obj from list
	# 8. list.reverse()- reverses objects of list in place
	# 9. list.sort([func]) - sorts objects of list, use compare func if given