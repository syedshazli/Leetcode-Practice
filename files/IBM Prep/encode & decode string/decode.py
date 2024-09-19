def decode(self, s: str) -> List[str]:
        # keep a window? 
        # I think we probably HAVE to keep a window
        # left starts at 0, right starts at 1
        # if str[i] == #:
        #   resArr.append(str[left:right])
        #   left = right
        #   right +=1
        # else:
        #   right +=1
        resArr = []
        left = 0
        while left<len(s):
            right = left
            while s[right] != "#": # move right over 1. 
                #we dont even wanna touch anything inside the #'s. 
                #This just lets us know when we got our length
                right+=1
                
            
            lengthStr = int(s[left:right])
            stringToProcess = s[right+1:lengthStr+1+right]
            resArr.append(stringToProcess)
            left = right+1+lengthStr
            
        return resArr



