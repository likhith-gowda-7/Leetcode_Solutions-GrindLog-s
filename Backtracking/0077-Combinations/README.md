# 77. Combinations


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/combinations/)


## 📝 Problem Description

Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`.

You may return the answer in **any order**.

 

Example 1:**

```

**Input:** n = 4, k = 2
**Output:** [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
**Explanation:** There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

```

Example 2:**

```

**Input:** n = 1, k = 1
**Output:** [[1]]
**Explanation:** There is 1 choose 1 = 1 total combination.

```

 

**Constraints:**

	- `1 <= n <= 20`

	- `1 <= k <= n`

## 🧠 Solution Explanation

**Intuition**
The solution uses a backtracking approach to generate all possible combinations of `k` numbers chosen from the range `[1, n]`. The key insight is to use a recursive function that adds elements to the current combination and then recursively generates all combinations of the remaining elements.

**Approach**
1. Initialize an empty list `res` to store all combinations and a temporary list `sol` to store the current combination.
2. Define a recursive function `backtrack` that takes a `start` index as an argument.
3. If the length of the current combination `sol` is equal to `k`, append a copy of `sol` to `res` and return.
4. Calculate the number of elements still needed for the current combination (`still_need`) and the number of choices available from the `start` index to `n` (`choices`).
5. If there are enough choices available, iterate from `start` to `n` and recursively call `backtrack` with the next index (`i+1`) after adding each element to the current combination.
6. After each recursive call, remove the last element from the current combination to backtrack and explore other branches.
7. Call `backtrack` with the initial `start` index of 1.

**Time Complexity**
The time complexity is O(n choose k) = O(n! / (k!(n-k)!)), which is the number of possible combinations. This is because each combination is generated exactly once, and the recursive function explores all possible branches.

**Space Complexity**
The space complexity is O(n choose k) = O(n! / (k!(n-k)!)), which is the maximum depth of the recursion tree. This is because each recursive call adds a new branch to the tree, and the maximum depth is equal to the number of combinations.

**Key Insight**
The key insight is to use a recursive function that adds elements to the current combination and then recursively generates all combinations of the remaining elements. This approach allows us to explore all possible branches of the combination tree and generate all possible combinations of `k` numbers chosen from the range `[1, n]`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 123 ms (Beats 27.39%) |
| 💾 Memory | 59.8 MB (Beats 97.62%) |
| 📅 Solved | 2025-07-22 |
| 💻 Language | Python |