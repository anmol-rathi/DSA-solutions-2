# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=0
        def dfs(node):
            nonlocal count
            sum_left=0
            sum_right=0
            left_count=0
            right_count=0
            if node.left:
                sum_left,left_count=dfs(node.left)
            if node.right:
                sum_right,right_count=dfs(node.right)
            totalnodes=left_count+right_count+1
            totalsum=sum_left+sum_right+node.val
            if (totalsum//totalnodes)==node.val:
                # print(node.val)
                count+=1
            return totalsum,totalnodes
        dfs(root)
        return count
            
            


        