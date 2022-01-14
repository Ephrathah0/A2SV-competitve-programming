class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        left, right, maxNum = 0, 0, 0
                for char in range(len(s)):
            if s[char] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                maxNum = max(maxNum, right*2)
               elif right >= left:
                left, right = 0, 0
      
        for char in range(len(s)-1, -1, -1):
            if s[char] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                maxNum = max(maxNum, left*2)
           elif left >= right:
                left, right, = 0, 0
                
        return maxNum
