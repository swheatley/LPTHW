# value of 100 is stored into the variable cars to represent the number of cars.
cars = 100
# 4 will fit in space of car
space_in_a_car = 4.0
# value of 30 is stored into the variable drivers to represent the number of drivers.
drivers = 30
# value 90 is stored into variable passengers.  Represents 90 passengers
passengers = 90
# The result of the cars(100)-drivers(30) which now equals a new variable cars_not_driven
cars_not_driven = cars - drivers
# drivers are now stored into the variable cars_driven
cars_driven = drivers
#calculation of cars_driven variable * space_in_a_car to equal new variable carpool_capacity.
carpool_capacity = cars_driven * space_in_a_car 
# passengers variable divided by the cars_driven variable to equal the average_passengers_per_car variable.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."

print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."

print "We have", passengers, "to carpool today."

print "We need to put about", average_passengers_per_car, "in each car."