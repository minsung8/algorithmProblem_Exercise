class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        cur_node = None

        over = 0

        while l1 or l2:

            if not head:

                temp = l1.val + l2.val

                if temp >= 10:
                    over += 1
                    temp -= 10
                
                head = ListNode(temp)
                cur_node = head
                l1 = l1.next
                l2 = l2.next
            
            else:

                if l1 and l2:
                    temp = l1.val + l2.val
                elif l1:
                    temp = l1.val
                else:
                    temp = l2.val

                if over > 0:
                    temp += 1
                    over = 0
                
                if temp >= 10:
                    over += 1
                    temp -= 10
                
                cur_node.next = ListNode(temp)
                cur_node = cur_node.next

                if l1 and l2:
                    l1 = l1.next
                    l2 = l2.next
                elif l1:
                    l1 = l1.next
                else:
                    l2 = l2.next
        if temp > 0:
            cur_node.next = ListNode(1)
        
        return head


        
            
            

                
                

        
