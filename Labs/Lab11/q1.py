from LinkedBinaryTree import LinkedBinaryTree

def bt_even_sum(root):
    if root is None:
        return 0
    else:
        left_evenSum = bt_even_sum(root.left)
        right_evenSum = bt_even_sum(root.right)
        sum = left_evenSum + right_evenSum
        if root.data % 2 == 0:
            sum += root.data
        return sum
    
def main():
    a = LinkedBinaryTree.Node(5)
    b = LinkedBinaryTree.Node(3)
    c = LinkedBinaryTree.Node(6, a, b)
    d = LinkedBinaryTree.Node(8)
    e = LinkedBinaryTree.Node(10, None, d)
    f = LinkedBinaryTree.Node(12, e, c)
    bin_tree = LinkedBinaryTree(f)
    print(bt_even_sum(bin_tree.root))

main()