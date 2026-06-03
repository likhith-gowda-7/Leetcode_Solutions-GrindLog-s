# 198. House Robber


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/house-robber/)


## 📝 Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

 

Example 1:**

```

**Input:** nums = [1,2,3,1]
**Output:** 4
**Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

Example 2:**

```

**Input:** nums = [2,7,9,3,1]
**Output:** 12
**Explanation:** Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 400`

## 🧠 Solution Explanation

### Intuition
This solution works by using a dynamic programming approach to consider all possible combinations of houses to rob, while avoiding adjacent houses. The key idea is to break down the problem into smaller sub-problems and store the results of these sub-problems to avoid redundant calculations. By doing so, we can efficiently compute the maximum amount of money that can be robbed.

### Approach
1. Define a recursive function `dfs` that takes an index `i` as input, representing the current house being considered.
2. If the current index is out of bounds (`i >= n`), return 0, as there are no more houses to rob.
3. If the current index is not in the memoization dictionary (`i not in memo`), calculate the maximum amount of money that can be robbed by either skipping the current house (`dfs(i+1)`) or robbing it (`nums[i] + dfs(i+2)`).
4. Store the result of the calculation in the memoization dictionary (`memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))`).
5. Return the result of the calculation (`return memo[i]`).

### Time Complexity
The time complexity of this solution is O(n), where n is the number of houses. This is because each house is visited at most once, and the recursive function calls are memoized to avoid redundant calculations.

### Space Complexity
The space complexity of this solution is O(n), where n is the number of houses. This is because the memoization dictionary stores the results of the sub-problems, which can grow up to a size of n in the worst case.

### Key Insight
The key insight behind this solution is the use of memoization to avoid redundant calculations and optimize the recursive function calls. By storing the results of the sub-problems, we can efficiently compute the maximum amount of money that can be robbed, avoiding the need for redundant calculations and reducing the time complexity of the solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.2 MB (Beats 100%) |
| 📅 Solved | 2025-12-19 |
| 💻 Language | Python |