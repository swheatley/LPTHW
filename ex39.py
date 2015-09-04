# Exercise 39: Dictionaries, Oh Lovely Dictionaries

stuff = {'name': 'Zed', 'age': 39, 'height': 6*12+2}
print stuff['name']
# Zed Shaw
print stuff['age']
# 39
print stuff['height']
# 6 foot 1 or 74 inches
stuff['city']= "San Francisco"
print stuff['city']
# San Francisco

stuff[1]="Wow"
stuff[2]= "Neato"
print stuff[1]
# Wow
print stuff[2]
# Neato
stuff
# {'city': "San Francisco", 2: "Neato", 1: 'Wow'....}

del stuff['city']
# removes San Francisco from the Dictionary

del stuff[1]
# removes the string "Wow"

del stuff[2]
# removes the string "Neato"

stuff
# prints out the original dictionary you had before.

# Real Exercise

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'

}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR']= 'Portland'

#print out some cities
print "_" * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print out some states
print "_" * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dictionary
print "_" * 10
print 'Michigan has: ', cities[states['Michigan']]
print 'Florida has: ', cities[states['Florida']]

#print every state abbreviation
print "_" * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" %(state,abbrev)

#print every city in state
print "_" * 10
for abbrev, city in cities.items():
	print "%s has the city %s" %(abbrev, city)

# now do both at the same time
print "_" * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])

print '_' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX is: %s" % city