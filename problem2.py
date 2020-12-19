# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        count = 0
        num1 = 0
        num2 = 0
        while curr1 is not None:
            num1 += curr1.val * (10**count)
            count += 1
            curr1 = curr1.next
        
        count = 0
        while curr2 is not None:
            num2 += curr2.val * (10**count)
            count += 1
            curr2 = curr2.next
        
        num3 = num1 + num2
        
        temp = num3 % 10
        retList = ListNode(temp)
        curr = retList
        count = 0
        for c in str(num3)[::-1]:
            if count == 0:
                count += 1
                continue
            curr.next = ListNode(int(c))
            curr = curr.next
        
        
        return(retList)


        