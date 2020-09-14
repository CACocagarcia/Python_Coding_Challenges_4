#!/usr/bin/env python3

"""
- In this file i'll be solving 7 challenging questions using
Methods and Functions in Python
- Solving these challenges demonstrate your comprehension how methods and functions work in Python
- The complexity of the problem are gradually increasing

Note
- Questions were obtained from Pierian-Data/Complete-Python-3-Bootcamp
- All solutions are my solutions to the problem. No solutions from Pierian-Data were used
"""
# PROBLEM 1 - Write a function that computes the volume of a sphere given its radius

import math # importing math to be able to use pi

def vol(rad):
    constant = 4/3
    n = math.pi
    return constant * n * (rad**3)

print(vol(2))

# PROBLEM 2 - Write a function that checks whether a number is ina given range (inclusive of high and low)

def ran_bool(p2_num,p2_low,p2_high):
    if p2_num >= p2_low and p2_num <= p2_high:
        return True 
    else:
        return False

print(ran_bool(11,1,10))

# PROBLEM 3 - Write a Python fuction that accepts a string and calculates the number of upper case letters and lower case letters
"""
Expected output: No. of Upper case characters: n && No. of Lower case Characters: n
"""

def up_low(s):
    #placeholder variables
    count_upper = 0
    count_lower = 0

    for character_s in s:
        if character_s.isupper() == True:
            count_upper += 1
        elif character_s.islower() == True:
            count_lower += 1
        else:
            pass
    return ('No. of Upper case characters: {}\nNo. of Lower case characters: {}'.format(count_upper,count_lower))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))

# PROBLEM 4 - Write a Python Function that takes a list and return a new list with unique elements of the first

def unique_list(lst):
    #placeholder variables
    return_unique_list = []

    for each_number in lst:
        if each_number not in return_unique_list: # an operator used to check if an element is present or not
            return_unique_list.append(each_number)
        else:
            pass
    return return_unique_list

lst = [1,1,1,1,2,2,3,3,3,3,4,5,4,5,2,3,5,6,7,8]
print(unique_list(lst))

# PROBLEM 5 - Write a Python function to multiply all numbers in a list 

def mutilplication(mult_numbers):
    #placeholder varibales
    multiplied_number = 1
    
    for indv_number in mult_numbers:
        multiplied_number = multiplied_number * indv_number
    return multiplied_number

mult_numbers = [1,2,3,0,-4,-6,2]
print(mutilplication(mult_numbers))

# PROBLEM 6 - Write a Python function that checks whether a word or phrase is palindrome or not

def palindrome(is_palindrome):
    #Placeholder Variable
    is_palindrome_list = is_palindrome.split()
    is_palindrome_reversed = is_palindrome[::-1] # a method way to reverse a list - start to end and stepsize negative 1
    is_palindrome_reversed_list = is_palindrome_reversed.split() #saving it into a list to be able to compare same datatype
    
    if is_palindrome_list == is_palindrome_reversed_list:
        return True
    else:
        return False

is_palindrome = 'hello'
print(palindrome(is_palindrome))

# PROBLEM - 7 Write a Python function to check whether a string is pangram or not (Assume that the string passed does not have any punctuation)

import string # import string library to invoke the ascii table

def ispangram(str1, the_ascii):
    #placeholder variable
    comparison_string = ''
    empty_space = " "

    str1 = str1.lower() # making all characters lowecase to keep stay inside ascii table values

    for each_letter in str1:
        if each_letter not in comparison_string and each_letter != empty_space:
            comparison_string += each_letter
        else:
            pass
    #print(comparison_string)

    sorted_comparison_string = sorted(comparison_string) # this will sort the characters in alphabetical order but it will return it as a string
    a_string = "".join(sorted_comparison_string)
    #print(a_string)

    if a_string == the_ascii:
        return True
    else:
        return False
        
the_ascii = string.ascii_lowercase #ascii alphabet in lowercase
str1 = 'The quick brown fox jumps over the lazy dog'

print(ispangram(str1,the_ascii))