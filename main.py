import random


result_list = []

def dice_roll():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2
    return roll_sum

count = 0
plays = input('Enter how many times you want to roll: ')
plays = int(plays)
while count < plays:
    roll_sum = dice_roll()
    result_list[roll_sum] += 1
    print(result_list)

count += 1





