def encode(self, strs: List[str]) -> str:
        #separate each word by a '#' character
        #this means add a # at the end of each word
        # also think about the last word, maybe we dont need to append there
        #for each word in the list, add to the end of the word
        newStr = []
        for word in strs:
            newStr.append(str(len(word)))
            newStr.append('#')
            newStr.append(word)
            
      
       
        newsString = ''.join(newStr)
        print(newsString)
        #return a string
        return newsString
