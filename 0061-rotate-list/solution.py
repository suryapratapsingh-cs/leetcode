class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute length and find old tail
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        
        # 2. Optimization
        k = k % n
        if k == 0:
            return head
        
        # 3. Connect tail to head to form a circle
        curr.next = head
        
        # 4. Find new tail: (n - k - 1) steps from head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next
            
        # 5. Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
