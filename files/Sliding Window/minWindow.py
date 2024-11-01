class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # this could be a simple hashmap problem if im not mistaken
        # make a window of some size. 
        # apparentley hashmap is inefficient solution... but we might as well try it
        # a window approach would just keep increasing the window until all the letters in our window are in t. From there, we can start removing from the left as long as all the letters are in t, and record the height at each step!
        hashmap = dict()
        for character in t:
            if character in hashmap:
                hashmap[character]+=1
            else:
                hashmap[character]=1
        
        left = 0
        right = 0

        minWindowLength = len(s)+1

        #start point of minWindow
        minWindowStart = 0
        #see how many characters still need to be included
        numCharsInclude = len(t)

        while right<len(s):
            # we found a character thats in t
            if s[right] in hashmap:
                if hashmap[s[right]]>0:
                    numCharsInclude-=1
                hashmap[s[right]]-=1
            
            #current window has all characters we want
            while numCharsInclude == 0:
                #check if window is smaller
                if right-left+1 < minWindowLength:
                    minWindowLength = right-left+1
                    minWindowStart = left

                #check if s[left] in t
                if s[left] in hashmap:
                    hashmap[s[left]]+=1
                    #if the value is > 0 then it is critical
                    if hashmap[s[left]]>0:
                        numCharsInclude+=1
                #move left forward, try to find smaller window
                left+=1
            #move right forward
            right+=1
        if minWindowLength == len(s)+1:
            return ""
        return s[minWindowStart:minWindowStart+minWindowLength] 
        
