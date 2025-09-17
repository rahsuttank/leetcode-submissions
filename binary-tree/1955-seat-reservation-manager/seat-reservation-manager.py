class SeatManager:

    def __init__(self, n: int):
        self.reserve_heap = []
        for i in range(1, n+1):
            self.reserve_heap.append(i)
        

    def reserve(self) -> int:
        seat = heapq.heappop(self.reserve_heap)
        return seat


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.reserve_heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)