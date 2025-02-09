from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        substring_len = word_len * word_count
        word_map = Counter(words)
        result = []

        for i in range(word_len):
            left, right = i, i
            current_map = Counter()
            word_used = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_map:
                    current_map[word] += 1
                    word_used += 1

                    while current_map[word] > word_map[word]:  
                        current_map[s[left:left + word_len]] -= 1
                        word_used -= 1
                        left += word_len

                    if word_used == word_count:  
                        result.append(left)
                
                else:
                    current_map.clear()
                    word_used = 0
                    left = right 

        return result

        