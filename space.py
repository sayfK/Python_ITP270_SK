#!/bin/python3

#Introduction
print("I have information for the following planets:\n")

#Planet List
print("1. Venus 2. Mars 3. Jupiter")
print("4. Saturn 5. Uranus 6. Neptune\n")

#Variables
weight = int(input("What is your weight?"))
planet = int(input("What planet is your match on?"))

#If else statement
if planet == 1:
	weight = weight * 0.91
elif planet == 2:
	weight = weight * 0.38
elif planet == 3:
	weight = weight * 2.34
elif planet == 4:
	weight = weight * 1.06
elif planet == 5:
	weight = weight * 0.92
elif planet == 6:
	weight = weight * 1.19

#Output
print("Your weight is:", weight)
