import copy

"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    def _compare(self, x, y):
        if isinstance(x, str):
            x = ord(x)
        if isinstance(y,str):
            y = ord(y)
        return x < y
    """
    Computes the maximum number of levels there are
    in the tree
    """
    
    def update_height(self):
        if not self.node:
            self.height = -1
        left = -1
        right = -1
        if self.node.left:
            self.node.left.update_height()
            left = self.node.left.height
        if self.node.right:
            self.node.right.update_height()
            right = self.node.right.height
        self.height = 1 + max(left, right)

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        left = -1
        right = -1
        if self.node.left:
            self.node.left.update_height()
            left = self.node.left.height
        if self.node.right:
            self.node.right.update_height()
            right = self.node.right.height
        self.balance = left - right

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        if self.node == None or self.node.right == None:
            return

        x = self.node
        shifted = self.node.right
        y = shifted.node
        x.right = y.left
        y.left = shifted
        self.node = y
        shifted.node = x

        self.update_height()
        self.update_balance()

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        if self.node == None or self.node.left == None:
            return
        
        x = self.node
        shifted = self.node.left
        y = shifted.node
        x.left = y.right
        y.right = shifted
        self.node = y
        shifted.node = x

        self.update_height()
        self.update_balance()

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def _swap_keys(self, left=True):
        x = self.node.key
        if left:
            y = self.node.left.node
        else:
            y = self.node.right.node
        self.node.key = y.key
        y.key = x
        
    
    def _arrange(self):
        if self.node.left:
            self.node.left._arrange()
            # if self.node.key < self.node.left.node.key:
            #     self._swap_keys(True)
            if self._compare(self.node.key, self.node.left.node.key):
                self._swap_keys(True)
        if self.node.right:
            self.node.right._arrange()
            if self._compare(self.node.right.node.key, self.node.key):
                self._swap_keys(False)
            # if self.node.key > self.node.right.node.key:
            #     self._swap_keys(False)

    def rebalance(self):
        self._arrange()
        self.update_height()
        self.update_balance()
        while self.balance < -1:
            print("a: ", self.balance)
            self.left_rotate()
            print("b: ", self.balance)
        while self.balance > 1:
            print("c: ", self.balance)
            self.display()
            self.right_rotate()
            print("d: ", self.balance)
            self.display()
        if self.node.left:
            self.node.left.rebalance()
        if self.node.right:
            self.node.right.rebalance()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def _unbal_insert(self, key):
        if self.node == None:
            self.node = Node(key)
        if self._compare(key, self.node.key):
            if self.node.left == None:
                self.node.left = AVLTree(Node(key))
                return self.node.left
            else:
                return self.node.left._unbal_insert(key)
        else:
            if self.node.right == None:
                self.node.right = AVLTree(Node(key))
                return self.node.right
            else:
                return self.node.right._unbal_insert(key)

    def insert(self, key):
        reply = self._unbal_insert(key)
        self.rebalance()
        self.update_height()
        return reply