binarySearch(nums,target):
left = 0
right = len(nums)-1
while left < right:
    middle = (left + right)/2
    if( nums[middle] > nums[left]):
        left +=1
    elif nums[middle] < nums[right]:
        right -=1
    else:
        return nums[middle]
    
return -1
        