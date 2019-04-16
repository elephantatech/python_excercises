from unittest import TestCase
from Excercise2 import lca, Node, confirm_parent, nodetree


class TestLca(TestCase):
    def test_lca_imediate(self):
        """
        node 1 is 2 with parent 1
        node 2 is 3 with parent 1
        """
        self.assertEqual(lca(nodetree[2], nodetree[3]), 1)

    def test_lca_longest(self):
        """
        test 2 nodes with the largest distance
        node 1 is 7 with parent 2
        node 2 is 9 with parent 4
        """
        self.assertEqual(lca(nodetree[7], nodetree[9]), 1)

    def test_lca_root(self):
        """
        test node 1 as root or ancestor node
        node 2 as 9
        the return value should be 1
        """
        self.assertEqual(lca(nodetree[1],nodetree[9]), 1)

