class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # first, convert sentence to a list of words.
        # then, check if sentence[0][0] == sentence[-1][-1]
        # if it's true, continue, otherwise, return false
        # then, loop through all the words in the list until len(words)-2
        # if sentence[i][-1] == sentence[i+1][0] != True, return false
        wordsList = sentence.split(" ")
        if wordsList[0][0] != wordsList[-1][-1]:
            return False
                

        for i in range(len(wordsList)-1):
            if wordsList[i][-1] != wordsList[i+1][0]:
                return False
        

        return True
