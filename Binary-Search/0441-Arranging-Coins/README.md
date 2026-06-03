> 📌 **Cross-listed:** Primary location is [Math/0441-Arranging-Coins](../../Math/0441-Arranging-Coins). This problem also appears under: **Math**, **Binary Search**

# 441. Arranging Coins


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/arranging-coins/)


## 📝 Problem Description

You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the `i^th` row has exactly `i` coins. The last row of the staircase **may be** incomplete.

Given the integer `n`, return *the number of **complete rows** of the staircase you will build*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg)
```

**Input:** n = 5
**Output:** 2
**Explanation:** Because the 3^rd row is incomplete, we return 2.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg)
```

**Input:** n = 8
**Output:** 3
**Explanation:** Because the 4^th row is incomplete, we return 3.

```

 

**Constraints:**

	- `1 <= n <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the number of complete rows in a staircase built with `n` coins. The key insight is that each row `i` requires `i` coins, so we can think of this as a problem of finding the largest `k` such that the sum of the first `k` positive integers is less than or equal to `n`. This is a classic problem that can be solved using binary search.

**Approach**
1. Initialize the search range `[l, r]` to `[1, n]`, where `l` is the smallest possible number of rows and `r` is the largest possible number of rows.
2. While the search range is not empty, find the middle value `mid` of the range.
3. Calculate the number of coins required to build `mid` rows, which is `mid*(mid+1)//2`.
4. If the number of coins required is less than or equal to `n`, update the search range to `[mid+1, r]`. Otherwise, update the search range to `[l, mid-1]`.
5. Repeat steps 2-4 until the search range is empty.
6. The final value of `r` is the number of complete rows.

**Time Complexity**
The time complexity of this solution is O(log n), where n is the input number of coins. This is because we are using binary search to find the largest `k` such that the sum of the first `k` positive integers is less than or equal to `n`.

**Space Complexity**
The space complexity of this solution is O(1), which means the space required does not grow with the size of the input. This is because we are only using a constant amount of space to store the search range and the temporary variables.

**Key Insight**
The key insight behind this solution is that we can use binary search to find the largest `k` such that the sum of the first `k` positive integers is less than or equal to `n`. This is a classic problem that can be solved using binary search, and the time complexity of O(log n) makes it very efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-02-23 |
| 💻 Language | Python |