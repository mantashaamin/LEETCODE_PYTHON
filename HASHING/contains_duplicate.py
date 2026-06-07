'''Pattern: HashSet

Clue:
Need to know quickly if an element appeared before.

Idea:
Store seen elements in a set.

Time Complexity:
O(n)

Space Complexity:
O(n)
'''
def contains_duplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
