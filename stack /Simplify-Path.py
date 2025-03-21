class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new_str = path.split('/')

        for char in new_str:
            if (char == '.' or char == ''):
                continue
            elif (char == '..'):
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return '/' + \/\.join(stack)

o(n)
o(n)