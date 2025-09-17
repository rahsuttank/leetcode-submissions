class SeatManager:

    def __init__(self, n: int):
        # self.n = n
        self.prev = 0
        self.pq = []
    def reserve(self) -> int:
        if self.pq and self.pq[0] < self.prev + 1:
            smallest = heappop(self.pq)
        else:
            smallest = self.prev + 1
            self.prev += 1
        return smallest

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.pq, seatNumber)
        