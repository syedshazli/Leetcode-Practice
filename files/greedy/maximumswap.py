class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = str(num)
        resArr = []
        listStr = list(numStr)
        for i in range(len(listStr)):
            for j in range(i, len(listStr)):
                listStr = list(numStr)
                temp = listStr[i]
                listStr[i] = listStr[j]
                listStr[j] = temp
                result = "".join(listStr)
                resArr.append(int(result))
        return max(resArr)
