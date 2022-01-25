class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack=[]
        for i in range(len(nums1)):
            
            
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                        x=j
            for i in range(x,len(nums2)):
                    if nums2[i]>nums2[x]:
                        stack.append(nums2[i])
                        break
                    elif i==len(nums2)-1:
                        stack.append(-1)
                    else:
                        continue
        return stack
