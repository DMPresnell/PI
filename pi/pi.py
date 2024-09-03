from math import pi

print("This program prints pi to the specified decimal place.")
print("Specify decimal place from 1 to 15:")

while True:
    user_input = input()

    try:
        user_input = int(user_input)

        if 0 < user_input <= 15:
            break
        else:
            print("IT'S GOTTA BE A WHOLE NUMBER FROM 1 TO 15")

    except ValueError:
        print("USE WHOLE DIGITS, NOT LETTERS OR SYMBOLS!")

rounded_pi = round(pi, user_input)
print("PI:")
print(rounded_pi)