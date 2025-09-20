class Router:

    def __init__(self, memoryLimit: int):
        self.router = deque()
        self.table = set()
        self.limit = memoryLimit
        self.destMap = defaultdict(deque)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        t = (source, destination, timestamp)
        if t in self.table:
            return False
        self.table.add(t)
        self.router.append(t)
        self.destMap[destination].append(timestamp)
        if len(self.router) > self.limit:
            t = self.router.popleft()
            self.table.remove(t)
            self.destMap[t[1]].popleft()
        return True
            
        

    def forwardPacket(self) -> List[int]:
        if self.router:
            t = self.router.popleft()
            self.table.remove(t)
            self.destMap[t[1]].popleft()
            return list(t)
        else:
            return []
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destMap:
            return 0
        high = 0
        low = 0
        arr = self.destMap[destination]
        l, r = 0, len(arr)
        while l < r:
            m = (l+r) // 2
            if arr[m] < startTime:
                l = m + 1
            else:
                r = m
        low = l
        l= 0
        r = len(arr)
        while l < r:
            m = (l+r) // 2
            if arr[m] > endTime:
                r = m
            else:
                l = m + 1
                

        return l - low

        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)