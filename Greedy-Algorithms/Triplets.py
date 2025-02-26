def increasingTriplet(nums):
    first = second = float('inf')

    for i in nums:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True

    return False

print(increasingTriplet([1, 2, 3, 4, 5]))  
print(increasingTriplet([5, 4, 3, 2, 1]))  
print(increasingTriplet([2, 1, 5, 0, 4, 6]))  
