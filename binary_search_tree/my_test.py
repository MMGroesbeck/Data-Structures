import unittest
import random
import sys
import io
from binary_search_tree import BSTNode

bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.in_order_print(bst)
# bst.bft_print(bst)
bst.dft_print(bst)