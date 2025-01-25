class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            temp = expand_around_center(i, i)
            if len(temp) > len(longest):
                longest = temp
            temp = expand_around_center(i, i + 1)
            if len(temp) > len(longest):
                longest = temp

        return longest