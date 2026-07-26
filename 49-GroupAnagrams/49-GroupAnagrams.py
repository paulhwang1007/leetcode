# Last updated: 7/26/2026, 3:53:36 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for string in strs:
            sorted_list = sorted(string)
            sorted_string = "".join(sorted_list)

            if sorted_string in hash:
                hash[sorted_string].append(string)
            else:
                hash[sorted_string] = [string]
                
        return list(hash.values())