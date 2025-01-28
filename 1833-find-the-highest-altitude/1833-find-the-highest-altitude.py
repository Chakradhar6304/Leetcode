class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        highest_altitude = 0
        for g in gain:
            current_altitude += g  
            highest_altitude = max(highest_altitude, current_altitude) 
        return highest_altitude