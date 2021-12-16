#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Dec , 2021
# This program gets the user to enter a number.
# It will also tell if the number is positive, negative or zero.


def main():
    # this function checks the user's number

    # input
    user_number = int(input("Enter any number: "))
    print("")

    # check number size
    if user_number > 0:
        print("{} is positive.". format(user_number))

    elif user_number < 0:
        print("{} is negative.". format(user_number))

    else:
        print("{} is zero.". format(user_number))


if __name__ == "__main__":
    main()