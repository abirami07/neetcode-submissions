class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for i in nums:
            group[i] = group.get(i,0) + 1
        sorted_group = sorted(group, key=group.get, reverse=True)
        
        result = []
        for j in range(k):
            result.append(sorted_group[j])

        return result

#1:1
#2:2
#3:3
        