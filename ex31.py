# Exercise 31: Making Decisions

print "Your name is Ang and you are the Avatar.  What bending skill would you like to learn first? Earth, Fire, Wind or Water?"

beding = raw_input(">")

if bending  == "Earth":
	print "You need to find a master earth bender.  Who do you seek?."
	print "1. Toph from Beifong City."
	print "2. Crazy Bumi "

	earth_bender = raw_input(">")

	if earth_bender == "1":
		print "You venture into the tunnels with Toph and practice bending with the badegermoles."
	elif earth_bender == "2":
		print "Bumi takes you on a crazy adventure through the city, you don't get much done but boy it was fun!"
	else:
		print "You take Apa and fly to the Air temple. You need some inspiration." 

elif bending == "Fire":
	print "You need to learn to firebend before the fire lord takes over during the eclipse. Who do you seek?"
	print "1. Lord Zuko from Fire Nation."
	print "2. Iroh, Uncle to Lord Zuko."

	fire_bender = raw_input(">")

	if fire_bender == "1" or fire_bender == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif bending == "Wind":
	print "You are in a secret tunnel with strange sounds and smells....What do you do?"
	print "1. Venture deep into the tunnel."
	print "2."
	

elif bending == "Water"
	print ""
	print ""

else:
	print "You don't defeat the fire Lord and hope in the world is lost....."