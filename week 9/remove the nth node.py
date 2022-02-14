class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        
        start = runner = head
        while(head):
            count += 1
            head = head.next
        traverse = count    
        if n == count:
            return start.next
        while(start and traverse > 1):
            traverse -= 1
            if traverse == n:
                start.next = start.next.next
            start = start.next
           
        return runner
