def better_than_average(class_points, your_points):

  # Program finds if you did better than the class average on a test
  # Used the sum method to sum up the values in the array, divided by the length of the class scores array
  # If my score > avg, true, else, false
    avg = sum(class_points) / len(class_points)
    
    if your_points > avg:
        return True
    return False
