class Solution:

    def encode(self, strs: List[str]) -> str:
        """example: strs = ["hello", "world"]
        hello#world --> encoded string
        "hello", "world" --> decoded string
        """ 
        result = ""
        for i in strs: #where i is each word in the list 
            result += str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        result = [] 
        i = 0
        while i < len(s):
           #    5#hello3#dog
            j = i
            while s[j] != "#": #we use while instead of if because what if there are more than one digit to move past
                j = j + 1
            
            start = j + 1
            length = int(s[i:j])
            result.append(s[start:start+length])
            i = start + length
        
        return result

                
                
                
                
""" 
                if s[i] == "#":
                    start = i + 1
                    end = int(s[0:i])
                    word = s[start:start+end]
                    result.append(word)

                    #slice off the rest
                    s = s[start+end:]
            
        return result
        """

    
