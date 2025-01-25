class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        memo = {}  
        def dp(i, j):
            if i == len(key):  
                return 0
            
            if (i, j) in memo:  
                return memo[(i, j)]
            
            min_steps = float('inf')
            for k in range(len(ring)):
                if ring[k] == key[i]: 
                    clock = (j - k) % len(ring)
                    anticlock = (k - j) % len(ring)
                   
                    steps = min(clock, anticlock) + 1 + dp(i + 1, k)
                    min_steps = min(min_steps, steps)
            
            memo[(i, j)] = min_steps  
            return min_steps
        
        return dp(0, 0)