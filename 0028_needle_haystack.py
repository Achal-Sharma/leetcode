class Solution(object):
    def str_str(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


nehay = Solution()
print(nehay.str_str("aquickbrownfoxjumpedoverthequickdog", "quick"))
