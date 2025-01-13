class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newStr = ''
        commonPrefix = strs[0]

        for i in range(len(commonPrefix)):
            char = commonPrefix[i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return newStr
            newStr += char
        
        return newStr



        