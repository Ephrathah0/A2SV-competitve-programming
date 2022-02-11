class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            
            while stack and stack[-1]==popped[index]:
                stack.pop()
                index += 1
                
        return index ==len(popped)
