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
        while self.task_heap:
            priority, taskId = self.task_heap[0]
            taskId, priority = -taskId, -priority
            if (taskId in self.task_map and 
                self.task_map[taskId][0] == priority and 
                self.task_map[taskId][2] == 1):
                heapq.heappop(self.task_heap)
                userId = self.task_map[taskId][1]
                del self.task_map[taskId]   # remove after execution
                return userId
            heapq.heappop(self.task_heap)  # discard stale entry
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()