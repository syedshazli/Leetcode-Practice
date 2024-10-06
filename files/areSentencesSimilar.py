
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # each string is a sentence of words
        # list of words separated by a space (" ".join() most likely)
        # sentence 1 or 2 is not necessarily bigger than the other
        # cannot append letters onto already existing words either
        # it's only possible if the phrase  of the shorter sentence is:
        #           1. at the beginning of the longer sentence
        #           2. at the end of the longer sentence
        #           3. One part of phrase in beginning of sentence and other at the end
        #               a. Ex: sentence1 = "My name is Haley", sentence2 = "My Haley"
        # so if the phrase of the shorter sentence is at the beginning or end of longer sentence, return true
        # the "inserted phrase" cannot wrap around the phrase we're trying to change
        
        # split each sentence into an array of words. use "".join
        # we can check if the first word of each phrases are equal. if not, then we will try to see if last word of longer phrase vs first word of shorter phrase are equal.
        # if theres only one word in the shorter phrase and it's equal to the first/last word of longer, then it's easy. 
        # most likely return an array == secondArray
        sentenceOne = deque(sentence1.split(' '))
        sentenceTwo = deque(sentence2.split(' '))
        while sentenceTwo and sentenceOne: 
            #while both queues are not empty. If the shorter queue ends up being empty during the process we return true

            if sentenceTwo[0] == sentenceOne[0]:
                sentenceTwo.popleft() # will take off left most element in the array
                #important because we're testing to see if front facing elements are same 
                sentenceOne.popleft()
                continue

            # if they're not the same, test to see if last elements are the same.
            # we will have gotten to this point as well if we popped off the top and the front two are not equal anymore.
            elif sentenceTwo[-1] == sentenceOne[-1]:
                # last elements are the same
                sentenceTwo.pop() # remember pop takes off right most (or last ) element in array
                sentenceOne.pop()

                continue # so that it immedietlye checks status of both queues. if the popping results in one of them being empty, that means we succesfully discovered that the remainding phrase inside can be appended to edge

            
            return False
        
        return True
             
        # left= 0
        # right = max(len(sentenceOneArr), len(sentenceTwoArr))-1

        # # beginning words are equal
        # if sentenceOneArr[0] == sentenceTwoArr[0]:
        #     for i in range(len(min(len(sentenceOneArr),len(sentenceTwoArr)))):
        #         if 

        #     # if the previous word is in the longer sentence 
        #     return True
        # #beginning words and ending words are equal
        # elif sentenceOneArr[0] == sentenceTwoArr[-1] or sentenceOneArr[-1] == sentenceTwoArr[0]:
        #     return True
