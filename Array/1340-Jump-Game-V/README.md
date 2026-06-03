# 1340. Jump Game V


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-v/)


## 📝 Problem Description

Given an array of integers `arr` and an integer `d`. In one step you can jump from index `i` to index:

	- `i + x` where: `i + x < arr.length` and ` 0 < x <= d`.

	- `i - x` where: `i - x >= 0` and ` 0 < x <= d`.

In addition, you can only jump from index `i` to index `j` if `arr[i] > arr[j]` and `arr[i] > arr[k]` for all indices `k` between `i` and `j` (More formally `min(i, j) < k < max(i, j)`).

You can choose any index of the array and start jumping. Return *the maximum number of indices* you can visit.

Notice that you can not jump outside of the array at any time.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/01/23/meta-chart.jpeg)
```

**Input:** arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
**Output:** 4
**Explanation:** You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

```

Example 2:**

```

**Input:** arr = [3,3,3,3,3], d = 3
**Output:** 1
**Explanation:** You can start at any index. You always cannot jump to any index.

```

Example 3:**

```

**Input:** arr = [7,6,5,4,3,2,1], d = 1
**Output:** 7
**Explanation:** Start at index 0. You can visit all the indicies. 

```

 

**Constraints:**

	- `1 <= arr.length <= 1000`

	- `1 <= arr[i] <= 10^5`

	- `1 <= d <= arr.length`

## 🧠 Solution Explanation

**Intuition**
This problem can be solved using a depth-first search (DFS) approach, where we start from each index and explore all possible jumps within the given distance `d`. We keep track of the maximum number of indices we can visit from each starting index.

**Approach**
1. Initialize a memoization dictionary `memo` to store the maximum number of indices we can visit from each index.
2. Define a recursive DFS function `dfs(idx)` that takes an index `idx` as input.
3. If the result for `idx` is already stored in `memo`, return the stored value.
4. Initialize a variable `curr` to store the maximum number of indices we can visit from `idx`.
5. Explore all possible left jumps from `idx` by iterating from `1` to `d` and checking if the jump is within the array bounds and if `arr[idx] > arr[left]`. If the jump is valid, recursively call `dfs(left)` and update `curr` with the maximum value.
6. Explore all possible right jumps from `idx` by iterating from `1` to `d` and checking if the jump is within the array bounds and if `arr[idx] > arr[right]`. If the jump is valid, recursively call `dfs(right)` and update `curr` with the maximum value.
7. Store the result `1 + curr` in `memo[idx]` and return it.
8. Initialize a variable `res` to store the maximum number of indices we can visit from any starting index.
9. Iterate over all indices in the array and call `dfs(i)` to update `res` with the maximum value.

**Time Complexity**
O(n * d * log(n)), where n is the length of the array and d is the given distance. This is because in the worst case, we may need to explore all possible jumps from each index, resulting in a time complexity of O(n * d). Additionally, the recursive DFS function may need to explore the entire array, resulting in a time complexity of O(log(n)) due to the binary search-like behavior of the DFS.

**Space Complexity**
O(n), where n is the length of the array. This is because we need to store the maximum number of indices we can visit from each index in the memoization dictionary.

**Key Insight**
The key insight here is to use a DFS approach to explore all possible jumps from each index, while keeping track of the maximum number of indices we can visit from each starting index. This allows us to efficiently find the maximum number of indices we can visit from any starting index.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 291 ms (Beats 26.81%) |
| 💾 Memory | 24 MB (Beats 39.48%) |
| 📅 Solved | 2026-05-24 |
| 💻 Language | Python |