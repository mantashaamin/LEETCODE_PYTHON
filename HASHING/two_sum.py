'''Pattern: HashMap

Clue:
Need to quickly find a complement.

Idea:
Store number -> index in a dictionary.

For each number:
    need = target - num

If need already exists:
    return indices

Else:
    store current number and index

Time Complexity:
O(n)

Space Complexity:
O(n)
'''

def two_sum(nums , target):
    seen = {}
    for index, num in enumerate(nums):
        need = target-num
        if need in seen:
            return [seen[need] , index]
        seen[num] = index 
print(two_sum([2,7,11,15], 9))      # [0,1]

print(two_sum([3,2,4], 6))          # [1,2]

print(two_sum([3,3], 6))            # [0,1]

print(two_sum([1,5,3,7], 8))        # [0,3] or [1,2]

print(two_sum([5,8,3], 11))         # [1,2]
    
