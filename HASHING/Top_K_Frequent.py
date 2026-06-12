'''1. Build frequency dictionary

2. Convert to pairs

3. Sort by frequency

4. Take first k pairs

5. Loop through those pairs

6. Add only the number to answer

7. Return answer'''
def top_k_frequent(nums , k):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    pairs =  list(freq.items())
    sorted(pairs, key = lambda x : x[1] ,reverse = True)
    top_k = pairs[:k]
    answer = []
    for num, freq in top_k:
        answer.append(num)
    return answer
   
    
print(top_k_frequent([1 ,2,3,2,1,1 ] , 2))




