
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
        layer_i_node_vals = list(map(lambda x: getattr(x, "val", None), nodes))
        if all([val is None for val in layer_i_node_vals]):
            break
        layer_dict_vals.append(layer_i_node_vals)
    return layer_dict_vals


def print_from_layer_dict(layer_dict_vals):
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
        # if len(layer) == 1 or len(layer) > 1 and layer[0] != "x" and layer[1] != "x":
        for child_i, child in enumerate(layer): 
            if child_i % 2 == 1:
                line += str(child) + " " * (2** (height - layer_i) - 4) 
            else:
                line += "  " + str(child) + " " * 2** (height - layer_i)
        print(line)

def pprint_tree(root):
    from binarytree import build
    root = build([val for layer in bfs_tree(root) for val in layer])
    print(root)

