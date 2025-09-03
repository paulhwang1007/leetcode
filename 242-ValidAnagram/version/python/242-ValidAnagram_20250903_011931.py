# Last updated: 9/3/2025, 1:19:31 AM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        
        return True
        