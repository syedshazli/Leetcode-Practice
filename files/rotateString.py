class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # abcde
        # bcdea
        #cdeab
        # can just have it run for 100 since thats the maximum size of the string
        # for i in range 100
        # temp = list[0]
        #list.pop(0)
        # list.append(temp)
        # if we're equal to the goal, return true
        if s == goal:
            return True
        List = list(s)
        for i in range(len(goal)):
            temp = List[0]
            List.pop(0)
            List.append(temp)
            if goal == "".join(List):
                return True
        return False


        
