# 3408. Design Task Manager


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Ordered Set](https://img.shields.io/badge/Ordered%20Set-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/design-task-manager/)


## 📝 Problem Description

There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the `TaskManager` class:

	- 
	`TaskManager(vector<vector<int>>& tasks)` initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form `[userId, taskId, priority]`, which adds a task to the specified user with the given priority.

	

	- 
	`void add(int userId, int taskId, int priority)` adds a task with the specified `taskId` and `priority` to the user with `userId`. It is **guaranteed** that `taskId` does not *exist* in the system.

	

	- 
	`void edit(int taskId, int newPriority)` updates the priority of the existing `taskId` to `newPriority`. It is **guaranteed** that `taskId` *exists* in the system.

	

	- 
	`void rmv(int taskId)` removes the task identified by `taskId` from the system. It is **guaranteed** that `taskId` *exists* in the system.

	

	- 
	`int execTop()` executes the task with the **highest** priority across all users. If there are multiple tasks with the same **highest** priority, execute the one with the highest `taskId`. After executing, the** **`taskId`** **is **removed** from the system. Return the `userId` associated with the executed task. If no tasks are available, return -1.

	

**Note** that a user may be assigned multiple tasks.

 

Example 1:**

**Input:**

["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]

[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

**Output:**

[null, null, null, 3, null, null, 5] 

**Explanation**

TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.

taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.

taskManager.edit(102, 8); // Updates priority of task 102 to 8.

taskManager.execTop(); // return 3. Executes task 103 for User 3.

taskManager.rmv(101); // Removes task 101 from the system.

taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.

taskManager.execTop(); // return 5. Executes task 105 for User 5.

 

**Constraints:**

	- `1 <= tasks.length <= 10^5`

	- `0 <= userId <= 10^5`

	- `0 <= taskId <= 10^5`

	- `0 <= priority <= 10^9`

	- `0 <= newPriority <= 10^9`

	- At most `2 * 10^5` calls will be made in **total** to `add`, `edit`, `rmv`, and `execTop` methods.

	- The input is generated such that `taskId` will be valid.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a combination of hash tables and heaps to efficiently manage tasks with varying priorities. The hash table stores tasks with their corresponding priorities and users, while the heap maintains a sorted list of tasks across all users. This design allows for efficient addition, modification, and removal of tasks, as well as execution of the highest-priority task.

**Approach**
1. In the `__init__` method, initialize the task map and tasks heap. Iterate through the input tasks, adding each task to the task map and the tasks heap.
2. In the `add` method, add the new task to the task map and the tasks heap.
3. In the `edit` method, update the priority of the existing task in the task map and push the updated task to the tasks heap.
4. In the `rmv` method, remove the task from the task map.
5. In the `execTop` method, pop tasks from the tasks heap until the highest-priority task is found. Return the user ID associated with the task.

**Time Complexity**
- `__init__`: O(n log n) due to heapification of the tasks heap.
- `add`, `edit`, `rmv`: O(log n) due to heap operations.
- `execTop`: O(n log n) in the worst case, where n is the number of tasks.

**Space Complexity**
O(n), where n is the number of tasks, to store the task map and tasks heap.

**Key Insight**
The key insight is the use of a single heap to maintain a sorted list of tasks across all users, allowing for efficient execution of the highest-priority task. This design choice enables the solution to handle addition, modification, and removal of tasks efficiently, while also supporting the execution of the highest-priority task.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 607 ms (Beats 24.5%) |
| 💾 Memory | 104.8 MB (Beats 54.15%) |
| 📅 Solved | 2025-09-18 |
| 💻 Language | Python |