class Solution(object):
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in digits:
            number = int(str(number) + str(i))
        number += 1
        return [int(x) for x in str(number)]


sol = Solution()
print(sol.plus_one([9, 9, 9, 9, 8]))
