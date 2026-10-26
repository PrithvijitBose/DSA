class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        n = len(s)
        hashs = {}
        left = 0

        for i in range(n):
            if s[i] in hashs:
                # 2. Jump left pointer past the last seen position of this duplicate
                left = max(left, hashs[s[i]] + 1) # 2

            hashs[s[i]] = i ## c will be stored in index 2
            longest = max(longest, i - left + 1) # 3
        

        return longest

            



        """
        :type s: str
        :rtype: int
        """
        