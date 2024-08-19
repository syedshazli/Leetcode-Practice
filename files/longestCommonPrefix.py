class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        mini = min(strs)

        for i in range(len(mini)):
            for word in strs:
                if word[i] != strs[0][i] or i == len(word):
                    return string
            string += strs[0][i]

        return string
