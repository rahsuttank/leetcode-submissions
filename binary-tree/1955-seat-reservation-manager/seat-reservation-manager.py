class SeatManager:

    def __init__(self, n: int):
        self.reserve_heap = []
        for i in range(n):
            self.reserve_heap.append([0, i])
        

    def reserve(self) -> int:
        _, seat = heapq.heappop(self.reserve_heap)
        # heapq.heappush(self.reserve_heap, [1, seat])
        return seat+1


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.reserve_heap, [0, seatNumber-1])
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)