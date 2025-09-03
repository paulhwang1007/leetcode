# Last updated: 9/3/2025, 1:13:35 AM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_count = [0] * 26
        t_count = [0] * 26

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            t_count[ord(t[i]) - ord('a')] += 1
        
        return s_count == t_count