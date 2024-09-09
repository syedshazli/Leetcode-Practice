class Solution:
    def romanToInt(self, s: str) -> int:
        #maybe write if the next number after current is a subtraction case
                #then just subtract 1 from result
        sum = 0
        hashmap = dict()
        hashmap["I"] = 1
        hashmap["V"] = 5
        hashmap["X"] = 10
        hashmap["L"] = 50
        hashmap["C"] = 100
        hashmap["D"] = 500
        hashmap["M"] = 1000
        for i in range(len(s)-1):
            if s[i] == "I":
                if s[i+1] == "V" or s[i+1] == "X":
                    sum-=1
                    continue
                sum+=hashmap[s[i]]
                continue
            elif s[i] == "X":
                if s[i+1] == "L" or s[i+1] == "C":
                    sum-=10
                    continue
                sum+= hashmap[s[i]]
            elif s[i] == "C":
                if s[i+1] == "D" or s[i+1] == "M":
                    sum-=100
                    continue
                sum+= hashmap[s[i]]
            else:
                sum+= hashmap[s[i]] 
        sum+=hashmap[s[len(s)-1]]  
            
        return sum

        
