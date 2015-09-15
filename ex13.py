# Exercise 13: Parameters, Unpacking, Variables
# Remember to include three variables before you run it
from sys import argv

argv =  raw_input("Give me a movie name: ")
movie = argv

argv =  raw_input("What is your favorite color?: ")
color = argv

argv = raw_input("Are you a cat or dog person?: ")
animal = argv

argv = int(raw_input("How old are you?: "))
age = argv





print "The movie is:", movie
print "Favorite color:", color
print "You are a %s person" % animal
print "You are %d years old" % age