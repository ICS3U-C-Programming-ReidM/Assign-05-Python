#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program uses a function to calculate the midpoint of a line segment with user input
# Function to repeatedly prompt for valid numeric input


def get_valid_number(prompt):
    while True:
        try:
            # Try to convert user input to a float
            return float(input(prompt))
        except ValueError:
            # If conversion fails, inform the user and repeat
            print("Invalid input. Please enter a valid number.")


# Function to calculate the midpoint between two points
def calculate_midpoint(x1, y1, x2, y2):
    # Calculate the x-coordinate of the midpoint
    mid_x = (x1 + x2) / 2
    # Calculate the y-coordinate of the midpoint
    mid_y = (y1 + y2) / 2
    # Return the result as a tuple (x, y)
    return (mid_x, mid_y)


# Main function that controls the program
def main():
    # Greet the user with a description of what the program does
    print(
        "Hello, today this program shall calculate and find the midpoint between two points"
    )
    print("using the formula: M(x1 + x2 / 2, y1 + y2 / 2)")

    # Prompt the user for coordinates, using get_valid_number to validate input
    x1 = get_valid_number("Enter x1: ")
    y1 = get_valid_number("Enter y1: ")
    x2 = get_valid_number("Enter x2: ")
    y2 = get_valid_number("Enter y2: ")

    # Call the function to compute the midpoint
    midpoint = calculate_midpoint(x1, y1, x2, y2)

    # Display the final result to the user
    print(f"The midpoint is: ({midpoint[0]}, {midpoint[1]})")


# Call the main function to start the program
main()
