from typing import *


class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def reverse_link(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def link_to_list(self, node) -> List:
        list: List = []

        while node:
            list.append(node.val)
            node = node.next

        return list

    def list_to_link(nums):
        root = head = LinkNode()

        for n in nums:
            head.next = LinkNode(n)
            head = head.next

        return root.next

    def __str__(self):
        node = self
        out = ''
        while node.next:
            out += f'{node.val}->'
            node = node.next
        out += str(node.val)
        return out

a = list(range(10))
node = LinkNode.list_to_link(a)
print(node)