'''approach 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        curr_len = 0
        max_substr = ""
        length = len(s)
        
        if length == 0:
            return ""
        
        if length == 1:
            return s[0]

        elif length == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        for c in range(1, length):
            i, j = c - 1, c
            # if the middle two elements are the same
            if s[i] == s[j]:
                curr_len = 2
                j = j + 1
                # move j right until different
                while j < length:
                    if s[i] == s[j]:
                        curr_len = curr_len + 1
                        j = j + 1
                    else:
                        j = j - 1
                        break
                if j == length:
                    j = j - 1
                
                # move i left until different
                i = i - 1
                while i >= 0:
                    if s[i] == s[j]:
                        curr_len = curr_len + 1
                        i = i - 1
                    else:
                        i = i + 1
                        break
                if i < 0:
                    i = i + 1 


                # if we reached the end of the string
                if i == 0 or j == length - 1:
                    if curr_len > max_len:
                        max_substr = s[i:i + curr_len]
                        max_len = curr_len
                        curr_len = 0
                        continue

                # otherwise, see if palindrome extends beyond the identical elements
                else:
                    i, j = i - 1, j + 1
                    while i >= 0 and j < length:
                        if s[i] == s[j]:
                            i, j = i - 1, j + 1
                            curr_len = curr_len + 2
                        else:
                            i = i + 1
                            j = j - 1
                            break
                    if i < 0:
                        i += 1
                
                if curr_len > max_len:
                    max_substr = s[i:i + curr_len]
                    max_len = curr_len
                    curr_len = 0
                else:
                    curr_len = 0
                            



            # otherwise, middle element is unique (e.g. cowoc)
            else:
                j = j + 1
            
                curr_len = 1
                while i >= 0 and j < length:
                    if s[i] == s[j]:
                        curr_len += 2
                        i, j = i - 1, j + 1
                    else:
                        break
                # reset indices to where s[i] == s[j] last
                i = i + 1
                if curr_len > max_len:
                    max_substr = s[i:i + curr_len]
                    max_len = curr_len
                    curr_len = 0
                else:
                    curr_len = 0
        
        return max_substr
                    
                    
            
'''       




# Dynamic programming aproach
#
#
import numpy as np
s = "aabacdddc"
max_str = ""
length = len(s)
x = np.identity(length)


if length == 0:
    print("")

if length == 1:
    print(s[0])

if length == 2:
    if s[0] == s[1]:
        print(s)
    else: 
        prin(s[0])

# check P(i,i + 1) for palindromes of length 2
for i in range(length - 1):
    if s[i] == s[i + 1]:
        x[i, i + 1] = 1

# check for palindromes of length >= 3
for j in range(2, length):
    for i in range(length - j):
        if x[i + 1, i + j - 1] and s[i] == s[i + j]:
            x[i, i + j] = 1
            max_str = s[i:i + j + 1]





