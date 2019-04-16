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

nodetree = [Node(1,0),Node(2,1),Node(3,1),Node(4,2), Node(5,2), Node(6,3), Node(7,3), Node(8,4), Node(9,4)]


def lca(node1, node2):
    """
    Function takes 2 parameters of nodes and return common parent
    :param node1:
    :param node2:
    :return: common_parent
    """

    parent_value = confirm_parent(node1.parent, node2.parent)

    while parent_value == None:
        if node1.isRoot() or node2.isRoot():
            break
        node1 = nodetree[node1.parent]
        node2 = nodetree[node2.parent]
        parent_value = confirm_parent(node1.parent, node2.parent)

    return parent_value


def confirm_parent(num1, num2):
    if num1 == num2:
        return num1
    else:
        return None



print(lca(nodetree[1],nodetree[2]))
print(lca(nodetree[7],nodetree[8]))