class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #in regular 2 sum, we used a dictionary. but here, since the array is already sorted in non decreasing order, we can solve it using two pointers. 
        left = 0
        right = len(numbers) - 1 

        while left < right: #make sure they haven't crossed yet lol
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            elif total > target:
                right -= 1
        
        