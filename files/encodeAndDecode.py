class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for word in strs:
            newString += str(len(word))
            newString+="#"
            newString+= word
            #print(newString)
        print(newString)
       # newString = "#".join(strs)
        #encode works
        return newString




    def decode(self, s: str) -> List[str]:
        newList = []
        i = 0
        while i < len(s):
            j = i
            while(s[j] != "#"):
                j +=1
            length = int(s[i:j])
            newList.append(s[j+1:length+j+1])
            i= j +1 + length
        return newList
