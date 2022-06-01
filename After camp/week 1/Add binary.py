class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i,j = len(a)-1, len(b)-1
        
        result = []
        while max(i, j) > -1:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j  >= 0 else 0
            
            mid_sum = x + y + carry
            if mid_sum > 1:
                carry = 1
                mid_sum -= 2
            else:carry = 0
                
            result.append(mid_sum)
            if i >= 0: i -=1
            if j >= 0: j -=1
                
        if carry > 0:result.append(1)
        return ''.join(list(map(str, result[::-1])))
