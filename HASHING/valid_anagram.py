
'''def valid_anagram(s, t):
    # length check

    # create count_s and count_t

    # build count_s

    # build count_t

    # compare dictionaries
    

    '''
def valid_anagram(s,t):
    if len(s)!=len(t):
        return False
    count_s = {}
    count_t = {}
    for char in s :
        if char in count_s:
            count_s[char]+=1
        else : count_s[char]=1
    for char in t :
        if char in count_t:
            count_t[char]+=1
        else:
            count_t[char] = 1
    return count_t==count_s
print(valid_anagram("anagram", "nagaram"))   # True
print(valid_anagram("rat", "car"))           # False
print(valid_anagram("listen", "silent"))     # True
print(valid_anagram("hello", "world"))       # False
print(valid_anagram("", ""))                 # True
print(valid_anagram("a", "a"))               # True
print(valid_anagram("ab", "a"))              # False
print(valid_anagram("aa", "bb"))             # False
            
        