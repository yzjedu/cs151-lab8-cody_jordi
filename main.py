# Programmers: Cody and Jordi
# Course: CS151, Professor Zee
# Due Date: November 7th, 2024
# Lab Assignment: Lab 08
# Problem Statement: Find probability of the different sums when rolling a pair of dice
# Data In: amount of rolls
# Data Out: Sums of (2-12)
# Credits: none other than class notes

#initialize variables & import random module
import random
count = 0
sum_counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
num_rolls = 0

#Purpose: Rolling of the dice and getting the sums
#Parameters: None
#Return: None
def roll_of_dice():
    global count
    global num_rolls
    while count < num_rolls:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll2 + roll1
        sum_counts[roll_sum] += 1
        count += 1

#Purpose: Main function for the program
#Parameters: None
#Return: None
def main():
    print('This program shows the probability of the different sums when rolling a pair of dice\n')
    global num_rolls
    num_rolls = -1  # Start with an invalid number to enter the loop

    # Keep asking for a valid number of rolls until it's greater than zero
    while num_rolls <= 0:
        user_input = input("How many times do you want to roll the dice? ")
        if user_input.isdigit():  # Check if input is numeric
            num_rolls = int(user_input)
            if num_rolls <= 0:
                print("Please enter a positive integer.")
        else:
            print("Invalid input. Please enter a positive integer.")
            # Call the function to roll the dice
    roll_of_dice()
    print(f'\nRolling {num_rolls} pairs of dice:')
    for sum_val in range(2, 13):
        print(f"Sum of {sum_val}: {'*' * sum_counts[sum_val]}")

# Call main function to start the program
main()




