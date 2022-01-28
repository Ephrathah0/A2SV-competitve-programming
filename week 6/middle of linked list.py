class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        count = 1
        headPos = 1
        mid = 0
        
        while curr.next:
            curr = curr.next
            count+=1
       
        if count % 2 == 0:
            mid = (count/2) + 1
        else: 
            mid = (count+1)/2
        
        while headPos!= mid:
            head = head.next
            headPos+= 1
        return head
