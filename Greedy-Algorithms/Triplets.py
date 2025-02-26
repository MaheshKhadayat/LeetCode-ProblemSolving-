# This program checks if there exists an increasing subsequence of length three in a given list of numbers.
# It uses two variables (first and second) to track the smallest and second smallest numbers found so far.
# If a third number greater than both is found, it returns True; otherwise, it returns False.
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
