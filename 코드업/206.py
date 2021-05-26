class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev

        next, node.next = node.next, prev
        return reverse(next, node)

nums = list(map(int, input().split()))
this = head = ListNode()
for n in nums:
    cur = ListNode(n)
    head.next = cur
    head = head.next