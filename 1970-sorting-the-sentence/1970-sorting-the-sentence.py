class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        n = len(words)
        result = [""] * n

        for w in words:
            pos = int(w[-1]) - 1   # last char is the index
            result[pos] = w[:-1]  # store word without index

        return " ".join(result)
