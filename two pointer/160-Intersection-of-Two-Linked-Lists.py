# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA  
        tempB = headB

        lengthA = 0
        lengthB = 0

        while headA:
            lengthA+=1
            headA = headA.next

        while headB:
            lengthB+=1
            headB = headB.next

        difference = abs(lengthB - lengthA)

        headA = tempA  
        headB = tempB

        if lengthA > lengthB:
            for _ in range(difference):
                headA = headA.next
        else:
            for _ in range(difference):
                headB = headB.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
