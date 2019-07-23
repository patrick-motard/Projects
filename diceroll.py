#usr/bin/python3
# imports typically go at the top of a file
import sys
import random

print (
    '''
    -------------------------------------------
    | Want to roll the dice? Enter one of the |
    |    following: D2, D4, D6, D10, D20      |
    -------------------------------------------
    '''
)

valid_inputs = ['D2', 'D4', 'D6', 'D10', 'D20']
# By upper-casing the user input, it allows the user to put lowercase,
# which is easier to type.
user_input = input('ROLL: ').upper()

# Validate the user input, ensuring that it is one of the options above.
if any(user_input == i for i in valid_inputs) == False:
    print ('You entered an invalid option.')
    # exit with code 1, signaling an error, 0 is success
    sys.exit(1)

# user_input is a string.
# Strings are a sequence of characters.
# You can select a sub sequence using an index.
# user_intput[1] takes the entire string starting with index 1.
# Note that all sequences (arrays) start with index value 0.
# So user_input[0] is always 'D'.
dice_int = int(user_input[1])


random = random.randint(1, dice_int)

print (f'You rolled a {random}, on a D{dice_int}')


# 'random' is already an int
# 'dice' is a string with non integer characters
# it can't be cast to an int. Python doesn't know what to do
# with the non int string characters during the cast.
# print ('you rolled a ', int(random), ' on a D', int(dice))

