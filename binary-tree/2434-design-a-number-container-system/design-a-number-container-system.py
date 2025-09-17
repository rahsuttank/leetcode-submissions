class NumberContainers:

    def __init__(self):
        self.num_heaps = defaultdict(list)
        self.idx_num = {}

        

    def change(self, index: int, number: int) -> None:
        heapq.heappush(self.num_heaps[number], index)
        self.idx_num[index] = number
        

    def find(self, number: int) -> int:
        heap = self.num_heaps[number]
        if not heap:
            return -1
        while heap:
            if self.idx_num[heap[0]] == number:
                return heap[0]
            heapq.heappop(heap)
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)