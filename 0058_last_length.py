class Solution(object):
    def length_of_last_word(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        split_list = s.split(' ')
        i = 1
        while len(split_list[-i]) == 0:
            i += 1
        return len(split_list[-i])


length = Solution()
print(length.length_of_last_word("sdagfhajs asdfjgnkjasg ojsdfangkjsna ojsfdngjna   "))
