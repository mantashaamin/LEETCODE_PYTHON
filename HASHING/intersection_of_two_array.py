'''1. Convert nums1 into a set.

2. Create an empty result set.

3. Loop through nums2.

4. If current number exists in nums1 set:
       add it to result set.

5. Convert result set to list and return it.'''
def intersection_of_two_array(nums1 , nums2):
    nums1 = set(nums1)
    result = set()
    for i in nums2:
        if i in nums1:
            result.add(i)
    return list(result)
print(intersection_of_two_array([ 1 , 2 , 2 ,1] , [2 , 2]))
            
 