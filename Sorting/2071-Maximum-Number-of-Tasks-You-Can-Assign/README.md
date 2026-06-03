> 📌 **Cross-listed:** Primary location is [Array/2071-Maximum-Number-of-Tasks-You-Can-Assign](../../Array/2071-Maximum-Number-of-Tasks-You-Can-Assign). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Greedy**, **Queue**, **Sorting**, **Monotonic Queue**

# 2071. Maximum Number of Tasks You Can Assign


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/)


## 📝 Problem Description

You have `n` tasks and `m` workers. Each task has a strength requirement stored in a **0-indexed** integer array `tasks`, with the `i^th` task requiring `tasks[i]` strength to complete. The strength of each worker is stored in a **0-indexed** integer array `workers`, with the `j^th` worker having `workers[j]` strength. Each worker can only be assigned to a **single** task and must have a strength **greater than or equal** to the task's strength requirement (i.e., `workers[j] >= tasks[i]`).

Additionally, you have `pills` magical pills that will **increase a worker's strength** by `strength`. You can decide which workers receive the magical pills, however, you may only give each worker **at most one** magical pill.

Given the **0-indexed **integer arrays `tasks` and `workers` and the integers `pills` and `strength`, return *the **maximum** number of tasks that can be completed.*

 

Example 1:**

```

**Input:** tasks = [**3**,**2**,**1**], workers = [**0**,**3**,**3**], pills = 1, strength = 1
**Output:** 3
**Explanation:**
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)

```

Example 2:**

```

**Input:** tasks = [**5**,4], workers = [**0**,0,0], pills = 1, strength = 5
**Output:** 1
**Explanation:**
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)

```

Example 3:**

```

**Input:** tasks = [**10**,**15**,30], workers = [**0**,**10**,10,10,10], pills = 3, strength = 10
**Output:** 2
**Explanation:**
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.

```

 

**Constraints:**

	- `n == tasks.length`

	- `m == workers.length`

	- `1 <= n, m <= 5 * 10^4`

	- `0 <= pills <= m`

	- `0 <= tasks[i], workers[j], strength <= 10^9`

## 🧠 Solution Explanation

**Intuition**
This solution uses a binary search approach to find the maximum number of tasks that can be assigned to workers, given the constraints of magical pills and worker strength. The key insight is to consider the workers with the highest strength first, and then use the pills to increase the strength of weaker workers as needed.

**Approach**
1. Define a helper function `canAssign` to check if it's possible to assign `mid` tasks to workers with the given constraints.
2. Sort the `tasks` and `workers` arrays in ascending order.
3. Initialize the binary search range `[l, r]` to `[0, min(len(tasks), len(workers))]`.
4. Perform binary search to find the maximum number of tasks that can be assigned.
5. In each iteration, call `canAssign` with the mid value and update the answer if it's possible to assign `mid` tasks.
6. If `canAssign` returns `True`, update the answer and move the left pointer to `mid + 1`. Otherwise, move the right pointer to `mid - 1`.

**Time Complexity**
O(n log n + m log m + k log k), where n is the number of tasks, m is the number of workers, and k is the number of workers that need to be increased in strength using magical pills. This is because we perform binary search, sorting, and bisect operations.

**Space Complexity**
O(1), excluding the space required for input arrays. We only use a constant amount of space to store the binary search variables and the answer.

**Key Insight**
The key insight is to use the workers with the highest strength first and then use the pills to increase the strength of weaker workers as needed. This approach allows us to efficiently find the maximum number of tasks that can be assigned, given the constraints of magical pills and worker strength.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 26.8 MB (Beats 100%) |
| 📅 Solved | 2025-05-02 |
| 💻 Language | Python |