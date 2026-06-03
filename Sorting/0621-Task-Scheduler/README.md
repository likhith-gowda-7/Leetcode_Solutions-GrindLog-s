> 📌 **Cross-listed:** Primary location is [Array/0621-Task-Scheduler](../../Array/0621-Task-Scheduler). This problem also appears under: **Array**, **Hash Table**, **Greedy**, **Sorting**, **Heap (Priority Queue)**, **Counting**

# 621. Task Scheduler


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/task-scheduler/)


## 📝 Problem Description

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.

Return the **minimum** number of CPU intervals required to complete all tasks.

 

Example 1:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 2

**Output:** 8

**Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3^rd interval, neither A nor B can be done, so you idle. By the 4^th interval, you can do A again as 2 intervals have passed.

Example 2:**

**Input:** tasks = ["A","C","A","B","D","B"], n = 1

**Output:** 6

**Explanation:** A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:**

**Input:** tasks = ["A","A","A", "B","B","B"], n = 3

**Output:** 10

**Explanation:** A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

**Constraints:**

	- `1 <= tasks.length <= 10^4`

	- `tasks[i]` is an uppercase English letter.

	- `0 <= n <= 100`

## 🧠 Solution Explanation

**Intuition**
This solution works by maintaining a priority queue (max heap) of the most frequent tasks and a queue (q) of tasks that are available to be executed. The idea is to execute tasks in a way that maximizes the usage of CPU intervals, ensuring that there is at least a gap of `n` intervals between two tasks with the same label.

**Approach**
1. Count the frequency of each task using a hash map `h1`.
2. Create a max heap `max_heap` with the negative frequencies of the most frequent tasks.
3. Initialize a queue `q` to store tasks that are available to be executed.
4. While the max heap or queue is not empty, do the following:
   - Increment the time by 1.
   - If the max heap is not empty, pop the task with the highest frequency and increment its frequency by 1. If the frequency is not 0, add it to the queue with its next available time.
   - If the queue is not empty and the task at the top of the queue is available to be executed (i.e., its next available time is equal to the current time), remove it from the queue and push it back into the max heap.
5. Return the time when all tasks have been executed.

**Time Complexity**
O(m log m), where m is the number of unique tasks. This is because we are using a max heap to store the most frequent tasks, and each insertion and deletion operation takes O(log m) time.

**Space Complexity**
O(m), where m is the number of unique tasks. This is because we are using a hash map to count the frequency of each task and a queue to store tasks that are available to be executed.

**Key Insight**
The key insight here is to use a priority queue (max heap) to store the most frequent tasks and a queue to store tasks that are available to be executed. This allows us to execute tasks in a way that maximizes the usage of CPU intervals, ensuring that there is at least a gap of `n` intervals between two tasks with the same label.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 148 ms (Beats 50.4%) |
| 💾 Memory | 19.2 MB (Beats 100%) |
| 📅 Solved | 2025-07-08 |
| 💻 Language | Python |