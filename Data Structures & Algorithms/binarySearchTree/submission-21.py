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
        
    def removeHelper(self, node: TreeNode, key: int) -> None:
        if node is None:
            return None
        
        if node.key < key:
            node.right = self.removeHelper(node.right, key)
        elif node.key > key:
            node.left = self.removeHelper(node.left, key)
        else:
            if not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_node = self.findMin(node.right)
                node.key = min_node.key
                node.val = min_node.val
                node.right = self.removeHelper(node.right, min_node.key)
        
        return node

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
