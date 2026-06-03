# 1345. Jump Game IV


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-iv/)


## 📝 Problem Description

Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to index:

	- `i + 1` where: `i + 1 < arr.length`.

	- `i - 1` where: `i - 1 >= 0`.

	- `j` where: `arr[i] == arr[j]` and `i != j`.

Return *the minimum number of steps* to reach the **last index** of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:**

```

**Input:** arr = [100,-23,-23,404,100,23,23,23,3,404]
**Output:** 3
**Explanation:** You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

```

Example 2:**

```

**Input:** arr = [7]
**Output:** 0
**Explanation:** Start index is the last index. You do not need to jump.

```

Example 3:**

```

**Input:** arr = [7,6,9,6,9,6,9,7]
**Output:** 1
**Explanation:** You can jump directly from index 0 to index 7 which is last index of the array.

```

 

**Constraints:**

	- `1 <= arr.length <= 5 * 10^4`

	- `-10^8 <= arr[i] <= 10^8`

## 🧠 Solution Explanation

**Intuition**
This solution uses a combination of a queue (BFS) and a hash table to efficiently traverse the array and find the minimum number of jumps to reach the last index. By utilizing the fact that we can jump to indices with the same value, we can explore multiple paths simultaneously.

**Approach**
1. Create a hash table `h1` to store the indices of elements with the same value.
2. Initialize a queue `q` with the starting index and a jump count of 0.
3. Initialize a seen array to keep track of visited indices.
4. While the queue is not empty, pop an index and its corresponding jump count.
5. If the next index (or previous index if we're at the start) is within bounds and not seen before, add it to the queue and mark it as seen.
6. If the current index has elements with the same value in the hash table, pop the indices from the hash table and add them to the queue if they're not seen before.
7. If we reach the last index, return the current jump count plus one.

**Time Complexity**
O(n) - We visit each index at most twice (once in the queue and once in the hash table), resulting in a linear time complexity.

**Space Complexity**
O(n) - We use a seen array of size n and a hash table that can store up to n elements, resulting in a linear space complexity.

**Key Insight**
The key insight is to utilize the fact that we can jump to indices with the same value, allowing us to explore multiple paths simultaneously. By using a queue and a hash table, we can efficiently traverse the array and find the minimum number of jumps to reach the last index.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 127 ms (Beats 86.34%) |
| 💾 Memory | 33.1 MB (Beats 72.76%) |
| 📅 Solved | 2026-05-18 |
| 💻 Language | Python |