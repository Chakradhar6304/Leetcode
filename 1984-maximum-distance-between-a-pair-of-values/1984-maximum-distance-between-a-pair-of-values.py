class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        best = 0

        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                # valid pair (i, j); maximize distance and move j forward
                best = max(best, j - i)
                j += 1
            else:
                # need a smaller/equal nums1[i]; move i forward
                i += 1
                # keep invariant i <= j
                if i > j:
                    j = i
        return best
