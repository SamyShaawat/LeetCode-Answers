# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hs = set(nums)
        cur = head
        prev = None

        while cur:
            if cur.val in hs:
                if cur == head:
                    head = head.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return head