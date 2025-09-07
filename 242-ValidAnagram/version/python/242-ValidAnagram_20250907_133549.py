# Last updated: 9/7/2025, 1:35:49 PM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        countS = [0] * 26
        countT = [0] * 26

        for letter in s:
            countS[ord(letter) - ord('a')] += 1
        for letter in t:
            countT[ord(letter) - ord('a')] += 1
        
        return countS == countT