class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i, j = 0, 0
        
        # Merge characters alternately
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        
        # Append remaining characters of the longer string
        if i < len(word1):
            merged.append(word1[i:])
        if j < len(word2):
            merged.append(word2[j:])
        
        return ''.join(merged)
        