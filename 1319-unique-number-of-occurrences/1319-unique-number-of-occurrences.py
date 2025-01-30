class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = Counter(arr)
        occurrences = set(freq.values())
        return len(occurrences) == len(freq)