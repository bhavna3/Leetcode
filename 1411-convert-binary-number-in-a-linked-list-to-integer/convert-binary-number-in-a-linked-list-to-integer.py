# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        b=''
        while head:
            b=b+str(head.val)
            head=head.next
        d=int(b,2)
        return d
        