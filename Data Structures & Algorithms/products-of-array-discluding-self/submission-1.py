"""bruteforce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #categorize into left and right. prefix and suffix technique. 
        #example: input = [1,2,3,4]. output = [48,24,12,8]
        prefix = 1
        result = [1] * len(nums) # [1,1,1,1] or however long nums is 
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) -1 , -1, -1): #range(start, stop, step)
            result[i] *= suffix
            suffix *= nums[i]
    
        return result
