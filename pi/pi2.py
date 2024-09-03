from math import pi

def process_input(user_input):
    """
    Take user input string and make sure it is an integer 1-15.
    If it is, return pi rounded.  If not, print error message for
    user and return False.
    """
    try:
        i = int(user_input)
        if 0 < i <= 15:
            pi_rounded = round(pi, i)
            return rounded_pi
        else:
            raise Exception
    except:
        print("Whole numbers from 1 to 15 only!")
        return False

print("This program prints pi to the specified decimal place.")
print("Specify decimal place from 1 to 15:")

pi_rounded = False

while not pi_rounded:
    user_input = input()
    pi_rounded = process_input(user_input)