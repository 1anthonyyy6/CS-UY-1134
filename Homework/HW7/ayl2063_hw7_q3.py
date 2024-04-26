from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):
    def subtree_is_height_balanced(root):
        if root is None:
            return (True, 0)
        else:
            left_sub, right_sub = subtree_is_height_balanced(root.left), subtree_is_height_balanced(root.right)
            left_sub_balanced, left_sub_height = left_sub[0], left_sub[1]
            right_sub_balanced, right_sub_height = right_sub[0], right_sub[1]
            height = max(left_sub_height, right_sub_height) + 1
            if abs(left_sub_height - right_sub_height) <= 1 and (left_sub_balanced and right_sub_balanced):
                return (True, height)
            else:
                return (False, height)
    if bin_tree.root is None:
        raise Exception('empty tree')
    else:
        return subtree_is_height_balanced(bin_tree.root)[0]
    
