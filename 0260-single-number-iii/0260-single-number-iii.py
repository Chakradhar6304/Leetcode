class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        
        rightmost_set_bit = xor & -xor
        
        
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num 
            else:
                num2 ^= num 
        
        return [num1, num2]

# Example usage:
sol = Solution()
print(sol.singleNumber([1,2,1,3,2,5])) 
print(sol.singleNumber([-1,0]))        
print(sol.singleNumber([0,1]))      