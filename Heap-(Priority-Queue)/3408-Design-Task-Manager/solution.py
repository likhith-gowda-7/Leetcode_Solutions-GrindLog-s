class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        #we map task -> priority,user
        self.task_map={}
        #this holds tasks of all users in a single heap
        self.tasks=list()
        for u_id,t_id,prior in tasks:
            self.task_map[t_id]=[-prior,u_id]
            self.tasks.append((-prior,-t_id))
        heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        #add the new task to the task's map
        self.task_map[taskId]=[-priority,userId]
        #add the new entry to the user's task's heap
        heappush(self.tasks,(-priority,-taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        #we'll do a lazy deletion
        self.task_map[taskId][0]=-newPriority
        heappush(self.tasks,(-newPriority,-taskId))

    def rmv(self, taskId: int) -> None:
        del self.task_map[taskId]

    def execTop(self) -> int:
        heap=self.tasks
        while heap:
            val = heap[0]
            task_id = -val[1]
            if task_id in self.task_map and self.task_map[task_id][0] == val[0]:
                break
            heappop(heap)

        if not heap:
            return -1
        _,task_id=heap[0]
        user_id=self.task_map[-task_id][1]
        del self.task_map[-task_id]
        heappop(self.tasks)
        return user_id

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()