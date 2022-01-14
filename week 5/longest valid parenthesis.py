class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        start=0
        for i in range(len(s)):
            brack=s[i]
            if stack and s[stack[-1]]=='(' and brack==')':
                stack.pop()
            else:
                stack.append(i)
        length=0
        if stack:
            length=max(stack[0],len(s)-1-stack[-1])
            for i in range(1,len(stack)):
                length=max(length,stack[i]-stack[i-1]-1)
        else:
            return len(s)
        return length
