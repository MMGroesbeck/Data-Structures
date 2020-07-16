from avl_tree import AVLTree
from avl_tree import Node

tree = AVLTree()
tree.node = Node(5)

tree.insert(2)

tree.insert("a")

tree.insert(1)

tree.insert(3)

tree.display()

tree.insert("b")

tree.display()

tree.left_rotate()

tree.display()

tree.left_rotate()

tree.display()

tree.rebalance()

tree.display()