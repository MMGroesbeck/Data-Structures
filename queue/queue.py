"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self, init_list=[]):
#         self.size = 0
#         self.storage = init_list
    
#     def __len__(self):
#         length = len(self.storage)
#         self.size = length
#         return length

#     def enqueue(self, value):
#         self.storage.insert(0,value)

#     def dequeue(self):
#         if len(self) > 0:
#             return self.storage.pop()
#         else:
#             return None

import sys
sys.path.append('C:\\Users\\mgroe\\Desktop\\lambdaGit\\DS\\week 2\\Data-Structures\\singly_linked_list')
from singly_linked_list import LinkedList, Node

class Queue:
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
        self.size = length
        return length

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        val = self.storage.remove_head()
        return val