class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][0:i]
        return strs[0]


sol = Solution()
print(sol.longest_common_prefix(["abcd", "abcde", "ab"]))
