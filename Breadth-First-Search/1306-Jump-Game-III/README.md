> 📌 **Cross-listed:** Primary location is [Array/1306-Jump-Game-III](../../Array/1306-Jump-Game-III). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**

# 1306. Jump Game III


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-iii/)


## 📝 Problem Description

Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach **any** index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:**

```

**Input:** arr = [4,2,3,0,3,1,2], start = 5
**Output:** true
**Explanation:** 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

```

Example 2:**

```

**Input:** arr = [4,2,3,0,3,1,2], start = 0
**Output:** true 
**Explanation: 
**One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

```

Example 3:**

```

**Input:** arr = [3,0,2,1,2], start = 2
**Output:** false
**Explanation: **There is no way to reach at index 1 with value 0.

```

 

**Constraints:**

	- `1 <= arr.length <= 5 * 10^4`

	- `0 <= arr[i] < arr.length`

	- `0 <= start < arr.length`

## 🧠 Solution Explanation

**Intuition**
The solution uses a breadth-first search (BFS) approach to explore all possible indices that can be reached from the starting index. The key insight is that we can use a queue to keep track of the indices to visit next, and by marking the visited indices with a special character (`#`), we can avoid revisiting them.

**Approach**
1. Initialize a queue with the starting index.
2. While the queue is not empty, pop the next index from the queue.
3. If the current index has already been visited (marked with `#`), skip it.
4. If the current index has a value of 0, return True (we have reached a target index).
5. Mark the current index with `#` to avoid revisiting it.
6. For each possible jump (forward and backward) from the current index, calculate the next index.
7. If the next index is within the bounds of the array and has not been visited, add it to the queue.
8. If the queue becomes empty and no target index has been reached, return False.

**Time Complexity**
O(n), where n is the length of the array. This is because we visit each index at most once, and the time complexity of the BFS algorithm is linear.

**Space Complexity**
O(n), where n is the length of the array. This is because in the worst case, we need to store all indices in the queue.

**Key Insight**
The key to this solution is the use of a queue to keep track of the indices to visit next, and by marking the visited indices with a special character (`#`), we can avoid revisiting them. This allows us to efficiently explore all possible indices and find a path to a target index with value 0.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 54.4%) |
| 💾 Memory | 25.1 MB (Beats 96.96%) |
| 📅 Solved | 2026-05-17 |
| 💻 Language | Python |