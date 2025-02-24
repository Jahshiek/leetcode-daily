class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []


        for i in range(len(operations)):
            print(operations[i])
            if operations[i] == 'C' :
                stack.pop()
            elif operations[i] == 'D':
                stack.append(stack[-1] * 2)
            elif operations[i] == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(operations[i]))
        return sum(stack)


[\5\,\2\,\C\,\D\,\+\]

5, 10, 15