# 45. Jump Game II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-ii/)


## 📝 Problem Description

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at index 0.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at index `i`, you can jump to any index `(i + j)` where:

	- `0 <= j <= nums[i]` and

	- `i + j < n`

Return *the minimum number of jumps to reach index *`n - 1`. The test cases are generated such that you can reach index `n - 1`.

 

Example 1:**

```

**Input:** nums = [2,3,1,1,4]
**Output:** 2
**Explanation:** The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

Example 2:**

```

**Input:** nums = [2,3,0,1,4]
**Output:** 2

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `0 <= nums[i] <= 1000`

	- It's guaranteed that you can reach `nums[n - 1]`.

## 🧠 Solution Explanation

## Intuition
This approach works by maintaining a sliding window of reachable indices and iteratively expanding it until the last index is reached. The key idea is to keep track of the farthest reachable index from the current window, which allows us to minimize the number of jumps. By doing so, we ensure that we always make the most progress towards the last index in each jump.

## Approach
1. Initialize the left and right boundaries of the window to 1 and the value of the first element in the array, respectively.
2. Initialize the result (minimum number of jumps) to 1.
3. While the right boundary is less than the last index, find the farthest reachable index from the current window.
4. Update the left and right boundaries of the window to the next position after the current right boundary and the farthest reachable index, respectively.
5. Increment the result by 1 for each expansion of the window.

## Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because we are potentially visiting each element in the array once during the iteration.

## Space Complexity
The space complexity is O(1), which means the space required does not change with the size of the input array. This is because we are only using a constant amount of space to store the boundaries of the window and the result.

## Key Insight
The key insight here is to recognize that the farthest reachable index from the current window can be used to minimize the number of jumps. By keeping track of this index and expanding the window accordingly, we can ensure that we always make the most progress towards the last index in each jump, resulting in the minimum number of jumps.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 89.48%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-02-14 |
| 💻 Language | Python |