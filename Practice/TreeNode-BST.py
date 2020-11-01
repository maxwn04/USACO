import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self ==  None:
            self.val = val
        elif val <= self.val:
            self.left.insert(val)
            if self.left.height() > self.right.height() + 1:
                if self.left.right.height() > self.left.left.height():
                    self.LRrotate()
                else:
                    self.Rrotate()
        elif val > self.val:
            self.right.insert(val)
            if self.right.height() > self.left.height() + 1:
                if self.right.left.height() > self.right.right.height():
                    self.RLrotate()
                else:
                    self.Lrotate()

    def delete(self, val):  
        if self.val == val:
            if self.right.height() > self.left.height():
                self.val = self.right.val
                right = self.right
        self.right.delete()
        self.left.delete()
    
    def deleteShift(self):
            if self.right.height() > self.left.height():
                self.val = self.right.val
                self.right.deleteShift()
            elif self.left.height() > 0:
                self.val = self.left.val
                self.left.deleteShift()

    def height(self):
        """returns the height of the tree rooted at self"""
        if self ==  None
            return 0
        height = max(self.right.height(), self.left.height()) + 1
        return height

    def Lrotate(self):
        """rotates  the tree around self such that the end result is balanced"""
        b = self.right
        a = self
        a.right = b.left
        b.left = a
        self = b
        self.left = a

    def Rrotate(self):
        """rotates  the tree around self such that the end result is balanced"""
        b = self.left
        a = self
        a.left = b.right
        b.right = a
        self = b
        self.right = a

    def LRrotate(self):
        self.left.Lrotate()
        self.Rrotate()
        
    def RLrotate(self):
        self.right.Rrotate()
        self.Lrotate()

    def isBalanced(self):
        """returns True if subtree rooted at root is balanced (left and right subtrees differ by height at most 1) else False"""
        dif = math.abs(root.right.height() - root.left.height())
        if self.right == None and self.left.height() <= 1 
        or self.left == None and self.right.height <= 1:
            return True
        if root.right.isBalanced() and root.left.isBalanced():
            return True
        return False    


    def pprint_tree(self, _prefix="", _last=True):
        """recursively pretty-prints a tree in horizontal format"""
        print(_prefix, "`- " if _last else "|- ", self.val)
        _prefix += "   " if _last else "|  "
        children = [self.left, self.right]
        # skip this layer if both children are None
        if self.left is None and self.right is None:
            return
        child_count = len(children)
        for i, child in enumerate(children):
            _last = i == (child_count - 1)
            # recursively print tree rooted at child if it exists
            if child is not None:
                child.pprint_tree(_prefix, _last)
            else: # else print None
                print(_prefix, "`- " if _last else "|- ", None)

def bfs_tree(root):
    """pretty-prints a tree vertically (the normal way) by BFSing to get the layer dict.
    Only looks nice for trees up to height 3 (0-indexed, so 4 layers including the root layer)"""

    from collections import defaultdict
    layer_dict = [[]]
    layer_i = 0
    layer_dict[layer_i].append(root)

    # BFS
    while len(layer_dict[layer_i]) > 0:
        layer_dict.append([])
        for node in layer_dict[layer_i]:
            if node is None:
                continue
            children = [node.left, node.right]
            layer_dict[layer_i + 1].extend(children)
        layer_i += 1

    # Convert layer_dict from TreeNodes to values
    layer_dict_vals = []
    for layer_i, nodes in enumerate(layer_dict):
        layer_i_node_vals = list(map(lambda x: getattr(x, "val", "x"), nodes))
        if all([val is None for val in layer_i_node_vals]):
            break
        layer_dict_vals.append(layer_i_node_vals)
    print(layer_dict_vals)

    height = len(layer_dict_vals)
    # print tree
    for layer_i, layer in enumerate(layer_dict_vals):
        prefix = " " * (2** (height - layer_i) // 2)
        line = prefix + "  "
        if len(layer) > 1 and layer[0] != "x" and layer[1] != "x":
            for child_i, child in enumerate(layer): 
                stem = "\\" if child_i % 2 == 1 else "/"
                stem += " " *( 2** (height - layer_i) -1)
                line += stem
            print(line)    

        line = prefix 
        if len(layer) == 1 or len(layer) > 1 and layer[0] != "x" and layer[1] != "x":
            for child_i, child in enumerate(layer): 
                if child_i % 2 == 1:
                    line += str(child) + " " * (2** (height - layer_i) - 4) 
                else:
                    line += "  " + str(child) + " " * 2** (height - layer_i)
            print(line)


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


if __name__ == '__main__':
    adj = {1: [2, 4], 2: [3, 7], 3:[5, 6], 4:[8]}
    v = {1: 6, 2: 4, 3: 2, 4: 8, 5: 1, 6: 3, 7:5, 8:7}

    root = parse_graph_to_treenodes(adj, v, 1)
    bfs_tree(root)
    # root.pprint_tree()
