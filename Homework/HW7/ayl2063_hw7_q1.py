from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return (root.data, root.data) 
        elif root.left is None:
            subtree = subtree_min_and_max(root.right)
            min, max = subtree[0], subtree[1]
        elif root.right is None:
            subtree = subtree_min_and_max(root.left)
            min, max = subtree[0], subtree[1]
        else:
            left_min_max = subtree_min_and_max(root.left)
            right_min_max = subtree_min_and_max(root.right)
            min, max = right_min_max[0], right_min_max[1]
            if left_min_max[0] < min:
                min = left_min_max[0]
            if left_min_max[1] > max:
                max = left_min_max[1]
        if root.data < min:
            min = root.data
        elif root.data > max:
            max = root.data
        return (min, max)
    
    if bin_tree.root is None:
        raise Exception('empty')
    return subtree_min_and_max(bin_tree.root)

def main():
    a = LinkedBinaryTree.Node(5)
    b = LinkedBinaryTree.Node(1)
    c = LinkedBinaryTree.Node(8)
    d = LinkedBinaryTree.Node(4)
    e = LinkedBinaryTree.Node(9, a, b)
    f = LinkedBinaryTree.Node(7, c, d)
    g = LinkedBinaryTree.Node(2, e, None)
    h = LinkedBinaryTree.Node(3, g, f)
    tree = LinkedBinaryTree(h)
    print(min_and_max(tree))

#main()