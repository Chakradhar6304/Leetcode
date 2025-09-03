class Solution(object):
    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        if not nums:
            return 0

        M = max(nums)
        freq = [0] * (M + 1)
        for v in nums:
            freq[v] += 1

        # prefix sums of frequencies: pref[i] = count of numbers <= i
        pref = [0] * (M + 1)
        for i in range(1, M + 1):
            pref[i] = pref[i - 1] + freq[i]

        def count_in(l, r):
            if l > r: 
                return 0
            if l <= 0:
                return pref[min(r, M)]
            return pref[min(r, M)] - pref[l - 1]

        ans = 0
        # For each possible x, add contributions of floor(y/x) for all y.
        for x in range(1, M + 1):
            fx = freq[x]
            if fx == 0:
                continue
            k = 1
            # y in [k*x, (k+1)*x - 1] contributes k
            while k * x <= M:
                l = k * x
                r = min((k + 1) * x - 1, M)
                cnt = count_in(l, r)
                if cnt:
                    ans = (ans + fx * cnt * k) % MOD
                k += 1

        return ans % MOD
