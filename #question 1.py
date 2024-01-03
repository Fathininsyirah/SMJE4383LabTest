#question 1
import math

def arithmetic (first_term, com_dif, number):
    first_term = int(print("Insert your first integer here:"))
    com_dif = int(print("Insert your second integer here:"))
    number = int (print("Insert your number here:"))
    arithmetic_sum = number / 2 * (2 * first_term + (number - 1) * com_dif)
    print ("The arithmetic sum", arithmetic_sum)
    return arithmetic_sum