class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f, m = flowerbed, len(flowerbed)
        
        for i in range(m):
            x = f[i-1] if i>0 else 0
            y = f[i+1] if i+1<m else 0
            if not f[i] and not x and not y:
                f[i], n = 1, n-1
                
        return n <= 0
