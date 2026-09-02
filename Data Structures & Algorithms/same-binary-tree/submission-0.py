# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_tree = deque([p])
        q_tree = deque([q])

        while p_tree and q_tree:
            p_node = p_tree.popleft()
            q_node = q_tree.popleft()

            if p_node and q_node and p_node.val == q_node.val:
                p_tree.append(p_node.left)
                p_tree.append(p_node.right)
                q_tree.append(q_node.left)
                q_tree.append(q_node.right)
            elif p_node is None and q_node is None:
                continue
            else:
                return False
        
        return True