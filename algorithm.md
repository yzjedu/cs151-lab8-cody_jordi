# Algorithm Document

1. import the random module
2. initialize variable count and num_rolls to 0
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
  3. set num_rolls to invalid input to enter loop
  4. while num_rolls <= 0
     1. ask user to input how many rolls they want, store under user
     2. if user is integer
        1. num_rolls = int(user)
        2. if num_rolls <= 0
            1. output to the user to enter a positive integer
     3. otherwise
        1. tell user they entered an invalid input and to enter a positive integer
  5. call roll_of_dice
  6. output how many times user rolled the dice
  7. output the table

6. call main()