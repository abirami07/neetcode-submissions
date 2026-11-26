class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {} #frequency 

        #loop through each value in the list
        for i in range(len(strs)):
            current = strs[i] #need to compare the letters in each version of current
            key = tuple(sorted(current))
            """
            frequency = {}
            #loop through every character for each word 
            for j in range(len(current)):
                frequency[current[j]] = frequency.get(current[j],0)+1
            """
            if key in grouping:
                grouping[key].append(current)
            else:
                grouping[key] = [current]

        #need to return the dictionary's values, not keys.
        return list(grouping.values())

            
