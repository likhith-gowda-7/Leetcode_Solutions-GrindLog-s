> 📌 **Cross-listed:** Primary location is [String/2379-Minimum-Recolors-to-Get-K-Consecutive-Black-Blocks](../../String/2379-Minimum-Recolors-to-Get-K-Consecutive-Black-Blocks). This problem also appears under: **String**, **Sliding Window**

# 2379. Minimum Recolors to Get K Consecutive Black Blocks


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)


## 📝 Problem Description

You are given a **0-indexed** string `blocks` of length `n`, where `blocks[i]` is either `'W'` or `'B'`, representing the color of the `i^th` block. The characters `'W'` and `'B'` denote the colors white and black, respectively.

You are also given an integer `k`, which is the desired number of **consecutive** black blocks.

In one operation, you can **recolor** a white block such that it becomes a black block.

Return* the **minimum** number of operations needed such that there is at least **one** occurrence of *`k`* consecutive black blocks.*

 

Example 1:**

```

**Input:** blocks = "WBBWWBBWBW", k = 7
**Output:** 3
**Explanation:**
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

```

Example 2:**

```

**Input:** blocks = "WBWBBBW", k = 2
**Output:** 0
**Explanation:**
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

```

 

**Constraints:**

	- `n == blocks.length`

	- `1 <= n <= 100`

	- `blocks[i]` is either `'W'` or `'B'`.

	- `1 <= k <= n`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to track the minimum number of operations needed to achieve `k` consecutive black blocks. It maintains a count of white blocks within the current window and updates this count as the window moves.

**Approach**
1. Initialize the minimum count of white blocks (`mini`) and the current count of white blocks (`sl`) within the first window of size `k`.
2. Iterate through the string `blocks` from the `k`-th character to the end.
3. For each character, if it is a white block, increment the current count `sl`.
4. If the character `k` positions before is a white block, decrement the current count `sl`.
5. Update the minimum count `mini` if the current count `sl` is smaller.
6. Return the minimum count `mini` as the minimum number of operations needed.

**Time Complexity**
O(n), where n is the length of the string `blocks`. This is because we iterate through the string once.

**Space Complexity**
O(1), since we only use a constant amount of space to store the minimum count and the current count.

**Key Insight**
The key insight is that we only need to keep track of the minimum count of white blocks within the current window, which allows us to efficiently update the count as the window moves. This is made possible by the fact that we only need to consider the characters within the current window, which are at most `k` positions apart.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-03-08 |
| 💻 Language | Python |