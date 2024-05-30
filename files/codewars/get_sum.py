"""Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
"""


def get_sum(a,b):
    max = 0
    min = 0
    sum = 0
    if(a>b):
        max = a
        min = b
    elif(b>a):
        max = b
        min = a
    else:
        return a
    
    for i in range(min, max+1): #did +1 because python loops dont count last value
        sum += i
        
    return sum
    
    #good luck!
