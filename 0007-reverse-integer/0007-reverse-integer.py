class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = 0
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10

        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0
        else:
            return sign * reversed_x