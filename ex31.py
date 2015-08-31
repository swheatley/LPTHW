# Exercise 31: Making Decisions

print "You are Ang the last Airbender, What bending skill would you like to learn first? Earth, Fire, Air or Water?"

bending = raw_input(">")

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
	print "You need to learn to firebend before the Fire Lord takes over. Who do you seek?"
	print "1. Lord Zuko from Fire Nation."
	print "2. Iroh, Uncle to Lord Zuko."

	fire_bender = raw_input(">")

	if fire_bender == "1":
		print "Lord Zuko helps you harness the power of fire.  You even meet real dragons!"
	elif fire_bender == "2":
		print "Iroh shows you how to redirect lighting.  This a skill only few know.  Then you sit down and enjoy some tea."

elif bending == "Air":
	print "You were a monk at an Air temple and are a master Air bender. Training complete :)"
	

elif bending == "Water":
	print " 1.You travel in the future and meet up with Korra of the Southern Water Tribe ."
	print " 2.You take Katara up on her water bending skills and practice your water wips!"

	water_bender = raw_input(">")

	if water_bender == "1":
		print "She helps you master the art of water bending and you help her reach new heights in air bending!."
	elif water_bender == "2":
		print "You pick up water bending very quickly only after a few attempts.  Water bending is pretty easy for you!"
	else:
		print "You take Apa and fly to the Air temple. You need some inspiration."

else:
	print "You don't defeat the Fire Lord and hope in the Avatar is lost....."