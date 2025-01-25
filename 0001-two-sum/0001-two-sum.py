class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hash table to store the numbers and their indices
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement exists in the hash table
            if complement in num_map:
                # If it does, return the current index and the index of the complement
                return [num_map[complement], i]
            
            # Add the current number and its index to the hash table
            num_map[num] = i
        
        # In case there is no solution (though the problem statement guarantees one)
        return []
