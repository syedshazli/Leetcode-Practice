class Solution:
    def minChanges(self, s: str) -> int:
        currentSubLen = 1
        listStr = list(s)
        countFlips = 0
        i = 1
        while i < len(listStr):
            # check if current Letter is equal to previois
            if listStr[i] == listStr[i-1]:
                currentSubLen+=1
                i+=1
                continue
            elif currentSubLen%2 == 0:
                currentSubLen = 1
                i+=1
            else:
                if listStr[i] == "0":
                    listStr[i] == "1"
                    countFlips+=1
                    i+=1
                    currentSubLen+=1
                    continue
                elif listStr[i] == "1":
                    listStr[i] == "0"
                    countFlips+=1
                    i+=1
                    currentSubLen+=1
                    continue
            # previous element is not equal, and our substring length is not even
        return countFlips
        
