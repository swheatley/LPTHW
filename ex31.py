# Exercise 31: Making Decisions

# Could print out, "What Airbender adventure do you want to go on?"
def airbender_adventure():
	print "You are Ang the last Airbender. What Airbender adventure do you want to go on? Earth, Fire, Air or Water?"

	bending = raw_input("Type answer ( in lowercase ): ")

	if bending == "earth":
		earth_kingdom()
	elif bending == "fire":
		fire_nation()
	elif bending == "water":
		water_tribe()
	elif bending == "air":
		air_nation()
	else:
		air_temple()

def earth_kingdom():
	print "You need to find a master earth bender.  Who do you seek?."
	print "1. Toph from Beifong City."
	print "2. Crazy Bumi "

	earth_bender = raw_input("Type answer 1 or 2: ")

	if earth_bender == "1":
		print "You venture into the tunnels with Toph and practice bending with the badegermoles."
		print "Where do you want to go next? Air, Fire or Water?"

		next = raw_input("Type answer ( in lowercase ):")

		if next == "air":
			return air_nation()
		elif next == "fire":
			return fire_nation()
		elif next == "water":
			return water_tribe()
		else:
			return air_temple()

	elif earth_bender == "2":
		print "Bumi takes you on a crazy adventure through the city, you don't get much done but boy it was fun!"
		print "&*&*&*&*&*&*&&*&*&*&*&*&*&&*&*&*&*&*&*&"
		return air_temple()
	else:
		return airbender_adventure() 

def fire_nation():

	print "You need to learn to firebend before the Fire Lord takes over. Who do you seek?"
	print "1. Lord Zuko from Fire Nation."
	print "2. Iroh, Uncle to Lord Zuko."

	fire_bender = raw_input("Type answer 1 or 2: ")

	if fire_bender == "1":
		print "Lord Zuko helps you harness the power of fire.  You even meet real dragons!"
		print "&*&*&*&*&*&*&&*&*&*&*&*&*&&*&*&*&*&*&*&"
	elif fire_bender == "2":
		print "Iroh shows you how to redirect lighting.  This a skill only few know.  Then you sit down and enjoy some tea."
	else:
		return eairbender_adventure()

def air_nation():
	print "You were a monk at an Air temple and are a master Air bender. Learn another bending power :)"
	print "    "
	return air_temple()

def water_tribe():
	print " 1.You travel in the future and meet up with Korra of the Southern Water Tribe ."
	print " 2.You take Katara up on her water bending skills and practice your water wips!"

	water_bender = raw_input("Type answer 1 or 2: ")

	if water_bender == "1":
		print "She helps you master the art of water bending and you help her reach new heights in air bending!."
	elif water_bender == "2":
		print "You pick up water bending very quickly only after a few attempts.  Water bending is pretty easy for you!"
	else:
		return air_temple()

def air_temple():
	print "You take Apa and fly to the Air temple. You need some inspiration."
	print "Do you want to play another game?"

	game = raw_input(" yes or no: ")

	if game == "yes":
		return airbender_adventure()
	else:
		print "You don't defeat the Fire Lord and hope in the Avatar is lost....."


airbender_adventure()