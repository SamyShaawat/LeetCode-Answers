class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tasks = SortedSet()
        self.task_to_users = {}
        self.task_to_priority = {}
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks.add((priority, taskId, userId))
        self.task_to_users[taskId] = userId
        self.task_to_priority[taskId] = priority
    def edit(self, taskId: int, newPriority: int) -> None:
        user = self.task_to_users[taskId]
        self.rmv(taskId)
        self.add(user, taskId, newPriority)        
    def rmv(self, taskId: int) -> None:
        user = self.task_to_users[taskId]        
        priority = self.task_to_priority[taskId]
        self.tasks.remove((priority, taskId, user))
        del self.task_to_users[taskId]
        del self.task_to_priority[taskId]
    def execTop(self) -> int:
        if not self.tasks:
            return -1
        _, task_id, user_id = self.tasks[-1]
        self.rmv(task_id)
        return user_id

