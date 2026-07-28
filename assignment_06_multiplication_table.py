# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_multiplication_table(number):
    """Part A: Print the multiplication table for a single number, 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


def print_tables_up_to_n(n):
    """Part B: Print multiplication tables for every number from 1 to N."""
    for number in range(1, n + 1):
        print_multiplication_table(number)
        if number != n:
            print("-" * 20)


def main():
    # PART A
    num_input = input("Enter a number: ")
    if not num_input.strip().lstrip("-").isdigit() or int(num_input) <= 0:
        print("Error: please enter a positive integer.")
        return
    print_multiplication_table(int(num_input))

    print()

    # PART B
    n_input = input("Enter a number N: ")
    if not n_input.strip().isdigit() or int(n_input) <= 0:
        print("Error: N must be a positive integer.")
        return
    print_tables_up_to_n(int(n_input))


main()
