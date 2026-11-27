class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we are going to use a set because a set has unique values 
        nums_set = set(nums)
        length = 0
        longest = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                length = 1
                while i + length in nums_set:
                    length = length + 1
            
            longest = max(longest, length)

        return longest