# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if there's only one node, deleting it returns None
        if not head or not head.next:
            return None
        
        slow = head
        fast = head.next.next  # Start fast two steps ahead to stop slow right before the middle
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Delete the middle node
        slow.next = slow.next.next
        
        return head
