"""Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

"""
    def row_sum_odd_numbers(n):
    #your code here
    #for x in range(1, 30, 2): jumps two every iteration
    #sum = 0
    #first number is blank % n = 1
    # 4th row has 4 numbers, 5th row has 5 numbers, etc
    
    num = 1
    total = 0
    #find the first number
    for i in range(n):
        total = total + num
        num = num + 2
    total = total * n
    return total
