# 1871. Jump Game VII


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-vii/)


## 📝 Problem Description

You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

	- `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and

	- `s[j] == '0'`.

Return `true`* if you can reach index *`s.length - 1`* in *`s`*, or *`false`* otherwise.*

 

Example 1:**

```

**Input:** s = "011010", minJump = 2, maxJump = 3
**Output:** true
**Explanation:**
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

```

Example 2:**

```

**Input:** s = "01101110", minJump = 2, maxJump = 3
**Output:** false

```

 

**Constraints:**

	- `2 <= s.length <= 10^5`

	- `s[i]` is either `'0'` or `'1'`.

	- `s[0] == '0'`

	- `1 <= minJump <= maxJump < s.length`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using a dynamic programming approach with a sliding window. The idea is to maintain a count of reachable indices at each position, and update this count based on the minimum and maximum jump constraints. The solution checks if the last index is reachable by checking the count at the last position.

**Approach**
1. Initialize a list `reachable_count` of size `n` to store the count of reachable indices at each position.
2. Set `reachable_count[0]` to 1, since the starting index is always reachable.
3. Iterate from the second index to the last index, and for each index `i`:
   1. Calculate the left and right bounds of the sliding window based on the minimum and maximum jump constraints.
   2. Update the count of reachable indices by adding the count at the left bound and subtracting the count at the right bound.
   3. If the count is greater than 0 and the current index is 0, set `reachable_count[i]` to 1.
4. Return True if the last index is reachable (i.e., `reachable_count[-1]` is 1), and False otherwise.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we are iterating over the string once, and the operations inside the loop take constant time.

**Space Complexity**
O(n), where n is the length of the string `s`. This is because we are using a list of size `n` to store the count of reachable indices at each position.

**Key Insight**
The key insight is to use a sliding window approach to update the count of reachable indices at each position, based on the minimum and maximum jump constraints. This allows us to efficiently determine whether the last index is reachable or not.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 169 ms (Beats 58.75%) |
| 💾 Memory | 20.5 MB (Beats 84.74%) |
| 📅 Solved | 2026-05-25 |
| 💻 Language | Python |