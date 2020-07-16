from avl_tree import AVLTree
from avl_tree import Node

tree = AVLTree()
tree.node = Node(5)

tree.insert(2)

tree.insert("a")

tree.insert(1)

tree.insert(3)

# tree.display()

tree._unbal_insert("b")

tree.right_rotate()

# tree.display()

tree.rebalance()

tree.display()

# tree.left_rotate()

tree.right_rotate()

tree.display()

# tree.right_rotate() #ENDLESS LOOP

tree.rebalance()

tree.display()

# tree.left_rotate() #ENDLESS LOOP

# tree.display()

# tree.rebalance()

# tree.display()