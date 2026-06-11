'''1. Put all numbers in a set.

2. Loop from 0 to n inclusive.

3. If a number is not in the set:
       return it.  
       '''
def missing_num(nums):
    n = len(nums)
    seen = set(nums)
    for nums in range (0,n+1):
        if nums not in seen:
            return nums
print(missing_num([0,1,2]))
    
