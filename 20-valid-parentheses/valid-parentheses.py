class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen={")":"(","}":"{","]":"["}
        stack=[]
        for br in s:
            if br in closetoopen:
                if stack and stack[-1]==closetoopen[br]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
        return True if len(stack)==0 else False


        