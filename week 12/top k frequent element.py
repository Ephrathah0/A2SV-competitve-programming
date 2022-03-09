class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)  
        heap = [(-freq[word], word) for word in freq]       
        heapq.heapify(heap)
        ans = [heapq.heappop(heap)[1] for i in range(k)]
 
        return ans
