class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(boxGrid), len(boxGrid[0])

        # 1) Simulate gravity in the original orientation:
        # stones '#' slide right until blocked by '*' or another stone.
        for i in range(m):
            write = n - 1  # next free spot to drop a stone to the right
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    write = j - 1                 # reset window to left of obstacle
                elif boxGrid[i][j] == '#':
                    # move stone to 'write' position
                    boxGrid[i][j] = '.'
                    boxGrid[i][write] = '#'
                    write -= 1
                # if '.', do nothing

        # 2) Rotate 90 degrees clockwise
        res = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]
        return res
