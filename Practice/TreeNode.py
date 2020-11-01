from treenode_helper import pprint_tree


def parse_graph_to_treenodes(adj_list, values, root):
    visited = set()
    def dfs(node, values, adj_list):
        if node in visited:
            raise RuntimeError("your tree has cycles; trees may not contain cycles. node {} was detected to be part of a cycle".format(node))
        visited.add(node)
        children = adj_list.get(node, [])
        # print(children)
        num_children = len(children)
        if num_children > 2:
            raise RuntimeError("each node of a binary tree may only have at most 2 children. Node {} has {} children ({})\n".format(node, num_children, children))
        assert node in values, "you have not specified the value of node {} in the value dict\n".format(node)
        return TreeNode(values[node], dfs(adj_list[node][0], values, adj_list) if num_children > 0 and children[0] is not None else None, dfs(adj_list[node][1], values, adj_list) if num_children > 1 and children[1] is not None else None)

    root = dfs(root, values, adj_list)
    should_be_empty = set(values.keys()).difference(visited)
    assert not bool(should_be_empty), "\n\nEither 1. the tree you specified in the adjacency list is disjoint, or \n2. you specified the incorrect root, or \n3. you have extra nodes specified in the value dict whose relations are not specified in the adjacency list. \nThese nodes were not added to the TreeNode representation: {}\n".format(should_be_empty)
    # should_also_be_empty = visited.intersection
    return root


# Definition for a Recursive binary tree node data structure.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        """inserts a node with value val into the tree. This method should be recursive"""
        if val < self.val:
            if self.left is not None:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        elif val >= self.val:
            if self.right is not None:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
        else:
            raise RuntimeError("error")


    def delete(self, val):
        """returns the node with value val from the tree and deletes it from the tree if exists, else returns None and does nothing. If muliple nodes with val exist, deletes anyone of them."""
        pass

    def height(self):
        """returns the height of the tree rooted at self"""
        pass 

    def rotate(self):
        """rotates the tree around self such that the end result is balanced"""
        pass

    def isBalanced(self, root):
        """returns True if subtree rooted at root is balanced (left and right subtrees differ by height at most 1) else False"""
        pass


if __name__ == '__main__':
    adj = {1: [2, 4], 2: [3, 7], 3:[5, 6], 4:[8]}
    v = {1: 6, 2: 4, 3: 2, 4: 8, 5: 1, 6: 3, 7:5, 8:7}

    root = parse_graph_to_treenodes(adj, v, 1)
    pprint_tree(root)
    root.insert(9)
    pprint_tree(root)    
