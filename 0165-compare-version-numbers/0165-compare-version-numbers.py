class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_revisions = list(map(int, version1.split('.')))
        v2_revisions = list(map(int, version2.split('.')))
      
        while len(v1_revisions) < len(v2_revisions):
            v1_revisions.append(0)
        while len(v2_revisions) < len(v1_revisions):
            v2_revisions.append(0)
       
        for i in range(len(v1_revisions)):
            if v1_revisions[i] < v2_revisions[i]:
                return -1
            elif v1_revisions[i] > v2_revisions[i]:
                return 1
        
        return 0