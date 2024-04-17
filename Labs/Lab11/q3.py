from LinkedBinaryTree import LinkedBinaryTree

def is_full(root):
    if root.left is None and root.right is None:
        return True
    elif root.left is None and root.right is not None:
        return False
    elif root.left is not None and root.right is None:
        return False
    else:
        return is_full(root.left) and is_full(root.right)
    
def main():
    a = LinkedBinaryTree.Node(3)
    b = LinkedBinaryTree.Node(9)
    c = LinkedBinaryTree.Node(11)
    d = LinkedBinaryTree.Node(4)
    e = LinkedBinaryTree.Node(1, b, c)
    f = LinkedBinaryTree.Node(6, e, d)
    root = LinkedBinaryTree.Node(7, a, f)
    bin_tree = LinkedBinaryTree(root)
    print(is_full(bin_tree.root))

main()