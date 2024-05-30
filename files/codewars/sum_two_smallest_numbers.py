# Was super stuck until I was able to do  secSmallest = smallest in the if statement
# This was to account for if we found a smallest number towards the end of the array
# good job sticking with it!
import sys
def sum_two_smallest_numbers(numbers):
    #your code here
    smallest = sys.maxsize
    secSmallest = sys.maxsize
    
    for num in numbers:
        
        if num < smallest:
            secSmallest = smallest
            smallest = num
            
        elif num < secSmallest and num > smallest:
            secSmallest = num
            
    return smallest + secSmallest
