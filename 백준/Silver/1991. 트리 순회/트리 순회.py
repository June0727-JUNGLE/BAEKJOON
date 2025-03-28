import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def insert(self, parent, left, right):
        if parent not in self.nodes:
            self.nodes[parent] = Node(parent)
        node = self.nodes[parent]
        
        if left != '.':
            if left not in self.nodes:
                self.nodes[left] = Node(left)
            node.left = self.nodes[left]

        if right != '.':
            if right not in self.nodes:
                self.nodes[right] = Node(right)
            node.right = self.nodes[right]

    def build(self, info_list):
        for parent, left, right in info_list:
            self.insert(parent, left, right)
        self.root = self.nodes['A']

    def preorder(self, node):
        if node:
            print(node.key, end='')
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end='')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end='')

if __name__ == "__main__":
    n = int(input())
    
    input_data = []
    for _ in range(n):
        parent, left, right = input().split()
        input_data.append((parent, left, right))
    
    tree = BinaryTree()
    tree.build(input_data)

    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()
    