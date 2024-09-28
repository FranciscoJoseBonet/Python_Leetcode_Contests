'''
MINIMUM ELEMENT AFTER REPLACEMENT WITH DIGIT SUM

You are given an integer array nums.
You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements.
'''




class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for n in nums:
            
            # Calculation of the sum of the digits
            sum_dig = sum(int(dig) for dig in str(n))
            arr.append(sum_dig)

        return min(arr) # Returns the min value of the digit sum