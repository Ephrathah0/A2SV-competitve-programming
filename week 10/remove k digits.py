class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num) <= k:
            return "0"
       
        newk = k
        for i in num:
            while stack and stack[-1] > i:
                if k < 1:
                    break
                stack.pop()
                k -= 1
            stack.append(i)
        while k > 0:
            stack.pop()
            k -= 1
            
        if len(num) == len(stack):
            while newk > 0:
                stack.pop()
                newk -= 1
                
        while len(stack) > 1 and stack[0] == "0":
            stack = stack[1:]
            
        return ''.join(stack)
