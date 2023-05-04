class Solution(object):
    def find_difference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]


sol = Solution()
print(sol.find_difference([1, 2, 3, 3], [2, 2, 4, 6]))
