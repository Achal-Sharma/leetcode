class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            xreversed = -int(str(-x)[::-1])
            if xreversed < pow(-2, 31):
                return 0
            else:
                return xreversed
        else:
            xreversed = int(str(x)[::-1])
            if xreversed > pow(2, 31) - 1:
                return 0
            else:
                return xreversed


sol = Solution()
print(sol.reverse(-1234))
