"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop()
#         else:
#             return

import sys
sys.path.append('C:\\Users\\mgroe\\Desktop\\lambdaGit\\DS\\week 2\\Data-Structures\\singly_linked_list')
from singly_linked_list import LinkedList, Node


class Stack:
    def __init__(self, init_node=None):
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
        return length
    def push(self, value):
        self.storage.add_to_tail(value)
    def pop(self):
        val = self.storage.remove_tail()
        return val