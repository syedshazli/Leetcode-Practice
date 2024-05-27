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
