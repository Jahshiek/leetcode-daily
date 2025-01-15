class Solution:
    def largestGoodInteger(self, num: str) -> str:
        newStr = ""

        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                curr = num[i] * 3

                if curr > newStr:
                    newStr = curr
        return newStr