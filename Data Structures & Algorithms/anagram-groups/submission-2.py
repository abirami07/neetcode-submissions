class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {} #frequency 

        #loop through each value in the list
        for i in range(len(strs)):
            current = strs[i] 
            frequency = {}
            #loop through every character for each word 
            for j in range(len(current)):
                frequency[current[j]] = frequency.get(current[j],0)+1
            
            key = tuple(sorted(frequency.items()))

            if key in grouping:
                grouping[key].append(current)
            else:
                grouping[key] = [current]
        
        return list(grouping.values())
         