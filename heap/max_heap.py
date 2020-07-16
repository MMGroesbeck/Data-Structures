class Heap:
    def __init__(self):
        self.storage = []
    
    def get_parent(self, index):
        if index == 0:
            return None
        else:
            return ((index + (index % 2)) / 2) - 1
    
    def swap(self, x, y):
        val = self.storage[x]
        self.storage[x] = self.storage[y]
        self.storage[y] = val

    def insert(self, value):
        self.storage.append(value)
        bubbler = self._bubble_up(len(self.storage)-1)
        while bubbler:
            bubbler = self._bubble_up(bubbler)

    def delete(self):
        # index = 0
        # while index*2 + 1 < len(self.storage):
        #     if self.storage[index*2 + 1] > self.storage[index*2 + 2]:
        #         child_ind = index*2 + 1
        #     else:
        #         child_ind = index*2 + 2
        #     self.swap(index, child_ind)
        #     index = child_ind
        # if index*2 + 2 == len(self.storage):
        #     self.swap(index, index*2 + 1)
        # self.storage.pop()
        pass
        
    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = self.get_parent(index)
        if self.storage[index] > self.storage[parent]:
            self.swap(index, parent)
            return parent
        else:
            return False

    def _sift_down(self, index):
        if self.storage[index*2 + 1] > self.storage[index*2 + 2]:
            child_ind = index*2 + 1
            child_val = self.storage[index*2 + 1]
        else:
            child_ind = index*2 + 2
            child_val = self.storage[index*2 + 2]
        if child_val > self.storage[index]:
            self.swap(index, child_ind)
            return child_ind
        else:
            return False