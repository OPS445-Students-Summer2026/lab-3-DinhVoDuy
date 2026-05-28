#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: dvo12 || 114641244 

import sys

def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    
    result = number1 + number2
    return result 

def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments

    result = number1 - number2
    return result

def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    
    result = number1 * number2
    return result

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))