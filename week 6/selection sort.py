class Solution: 
    def select(self, arr, i):
        #code here
        pos = i
        for j in range(i,len(arr)):
            if arr[j]<arr[pos]:
                pos = j
        return pos    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            pos = self.select(arr,i)
            tmp = arr[pos]
            arr[pos] = arr[i]
            arr[i] = tmp
        return arr
