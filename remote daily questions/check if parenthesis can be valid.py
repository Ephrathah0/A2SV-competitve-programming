class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:  
            return False

        amount = 0
        for i in range(len(s)):
            amount += 1 if s[i] == '(' or locked[i] == '0' else -1
            if amount < 0:
                return False


        amount = 0
        for i in range(len(s) - 1, -1, -1):
            amount += 1 if s[i] == ')' or locked[i] == '0' else -1
            if amount < 0:
                return False

        return True
