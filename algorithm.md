# Algorithm Document

1. import the random module
2. intialize variable count and num_rolls to 0
3. set sum_counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
4. Function 1
* Purpose : Rolling of dice and getting the sum
* Name: roll_of_dice
* Parameters: None
* Return: None
* Algorithm:
  1. globalize count & num_rolls
  2. while count < num_rolls:
     1. roll1 = random.randint(1,6)
     2. roll2 = random.randint(1,6)
     3. roll_sum = roll2 + roll1
     4. sum_counts[roll_sum] += 1
     5. count += 1

5. Function 2
* Purpose: Main function for the program
* Name: main
* Parameters: None
* Return: None
* Algorithm:
  1. output to the user the purpose of program
  2. globalize num_rolls
  3. while True:
     1. num_rolls = ask user to input the amount of dice they want to roll
     2. if num_rolls > 0:
        1. call roll_of_dice()
        2. output to user how many dice they rolled
        3. for sum_val in the range (2,13)
            1. output the chart below (f'Sum of {sum_val}: {'*' * sum_count[sum_val]}")
            2. add a break
     3. else:
        1. num_rolls = error message, ask user to try again, enter a value to try again

6. call main()