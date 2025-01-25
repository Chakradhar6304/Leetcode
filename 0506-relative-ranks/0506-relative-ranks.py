class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_scores = sorted(score, reverse=True)
        
        
        rank_map = {}
        for i in range(len(sorted_scores)):
            if i == 0:
                rank_map[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                rank_map[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                rank_map[sorted_scores[i]] = "Bronze Medal"
            else:
                rank_map[sorted_scores[i]] = str(i + 1)
        
      
        answer = []
        for s in score:
            answer.append(rank_map[s])
        
        return answer