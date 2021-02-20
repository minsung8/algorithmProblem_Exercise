class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
                
        total = 0

        temp = 1
        while l1:
            total += temp * l1.val
            l1 = l1.next
            temp *= 10

        temp2 = 1
        while l2:
            total += temp2 * l2.val
            l2 = l2.next
            temp2 *= 10
            
        cur_node = None
        head = None

        for s in reversed(str(total)):
            if not head:
                cur_node = ListNode(int(s))
                head = cur_node
            else:
                cur_node.next = ListNode(int(s))
                cur_node = cur_node.next
        return head








