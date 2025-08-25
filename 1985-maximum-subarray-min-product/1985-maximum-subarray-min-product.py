class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # prefix sums: pref[k] = sum(nums[:k])
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]

        # Monotonic increasing stack of indices
        st = []
        best = 0

        for i in range(n + 1):  # sentinel i == n to flush stack
            cur = nums[i] if i < n else -1  # smaller than any nums[j]
            # next smaller-or-equal found; resolve ranges
            while st and nums[st[-1]] >= cur:
                m = st.pop()
                left = st[-1] if st else -1         # previous strictly smaller
                right = i                            # next smaller-or-equal
                sub_sum = pref[right] - pref[left+1] # sum over (left+1 .. right-1)
                best = max(best, sub_sum * nums[m])
            st.append(i)

        return best % MOD
