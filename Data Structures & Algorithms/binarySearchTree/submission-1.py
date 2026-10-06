class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if self.root is None:
            self.root = new_node
            return
        
        curr = self.root
        while curr:
            if curr.key < new_node.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            elif curr.key > new_node.key:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            else:
                curr.val = new_node.val
                return        


    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.left
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.val if curr else -1

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.findMax(self.root)
        return curr.val if curr else -1
    
    def findMax(self, node: TreeNode) -> TreeNode:
        while node and node.right:
            node = node.right
        return node
    
    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    # def remove(self, key: int) -> None:
    #     self.removeHelper(self.root, key)
        
    # def removeHelper(self, node: TreeNode, key: int) -> None:
    #     curr = node
    #     prev = None
    #     temp = None
    #     while curr:
    #         temp = curr
    #         if curr.key < key:
    #             curr = curr.right
    #         elif curr.key > key:
    #             curr = curr.left
    #         else:
    #             break
    #         prev = temp
        
    #     if not curr:
    #         return
    #     elif not curr.left:
    #         curr = curr.right
    #     elif not curr.right:
    #         curr = curr.left
    #     else:
    #         min_node = self.findMin(curr.right)
    #         curr.key = min_node.key
    #         curr.val = min_node.val
    #         self.removeHelper(curr.right, min_node.key)

    #     if prev:
    #         if prev.right == temp:
    #             prev.right = curr
    #         else:
    #             prev.left = curr
    #     else:
    #         self.root = curr

    def getInorderKeys(self) -> List[int]:
        res = []
        stack = []
        curr = self.root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.key)
                curr = curr.right
        
        return res
