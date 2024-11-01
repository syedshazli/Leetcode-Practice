class Solution:
    def makeFancyString(self, s: str) -> str:
        List = list(s)
        #if the current letter is equal to the previous letter and current letter is equal to next letter, remove the current letter from the lsit

        #what could be easier:
        #   making a count of consecutive characters. If the current elememnt is equal to the element we are comparing to, increment the counter. If the counter ever hits 3, remove the current letter
        letterNow = List[0]
        counter = 1
        i = 1
        resArr = [letterNow]
        while i<len(List):
            if List[i] == letterNow:
                counter+=1
            else:
                letterNow = List[i]
                counter=1

            if counter<3:
                resArr.append(List[i])
            else:
                i+=1
                continue
            
           
            i+=1
        return "".join(resArr)


        
