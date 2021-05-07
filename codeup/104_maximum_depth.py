# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

def list2link(nums):
    root = node = TreeNode(nums[0])
    q = collections.deque([root])
    for i, n in enumerate(nums[1:]):
        if node.right is not None:
            node = node.left
        if i % 2 == 0:
            node.left = TreeNode(n)
        else:
            node.right = TreeNode(n)


    return root


def maxDepth(root: TreeNode) -> int:
    q = collections.deque([root])
    depth = 0
    while q:
        depth += 1

        for _ in range(len(q)):
            cur_root = q.popleft()
            if cur_root.left:
                q.append(cur_root.left)
            if cur_root.right:
                q.append(cur_root.right)

    return depth

nums = [3, 9, 20, None, None, 15, 7]
tree = list2link(nums)
depth = maxDepth(tree)
print(depth)
