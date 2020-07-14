import sys
sys.path.append('C:\\Users\\mgroe\\Desktop\\lambdaGit\\DS\\week 2\\Data-Structures\\doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.lru_list = DoublyLinkedList()
        self.lru_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if self.lru_list.head is None:
            return None
        else:
            this_node = self.lru_list.head
            while this_node.next is not None and this_node.value != key:
                this_node = this_node.next
            if this_node.value == key:
                self.lru_list.move_to_end(this_node)
                return self.lru_dict[key]
            else:
                return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        self.lru_dict[key] = value
        this_node = self.lru_list.head
        if this_node:
            while this_node.next is not None and this_node.value != key:
                this_node = this_node.next
            if this_node.value == key:
                self.lru_list.move_to_end(this_node)
                return
        self.lru_list.add_to_tail(key)
        if self.lru_list.length > self.limit:
            del self.lru_dict[self.lru_list.head.value]
            self.lru_list.remove_from_head()