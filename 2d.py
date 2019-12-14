#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: December 2019
# This program get's the average of all the numbers in a 2d list

import random


def calculator(dimension_list, rows, columns):
    # this finds the average of all elements in a 2d list

    total = 0
    for row_value in dimension_list:
        for single_value in row_value:
            total += single_value
    total = total/(rows*columns)

    return total


def main():
    # this function places random integers into a 2D list
    dimension_list = []

    # Input
    rows = (input("How many rows: "))
    columns = (input("How many columns: "))
    try:
        # Process
        rows = int(rows)
        columns = int(columns)
        for rows_loop in range(0, rows):
            temp_column = []
            for column_loop in range(0, columns):
                random_int = random.randint(1, 50)
                temp_column.append(random_int)

                # Output 1
                print("Random Number " + str(rows_loop + 1) + ", "
                      + str(column_loop + 1) + " is: " + str(random_int))
            dimension_list.append(temp_column)
            print("")

        # Output 2
        averaged = calculator(dimension_list, rows, columns)
        print("The average of the random numbers is: {0} ".format(averaged))

    except Exception:
        print("Please input a valid integer.")


if __name__ == "__main__":
    main()
