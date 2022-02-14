class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x = y = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                y.next = list1
                list1 = list1.next
            else:
                y.next = list2
                list2 = list2.next
            y = y.next
        y.next = list1 or list2
        
        return x.next
