# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                left_height, left_diameter = mp[node.left]
                right_height, right_diameter = mp[node.right]

                height = 1 + max(left_height, right_height)
                diameter = max(left_height + right_height, left_diameter, right_diameter)
                mp[node] = (height, diameter)
            
        return mp[root][1]