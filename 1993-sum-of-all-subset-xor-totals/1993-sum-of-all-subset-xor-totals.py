class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_or = 0
        for v in nums:
            all_or |= v
        return all_or << (len(nums) - 1)
