# Exercise 13: Parameters, Unpacking, Variables
# Remember to include three variables before you run it
from sys import argv 

script,userName = argv

prompt = " ---> "

print " %s what is your favorite Judd Apatow movie?" % userName
movie = raw_input(prompt)

if movie == "this is 40" or "knocked up":
	print "It's classic!!!"
elif movie == "the neighbors":
	print "Growing up man!!!"
else:
	print "Life is about growing and learning"

print " %s are you a cat or a dog person?" % userName
animal = raw_input(prompt)

if animal == 'dog':
	print "Dogs are awesome!!! Ceasar Millan would be proud"
else:
	print "I'm not helping you remove cat pee from your clothes!"

print "%s are you a male or female?" % userName
gender = raw_input(prompt)

print "What month is your birthday in?"
birthday = raw_input(prompt)

print "Here is your story.."

print """

      """ % ()




