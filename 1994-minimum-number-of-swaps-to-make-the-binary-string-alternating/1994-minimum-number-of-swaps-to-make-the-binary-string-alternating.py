class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        c0 = s.count('0')
        c1 = n - c0
        if abs(c0 - c1) > 1:
            return -1

        def mismatches(start_char):
            # count positions where s[i] != expected pattern starting with start_char
            mism = 0
            expected = start_char
            for ch in s:
                if ch != expected:
                    mism += 1
                expected = '1' if expected == '0' else '0'
            return mism

        if c0 == c1:
            # both patterns possible; take min swaps among them
            m0 = mismatches('0') // 2
            m1 = mismatches('1') // 2
            return min(m0, m1)
        elif c0 > c1:
            # must start with '0'
            return mismatches('0') // 2
        else:
            # must start with '1'
            return mismatches('1') // 2