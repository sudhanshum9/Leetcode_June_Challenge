# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        start=root
        while start:
            if(start.val==val):
                break
            
            
            if(val<start.val):
                start= start.left
            elif(val>start.val):
                start=start.right
                
        return start