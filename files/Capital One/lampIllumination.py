#basically find if a number exists within multiple ranges of a 2d array of column length 2, representing start and end poitns of a lamp, inclusive. 
# add how many times this number is seen to an array, and return it, the numbers you want to find are given as an input points
def solution(lamps, points):
    returnArr = [0]*len(points)
    for k in range(len(points)):
        for i in range(len(lamps)):
            startBound = lamps[i][0]
            endBound = lamps[i][1]
            if startBound<=points[k]<=endBound:
                returnArr[k]+=1
    return returnArr
