class Solution:
    def reverseParentheses(self, s: str) -> str:
        d=''
        i=0
        string_index=[]
        for idx,val in enumerate(s):
            if val=='(':
                string_index.append(idx-i)
                d=d+val
            elif val ==')':
                temp=string_index.pop()
                d=d[0:temp]+d[temp+1:idx][::-1]
                i+=2
            else:
                d=d+val
        return d
