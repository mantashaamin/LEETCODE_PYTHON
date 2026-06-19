'''1. Create a left pointer at index 0.

2. Create a right pointer at the last index of the string.

3. While left pointer is smaller than right pointer:

    a. Compare the character at left and right.

    b. If they are not equal:
           return False

    c. Move left pointer one step forward.

    d. Move right pointer one step backward.

4. If the loop finishes without finding any mismatch:
       return True'''
def valid_palindrome(s):
    left=0
    right = len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        else:
            left+=1
            right-=1
    return True
        
print(valid_palindrome("magic"))
print(valid_palindrome("mom"))
    
    
        