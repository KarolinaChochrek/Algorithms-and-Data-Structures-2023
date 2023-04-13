# skończone

class Element:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __gt__(self, other):
        return self.priority > other.priority

    def __str__(self):
        return f"{self.priority} : {self.data}"

    def __repr__(self):
        return f"{self.priority} : {self.data}"


class Heap:
    def __init__(self):
        self.queue = []

    @property
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return not bool(self.queue)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

    def dequeue(self):
        if not self.queue:
            return None
        elementToDequeue = self.queue[0]
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        self.queue = self.queue[:-1]

        self.heapify_down(0)
        return elementToDequeue

    def heapify_down(self, parent: int):
        left = self.left(parent)
        right = self.right(parent)
        largest = parent

        if left <= self.size - 1 and self.queue[left] > self.queue[largest]:
            largest = left

        if right <= self.size - 1 and self.queue[right] > self.queue[largest]:
            largest = right

        if largest != parent:
            self.queue[parent], self.queue[largest] = self.queue[largest], self.queue[parent]
            self.heapify_down(largest)

    def enqueue(self, element: Element):
        self.queue.append(element)  
        childIdx = self.size - 1  

        while childIdx > 0 and self.queue[self.parent(childIdx)] < self.queue[childIdx]:
            self.queue[childIdx], self.queue[self.parent(childIdx)] = self.queue[self.parent(childIdx)], self.queue[childIdx]
            childIdx = self.parent(childIdx)
            
    def right(self, idxOfParent):
        return 2 * idxOfParent + 2

    def left(self, idxOfParent):
        return 2 * idxOfParent + 1

    def parent(self, idxOfChild):
        return (idxOfChild - 1) // 2

    def print_tab(self):
        if self.is_empty():
            print("{ }")
            return
        print('{', end=' ')
        for i in range(self.size - 1):
            print(self.queue[i], end=', ')
        if self.queue[self.size - 1]:
            print(self.queue[self.size - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.queue[idx] if self.queue[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


if __name__ == '__main__':
    listOfPriorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    word = "GRYMOTYLA"
    queue = Heap()

    for idx in range(len(listOfPriorities)):
        queue.enqueue(Element(word[idx], listOfPriorities[idx]))
    queue.print_tree(0, 0)
    queue.print_tab()
    first = queue.dequeue()
    print(queue.peek())
    queue.print_tab()
    print(first)
    while queue:
        el = queue.dequeue()
        if el is None:
            break
        print(el)
    queue.print_tab()