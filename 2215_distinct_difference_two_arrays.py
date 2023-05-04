class Solution(object):
    def find_difference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # // My first approach
        # list1 = set(nums1)
        # list2 = set(nums2)
        # for item in nums1:
        #     if item in list2:
        #         list2.remove(item)
        # for item in nums2:
        #     if item in list1:
        #         list1.remove(item)
        # return [list1, list2]
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]


sol = Solution()
print(sol.find_difference([1, 2, 3, 3], [2, 2, 4, 6]))
