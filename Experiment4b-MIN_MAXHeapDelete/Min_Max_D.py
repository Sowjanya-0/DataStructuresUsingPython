class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
            
    def sift_up_max(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
                    
    def insert_min(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)
        
    def insert_max(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)
        self.sift_up_max(self.current_size)
 
    def sift_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
    
    def print_heap(self):
        for i in self.heap_list:
            if i==0:
                continue
            print(i)
        
    def delete_min(self):
        if len(self.heap_list) == 1:
            return 'Empty heap'
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        *self.heap_list, _ = self.heap_list
        self.current_size -= 1
        self.sift_down(1)
        return root
    
    def max_child(self, i):
        if (i * 2)+1 > self.current_size:
            return (i * 2)
        else:
            if self.heap_list[i*2] > self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
    
    
    def sift_down_max(self, i):
        while (i * 2+1) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
    
    def delete_max(self):
        if len(self.heap_list) == 1:
            return 'Empty heap'
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        *self.heap_list, _ = self.heap_list
        self.current_size -= 1
        self.sift_down_max(1)
        return root

my_heap = Heap()
my_heap.insert_min(5)
my_heap.insert_min(6)
my_heap.insert_min(7)
my_heap.insert_min(9)
my_heap.insert_min(13)
my_heap.insert_min(11)
my_heap.insert_min(10)
print("Min Heap Order:")
print(my_heap.print_heap())
print("Delete the min node in the heap list which is ")
print(my_heap.delete_min()) # removing min node i.e 5
print("After deletion in Min Heap tree: ")
print(my_heap.print_heap())
my_heap1 = Heap()
my_heap1.insert_max(5)
my_heap1.insert_max(6)
my_heap1.insert_max(7)
my_heap1.insert_max(9)
my_heap1.insert_max(13)
my_heap1.insert_max(11)
my_heap1.insert_max(10)
print("Max Heap Order:")
print(my_heap1.print_heap())
print("Delete the max node in the heap list which is ")
print(my_heap1.delete_max()) # removing min node i.e 5
print("After deletion in Max Heap tree: ")
print(my_heap1.print_heap())

 