# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def set_list(nums: List[int]):
        head = node = None
        for n in nums:
            if head is None:
                head = node = ListNode(n)
            else:
                node = ListNode(n)
            node = node.next

        return head

    def __str__(self):
        node = self
        nodes = ""
        while node.next != None:
            nodes += f"{node.val}"
            if node.next != None:
                nodes += "->"
            node = node.next
        return nodes

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = mergeTwoLists(l1.next, l2)

    return l1

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(nums1, nums2)
l1 = ListNode.set_list(nums1)
l2 = ListNode.set_list(nums2)
print(mergeTwoLists(l1, l2))