#usr/bin/python3 

print ("-------------------------------------------")
print ("| Want to roll the dice? Enter an interger|")
print ("|         D2, D4, D6, D10, D20:           |")
#dice = int(input ("|         D2, D4, D6, D10, D20:           |"))
print ("-------------------------------------------")
dice = int(input ("ROLL: "))

from random import randrange
random = (randrange(1, dice, 1))


print ("you rolled a ", int(random), " on a D", int(dice))

