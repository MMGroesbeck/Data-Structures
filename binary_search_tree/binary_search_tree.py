"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# import sys
# sys.path.append('C:\\Users\\mgroe\\Desktop\\lambdaGit\\DS\\week 2\\Data-Structures\\queue')
# from queue import Queue
# sys.path.append('C:\\Users\\mgroe\\Desktop\\lambdaGit\\DS\\week 2\\Data-Structures\\stack')
# from stack import Stack

import sys
sys.path.append('C:\\Users\\mgroe\\Desktop\\lambdaGit\\DS\\week 2\\Data-Structures\\singly_linked_list')
from singly_linked_list import LinkedList, Node

class Queue:
    def __init__(self, init_node=None):
        if init_node:
            self.size = 1
        else:
            self.size = 0
        self.storage = LinkedList(init_node)
    
    def __len__(self):
        length = 0
        if self.storage.head:
            length = 1
            current = self.storage.head
            while current.next:
                length += 1
                current = current.next
        self.size = length
        return length

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        val = self.storage.remove_head()
        if val:
            self.size -= 1
        return val

class Stack:
    def __init__(self, init_node=None):
        if init_node:
            self.size = 1
        else:
            self.size = 0
        self.storage = LinkedList(init_node)
    def __len__(self):
        length = 0
        if self.storage.head:
            length = 1
            current = self.storage.head
            while current.next:
                length += 1
                current = current.next
        self.size = length
        return length
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
    def pop(self):
        val = self.storage.remove_tail()
        if val:
            self.size -= 1
        return val

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
                return self.left
            else:
                return self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
                return self.right
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    
    def bft_print(self, node):
        found = Queue(node)
        while found.size > 0:
            this_node = found.dequeue()
            print(this_node.value)
            if this_node.left:
                found.enqueue(this_node.left)
            if this_node.right:
                found.enqueue(this_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        found = Stack(node)
        while found.size > 0:
            this_node = found.pop()
            print(this_node.value)
            if this_node.left:
                found.push(this_node.left)
            if this_node.right:
                found.push(this_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
