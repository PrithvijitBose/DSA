class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        n = len(s)
        max_freq = 0
        hashs = {}
        longest = 0

        for i in range(n):
            char = s[i]
            hashs[char] = hashs.get(char,0)+1 # A:3 B:3
            max_freq = max(max_freq, hashs[char]) # 3

            if (i-left+1) - max_freq >k: #   B A B B
                hashs[s[left]] -= 1 # 6-2+1=
                left +=1
            longest = max(longest, i-left+1) # 1

        return longest


         

        
        
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        