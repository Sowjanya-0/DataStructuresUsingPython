class Heap_Array(object):
    heap_type = 'MaxHeap'

    def __init__(self, capacity=20):
        self.arr = [None for x in range(capacity)]
        self.count = 0
        self.capacity = capacity

    def parent_node(self, i):
        if i < 0 or i > self.count:
            return False
        return int((i-1)/2)

    def left_child(self, i):
        left = 2*i+1
        return False if left >= self.count else left

    def right_child(self, i):
        right = 2*i+2
        return False if right >= self.count else right

    def insert(self, key):
        if self.count < self.capacity:
            self.arr[self.count] = key
            self.heapify_up(self.count)
            self.count += 1


    def print_heap(self):
        print(', '.join([str(x) for x in self.arr[:self.count]]))

    def heapify_down(self, parent):
        
        left = self.left_child(parent)
        right = self.right_child(parent)

        if left and self.arr[left] > self.arr[parent]:
            max_ = left
        else:
            max_ = parent
        if right and self.arr[right] > self.arr[max_]:
            max_ = right

        if max_ != parent:
            self.arr[parent], self.arr[max_] = self.arr[max_], self.arr[parent]

            self.heapify_down(max_)
    
    def heapify_down_min(self, parent):
        
        left = self.left_child(parent)
        right = self.right_child(parent)

        if left and self.arr[left] < self.arr[parent]:
            min_ = left
        else:
            min_ = parent
        if right and self.arr[right] < self.arr[min_]:
            min_ = right

        if min_ != parent:
            self.arr[parent], self.arr[min_] = self.arr[min_], self.arr[parent]

            self.heapify_down(min_)


    def heapify_up(self, child):
        parent = self.parent_node(child)

        if self.arr[parent] < self.arr[child]:
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            self.heapify_up(parent)

    def search_max(self):
        if self.count ==0 :
            print('__ Heap is Empty !__')
            return
        max_data = self.arr[0]
        self.arr[0] = self.arr[self.count-1]
        self.arr[self.count-1] = None
        self.count -= 1
        self.heapify_down(0)
        return max_data
    
    def search_min(self):
        if self.count ==0 :
            print('__ Heap is Empty !__')
            return
        min_data = self.arr[self.count-1]
        self.arr[0] = self.arr[self.count-1]
        self.arr[self.count-1] = None
        self.count -= 1
        self.heapify_down_min(0)
        return self.arr[0]


if __name__ == '__main__':
    heap_arr = Heap_Array()
    for i in range(1,10):
        heap_arr.insert(i)
    heap_arr.print_heap()

    print("MAX HEAP ORDER")
    heap_arr.print_heap()
    print('Search Max :', heap_arr.search_max())
    
    print("MIN HEAP ORDER")
    heap_arr.print_heap()
    print('Search Min :', heap_arr.search_min())
    