class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for i in range(len(nums)):
            if nums[i] in check:
                return True
            check.add(nums[i])
        return False
        
        
        """for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False"""