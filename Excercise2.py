""" Exercise 2
Author: Vivek Mistry
"""
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def isRoot(self):
        if self.parent == 0:
            return True
        else:
            return False

nodetree = { 1 : Node(1,0), 2 : Node(2,1), 3 : Node(3,1), 4 : Node(4,2),
             5 : Node(5,2), 6 : Node(6,3), 7 : Node(7,3), 8: Node(8,4), 9: Node(9,4)}


def lca(node1, node2):
    """
    Function takes 2 parameters of nodes and return common parent
    :param node1:
    :param node2:
    :return: common parent value on both nodes

    this function will take time to run if the nodetree is big as the function core runs recursively.
    Therefore the further apart the nodes on the node tree the longer it takes to find the parent.
    So other mechanisms need to be added to calculate how far apart the nodes are and how to get the common parent faster
    in a logical manner instead of a recursive manner.
    """
    parent_tree1 = get_all_parents(node1)
    parent_tree2 = get_all_parents(node2)
    if node1.isRoot():
        common_parents = set([1]).intersection(parent_tree2)
    elif node2.isRoot():
        common_parents = set(parent_tree1).intersection([1])
    else:
        common_parents = set(parent_tree1).intersection(parent_tree2)

    return max(common_parents)

def get_all_parents(node):
    parent_list = []
    while node.parent > 0:
        parent_list.append(nodetree[node.parent].value)
        node = nodetree[node.parent]

    return parent_list


def confirm_parent(num1, num2):
    if num1 == num2:
        return num1
    else:
        return None


# print(lca(nodetree[8],nodetree[9]))
# print(lca(nodetree[6],nodetree[8]))