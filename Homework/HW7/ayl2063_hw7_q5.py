from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    lst = prefix_exp_str.split()[::-1]
    root = LinkedBinaryTree.Node(lst.pop())
    def create_expression_subtree(root):
        if len(lst) == 0:
            return
        else:
            if lst[-1] not in '-+*/':
                new_node1 = LinkedBinaryTree.Node(int(lst[-1]))
                lst.pop()
            else:
                new_node1 = LinkedBinaryTree.Node(lst[-1])
                lst.pop()
                create_expression_subtree(new_node1)
            root.left = new_node1
            if lst[-1] not in '-+*/':
                new_node2 = LinkedBinaryTree.Node(int(lst[-1]))
                lst.pop()
            else:
                new_node2 = LinkedBinaryTree.Node(lst[-1])
                lst.pop()
                create_expression_subtree(new_node2)
            root.right = new_node2
    create_expression_subtree(root)
    tree = LinkedBinaryTree(root)
    return tree

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    s = ''
    for i in tree.postorder():
        if isinstance(i.data, int):
            s += str(i.data) + ' '
        else:
            s += i.data + ' '
    return s[:len(s) - 1]

def main():
    tree = create_expression_tree('* 2 + - 15 6 4')
    print(prefix_to_postfix('* 2 + - 15 6 4'))

#main()