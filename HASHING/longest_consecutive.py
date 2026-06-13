'''1. Put all numbers in a set

2. For each number

3. If num-1 is NOT present
      this is a start

4. From this start,
      keep checking next numbers

5. Count the length

6. Keep track of the maximum length'''
def longest_consecutive(nums):
      longest = 0 
      current_nums = set(nums)
      for i in current_nums:
            if i-1 not in current_nums:
                  current = i
                  count = 1
            while current + 1 in current_nums:
                  current+=1
                  count+=1
            longest = max(longest, count)
            return longest 
print(longest_consecutive([100,4,200,1,3,2]))
                  
                  
                  
                  