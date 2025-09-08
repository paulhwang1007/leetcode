# Last updated: 9/8/2025, 10:50:27 AM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for str in strs:
            key = "".join(sorted(str))

            if key in groups:
                groups[key].append(str)
            else:
                groups[key] = [str]
        return list(groups.values())
