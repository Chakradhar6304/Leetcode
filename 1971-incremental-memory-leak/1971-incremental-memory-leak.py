class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        t = 1
        m1, m2 = memory1, memory2
        while True:
            if m1 >= m2:
                if m1 >= t:
                    m1 -= t
                else:
                    return [t, m1, m2]
            else:
                if m2 >= t:
                    m2 -= t
                else:
                    return [t, m1, m2]
            t += 1