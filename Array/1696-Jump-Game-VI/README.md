# 1696. Jump Game VI


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-vi/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` and an integer `k`.

You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. That is, you can jump from index `i` to any index in the range `[i + 1, min(n - 1, i + k)]` **inclusive**.

You want to reach the last index of the array (index `n - 1`). Your **score** is the **sum** of all `nums[j]` for each index `j` you visited in the array.

Return *the **maximum score** you can get*.

 

Example 1:**

```

**Input:** nums = [1,-1,-2,4,-7,3], k = 2
**Output:** 7
**Explanation:** You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

```

Example 2:**

```

**Input:** nums = [10,-5,-2,4,0,3], k = 3
**Output:** 17
**Explanation:** You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

```

Example 3:**

```

**Input:** nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length, k <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The problem is a variation of the classic "Jump Game" problem, but with a twist: we need to maximize the sum of visited indices. The key insight is to use a priority queue (deque in Python) to keep track of the indices with the maximum sum. By maintaining a sliding window of the maximum sum, we can efficiently explore all possible jumps and find the optimal solution.

**Approach**
1. Initialize a deque `maxi` with the starting index `0` and a variable `res` to store the maximum sum.
2. Iterate through the array `nums` from index `1` to `n-1`.
3. For each index `r`, update the maximum sum `res` by adding the sum of the current index and the maximum sum at the previous index `maxi[0]`.
4. Update the value at index `r` in `nums` to store the maximum sum `res`.
5. Use a while loop to remove indices from the end of `maxi` if their sum is less than the sum at index `r`.
6. Add index `r` to the end of `maxi`.
7. If the index at the front of `maxi` is out of the sliding window, remove it from the front of `maxi`.
8. Return the maximum sum `res` after iterating through all indices.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we iterate through the array once and perform constant-time operations for each index.

**Space Complexity**
O(n), where n is the length of the array `nums`. This is because in the worst case, we need to store all indices in the deque `maxi`.

**Key Insight**
The key insight is to use a priority queue (deque) to maintain a sliding window of the maximum sum. By efficiently exploring all possible jumps and keeping track of the maximum sum, we can find the optimal solution in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 121 ms (Beats 86.68%) |
| 💾 Memory | 29.3 MB (Beats 100%) |
| 📅 Solved | 2025-03-28 |
| 💻 Language | Python |