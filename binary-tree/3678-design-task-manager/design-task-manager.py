class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.task_heap = []
        for user, task, priority in tasks:
            self.task_map[task] = [priority, user, 1]
            heapq.heappush(self.task_heap, [- priority, -task])
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = [priority, userId, 1]
        heapq.heappush(self.task_heap, [-priority, -taskId])
        

    def edit(self, taskId: int, newPriority: int) -> None:
        # cur = self.task_map[taskId]
        self.task_map[taskId][0] = newPriority
        heapq.heappush(self.task_heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        # cur = self.task_map[taskId]
        self.task_map[taskId][2] = 0
        

    def execTop(self) -> int:
        heap = self.task_heap
        mp = self.task_map
        while heap:
            if -heap[0][1] in mp and - heap[0][0] == mp[-heap[0][1]][0] and mp[-heap[0][1]][2] == 1:
                pop = heapq.heappop(heap)
                userId = mp[-pop[1]][1]
                del mp[-pop[1]]
                return userId
            heapq.heappop(heap)
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()