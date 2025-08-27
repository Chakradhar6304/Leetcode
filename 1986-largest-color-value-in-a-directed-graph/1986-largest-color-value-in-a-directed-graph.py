from collections import defaultdict, deque

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        
        # Build adjacency list and indegree
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Initialize color counts: count[node][c] = max freq of color c on path ending at node
        count = [[0]*26 for _ in range(n)]
        
        # Queue for topological sort
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        visited = 0
        res = 0
        
        while q:
            u = q.popleft()
            visited += 1
            
            # Update current node’s color count
            c_idx = ord(colors[u]) - ord('a')
            count[u][c_idx] += 1
            res = max(res, count[u][c_idx])
            
            # Propagate to neighbors
            for v in graph[u]:
                for c in range(26):
                    count[v][c] = max(count[v][c], count[u][c])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        # If not all nodes visited => cycle
        if visited < n:
            return -1
        
        return res
