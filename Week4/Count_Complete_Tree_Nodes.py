    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def countNodes(self, root: TreeNode) -> int:

            if root is None:
                return 0

            stack=[root,]
            count=0

            while stack:
                root=stack.pop()

                if root is not None:
                    count+=1
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)


            return counts