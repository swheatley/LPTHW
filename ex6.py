# variable with the value of a string 
x = "There are %d types of people." % 10
# binary variable stores the value of the string "binary" variable
binary = "binary"
# do_not variable stores the value of the string "dont"
do_not = "don't"
# y variable stores the value of the string as well as the binary and do_not variables.
y = "Those who know %s and those who %s." %(binary, do_not)

# variable x is printed out
print x 
# variable y is printed out
print y

# string that includes variable x is printed out
print "I said: %r." % x
# string that includes variable y is printed out
print "I also said: '%s' " % y
# the variable hilarious is given the value of false
hilarious = False
# the variable of joke_evaluation is given the value of the string, "Isn't that joke so funny?!"
joke_evaluation = "Isn't that joke so funny?! %r"

# the variable joke_evaluation and hilarious are printed out
print joke_evaluation % hilarious

# the variable w is given the string value of "This is the left side of..."
w = "This is the left side of..."
# the variable e is given the string value of "a string with a right side."
e = "a string with a right side."

# the variable w and e are concatenated together as strings
print w + e

