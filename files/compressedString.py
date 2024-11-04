class Solution:
    def compressedString(self, word: str) -> str:
        # we have empty string. we want to iterate across whole given word
        # while the current char is the same and length of prefix is <9, charCount +=1, pointer+=1
        # exit the second while loop, word +=  charCount + preFix
        comp = ""
        left = 0
        preFixLength = 0

        while left < len(word):
            preFixLength = 1
            while left<len(word)-1 and word[left] == word[left+1] and preFixLength <9:
                preFixLength+=1
                left +=1
            comp += str(preFixLength)+word[left]
            left+=1
        return comp
