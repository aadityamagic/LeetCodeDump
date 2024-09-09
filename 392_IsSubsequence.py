"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

 

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

"""
"""
Runtime37ms
Beats47.60%
time complexity O(N+M)
"""

if __name__=="__main__":
    s="twn"
    t="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"
    
    #if all elements are not in there no bothering to check
    
    i=0
    j=0

    while j<len(s) and i<len(t) and t!='':
        while i < len(t):

            if s[j]==t[i]:
                t=t[i+1:]
                s=s[j+1:]
                break
            t=t[i+1:]
            
    
        
    if s=='':
        print(True)
    else:
        print(False)