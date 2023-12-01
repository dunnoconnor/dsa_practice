#Assignment
#Write a function, sumNums, that takes a number, num, as an argument and returns the sum of 
#all the numbers between 1 and num. You can assume that num will be greater than 1. Use recursion.
# example: 
#sumNums(3); // => 6 (3 + 2 + 1)


# 1.) Summary of the problem in my own words
'''
Write a recursive function, sumNums, that takes a positive integer num as an argument and 
returns the sum of all the positive integers from 1 to num.
'''
# 2.) Write test cases for example inputs and outputs

sumNums(5)  # Output: 15

# 3.) Pseudocode your plan in comments

# sumNums() this is the function 

# sumNums(2) input is 2, which will recursively 

# actually, I should set a variable as 'nums', which will allow me to change the input,
#  but the function will still work for any numbered input.


# 4.) Commit your code as you go until you solution is complete

num = 25

def sumNums(num):
    if num == 1:
        print(1)
    else:
      num == 1:
        print(num + sumNums(num - 1))