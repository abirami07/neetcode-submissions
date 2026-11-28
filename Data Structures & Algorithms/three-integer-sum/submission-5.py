class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums[j] + nums[k] = - nums[i] --> rearrange the equation
        result = []
        #for 2 pointer technique, we need a sorted array
        nums.sort()

        for i in range(len(nums)-2):
            #avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1 #j
            right = len(nums) - 1 #k
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                elif total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result


