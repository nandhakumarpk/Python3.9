class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
        
def preorder(root):
    if root is not None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)
        
def postorder (root):
     if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key)

root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
print("Inorder")
inorder(root)
print("Preorder")
preorder(root)
print("Postorder")
postorder(root)
