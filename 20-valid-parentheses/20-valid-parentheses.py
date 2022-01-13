class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(': ')',
            '[': ']',
            '{' : '}'
        }
        par  = list()
        for i in s:
            if i in dic.keys():
                par.append(i)
            
            elif len(par) > 0 and i == dic[par[-1]]:
                par.pop()
            else:
                return False
                
        if len(par) == 0:
            return True
        else:
            return False
       