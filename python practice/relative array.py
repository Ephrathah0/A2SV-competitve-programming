class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_same=[]
        arr2_diff=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    arr1_same.append(i)
        arr1.sort()
        
        for i in arr1:
            if i not in arr1_same:
                arr2_diff.append(i)
        return arr1_same + arr2_diff
