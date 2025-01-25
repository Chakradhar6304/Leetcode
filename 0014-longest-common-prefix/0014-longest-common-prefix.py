class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            temp_prefix = ""
            
            for i in range(min(len(prefix), len(string))):
                if prefix[i] == string[i]:
                    temp_prefix += prefix[i]
                else:
                    break
            prefix = temp_prefix
            if not prefix:
                break

        return prefix