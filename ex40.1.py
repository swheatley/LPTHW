# Exercise 40: Modules, Classes, and Objects

mystuff ={'apple', "I AM APPLES!"}
print mystuff['apple']

#this goes in mystuff.py 
def apple():
	print "I AM APPLES!"

import mystuff
mystuff.apple()

def apple():
	print "I AM APPLES!"

# this is just a variable
tangerine = "Living reflection of a dream"

import mystuff

mystuff.apple()
print mystuff.tangerine

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable

class MyStuff(object):
	def _init_(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print "I AM CLASSY APPLES!"

# Instaniates the class MyStuff
thing = MyStuff()
thing.apple()
print thing.tangerine

# dict style
mystuff['apples']

#module style
mystuff.apples()
print mystuff.tangerine

#class style
thing = MyStuff()
thing.apples()
print thing.tangerine
