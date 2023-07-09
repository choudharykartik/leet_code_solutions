# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_height(self,root,max_dia):
        if root== None :
            return 0,0
        lh,ldia = self.max_height(root.left,max_dia)
        lr,rdia = self.max_height(root.right,max_dia)
        height = 1+ max(lh,lr) 
        diameter = lh+lr
        max_dia = max(diameter,max_dia,ldia,rdia)
        print(root.val,height,max_dia)
        return height,max_dia


    def diameterOfBinaryTree(self, root: Optional[TreeNode],diameter:int=0) -> int:
        
        lh,dia = self.max_height(root,0)
        return dia