class Solution(object):
    def length_of_last_word(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        return len(s.strip().split(' ')[-1])


length = Solution()
print(length.length_of_last_word("sdagfhajs asdfjgnkjasg ojsdfangkjsna ojsfdngjna   "))
