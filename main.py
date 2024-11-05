import random
count = 0
sum_counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
num_rolls = 0


def roll_of_dice():
    global count
    global num_rolls
    while count < num_rolls:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll2 + roll1
        sum_counts[roll_sum] += 1
        count += 1


def main():
    global num_rolls
    num_rolls = int(input("How many dice do you want to roll? "))
    while num_rolls > 0:
        if num_rolls > 0:
            roll_of_dice()
            print(f'Rolling {num_rolls} pairs of dice')
            for sum_val in range(2, 13):
                print(f"Sum of {sum_val}: {'*' * sum_counts[sum_val]}")
            break

    num_rolls = int(input("Error, Try again. How many dice do you want to roll? "))

main()




