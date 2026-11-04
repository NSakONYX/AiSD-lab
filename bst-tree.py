class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key)
        return node


    def contains(self, key):
        current = self.root
        while current:
            if key == current.key:
                return True
            current = current.left if key < current.key else current.right
        return False


    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete_rec(node.right, successor.key)

        return node

    def _min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

   
    def inorder(self):
        def _walk(node):
            if node:
                yield from _walk(node.left)
                yield node.key
                yield from _walk(node.right)

        return list(_walk(self.root))