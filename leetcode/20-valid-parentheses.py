class Solution(object):
    def isValid(self, s:str) -> bool:

        if(len(s)<=1):
            return False

        pairs : dict[str, str] = {"}":"{","]":"[",")":"("}
        stack : list[str] = []

        for char in s:
            if char in pairs:

                if stack.__len__() < 1:
                    return False
                
                temp = stack[-1]
                
                if pairs[char] == temp:
                    stack.pop()

                else:
                    stack.append(char)
            else:
                stack.append(char)

        if stack.__len__() == 0:
            return True

        return False

p  = Solution()
v = p.isValid("{[()]}()")
print(v)
