#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is math_program


def main():

    loop_counter = 0
    # input
    integer = input("Enter any positive number: ")

    # process & output
    try:
        number = int(integer)
        if number < 0:
            print("You did not enter a positive number")
        else:
            for loop_counter in range(number + 1):
                answer = loop_counter ** 2
                print("{0}² = {1}".format(loop_counter, answer))

    except Exception:
        print("Please follow the instructions! Use numbers")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
