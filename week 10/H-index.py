class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        counter = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                counter += 1
            else:
                return counter
            
        return counter
