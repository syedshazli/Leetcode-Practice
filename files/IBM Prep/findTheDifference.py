
class Solution:
    # return a letter thats not in the right spot
    # The thing is the letter is added at a random position, and any of the prev letters could be true 
    #so I think it's obvious we need a hashmap
    #it's confirmed we do add a letter somewhere
    #iterate through and make a map that coorelates letter to occurences for s
    # do the same for t
    # if there's an occurence in t that is ever greater than occurence in s, return it
    def findTheDifference(self, s: str, t: str) -> str:
        sMap = dict()
        tMap = dict()
        if len(s) == 0:
            return t
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i],0)+1
        
        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i],0)+1
         
            # if i<len(s) and tMap[t[i]]>sMap[s[i]]:
            #     return t[i]
            # elif i<len(s):
            #     continue
            # else:
            #     return t[i]
       
        for i in range(len(t)):
            if i<len(s) and sMap[s[i]]<tMap[s[i]]:
                return s[i]
            elif i==len(s):

                return t[i]
