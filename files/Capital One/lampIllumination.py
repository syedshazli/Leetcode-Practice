def solution(lamps, points):
    returnArr = [0]*len(points)
    for k in range(len(points)):
        for i in range(len(lamps)):
            startBound = lamps[i][0]
            endBound = lamps[i][1]
            if startBound<=points[k]<=endBound:
                returnArr[k]+=1
    return returnArr
