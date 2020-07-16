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

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def _lvls_below(self):
        if not self.node:
            return -1
        else:
            left = -1
            right = -1
            if self.node.left:
                print("Left of ", self.node.key)
                left = self.node.left._lvls_below()
            if self.node.right:
                print("Right of ", self.node.key)
                right = self.node.right._lvls_below()
            return 1 + max(left, right)
    
    def update_height(self):
        self.height = self._lvls_below()

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        left = -1
        right = -1
        if self.node.left:
            left = self.node.left._lvls_below()
        if self.node.right:
            right = self.node.right._lvls_below()
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
        y = self.node.right
        self = y
        if self.node.left:
            x.right = self.node.left
        self.node.left = AVLTree(x)


    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        if self.node == None or self.node.left == None:
            return
        x = self.node
        y = self.node.left
        self = y
        if self.node.right:
            x.left = self.node.right
        self.node.right = AVLTree(x)

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_balance()
        while self.balance < -1:
            self.update_height()
            self.update_balance()
            self.left_rotate()
            self.update_balance()
        while self.balance > 1:
            self.update_height()
            self.update_balance()
            self.right_rotate()
            self.update_balance
        if self.node.left:
            self.node.left.rebalance()
        if self.node.right:
            self.node.right.rebalance()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def _compare(self, x, y):
        if isinstance(x, str):
            x = ord(x)
        if isinstance(y,str):
            y = ord(y)
        return x < y
    
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