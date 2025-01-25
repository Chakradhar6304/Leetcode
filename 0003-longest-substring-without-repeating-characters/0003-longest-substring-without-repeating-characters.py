class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}
        longest = 0
        start = 0  
        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            else:
                longest = max(longest, i - start + 1)
            char_index_map[char] = i

        return longest