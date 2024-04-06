class Node:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a node in a binary tree.

        Args:
        - val: Value of the node (default is 0)
        - left: Left child of the node (default is None)
        - right: Right child of the node (default is None)
        """
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, l, r):
    """
    Find the lowest common ancestor (LCA) of two nodes in a binary search tree.

    Args:
    - root: Root node of the binary search tree
    - l: First node
    - r: Second node

    Returns:
    - Node: LCA of the two input nodes
    """
    if not root:
        return None
    
    # If both p and q are smaller than the current node, LCA must be in the left subtree
    if l.val < root.val and r.val < root.val:
        return lowest_common_ancestor(root.left, l, r)
    
    # If both p and q are greater than the current node, LCA must be in the right subtree
    if l.val > root.val and r.val > root.val:
        return lowest_common_ancestor(root.right, l, r)
    
    # If one node is on the left subtree and the other is on the right subtree,
    # or if the current node is equal to either p or q, then the current node is the LCA
    return root

# Test Cases
root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(9)
root.left.right.left = Node(3)
root.left.right.right = Node(5)

test1 = lowest_common_ancestor(root, root.left.left, root.left.right.right)
print(test1.val)   # Output: 2 (0 and 5)
test2 = lowest_common_ancestor(root, root.right.left, root.right.right)
print(test2.val)   # Output: 8 (7 and 9)
test3 = lowest_common_ancestor(root, root.left.right.left, root.right)
print(test3.val)   # Output: 6 (3 and 8)
test4 = lowest_common_ancestor(root, root.left, root.left.right)
print(test4.val)   # Output: 2 (2 and 4)