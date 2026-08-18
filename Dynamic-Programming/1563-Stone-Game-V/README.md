> 📌 **Cross-listed:** Primary location is [Array/1563-Stone-Game-V](../../Array/1563-Stone-Game-V). This problem also appears under: **Array**, **Math**, **Dynamic Programming**, **Game Theory**

# 1563. Stone Game V


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Game Theory](https://img.shields.io/badge/Game%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/stone-game-v/)


## 📝 Problem Description

There are several stones **arranged in a row**, and each stone has an associated value which is an integer given in the array `stoneValue`.

In each round of the game, Alice divides the row into **two non-empty rows** (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only **one stone remaining**. Alice's score is initially **zero**.

Return *the maximum score that Alice can obtain*.

 

Example 1:**

```

**Input:** stoneValue = [6,2,3,4,5,5]
**Output:** 18
**Explanation:** In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

```

Example 2:**

```

**Input:** stoneValue = [7,7,7,7,7,7,7]
**Output:** 28

```

Example 3:**

```

**Input:** stoneValue = [4]
**Output:** 0

```

 

**Constraints:**

	- `1 <= stoneValue.length <= 500`

	- `1 <= stoneValue[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**  
When Alice splits a segment `[l,r]`, Bob keeps the larger half.  
Alice’s score for that split is the sum of the smaller half.  
Thus the best score for `[l,r]` is the maximum over all splits where the left sum ≤ right sum.  
If we know the best score for every sub‑segment, we can build larger segments by considering only the “valid” splits.

**Approach**  
1. Compute prefix sums to get any sub‑segment sum in O(1).  
2. `dp[l][r]` – best score Alice can get from `[l,r]`.  
3. `left_best[l][x]` – maximum of `dp[l][k] + sum(l,k)` for all `k ≤ x`.  
   `right_best[y][r]` – maximum of `dp[k][r] + sum(k,r)` for all `k ≥ y`.  
   These helpers let us query the best score of a left or right part in O(1).  
4. For each segment length from 2 to `n`:  
   *Let `total = sum(l,r)`.*  
   *Move two pointers (`left_ptr[l]`, `right_ptr[l]`) to find the last index `k` on the left such that `2*sum(l,k) ≤ total` (left side not larger) and the first index where `2*sum(l,k) ≥ total` (right side not smaller).  
   *The best split is either the best left part (`left_best[l][left_ptr[l]]`) or the best right part (`right_best[right_ptr[l]+1][r]`).  
   *Set `dp[l][r]` to that maximum.  
   *Update `left_best[l][r]` and `right_best[l][r]` using the new `dp[l][r]`.  
5. Return `dp[0][n-1]`.

**Time Complexity**  
`O(n²)` – we iterate over all `O(n²)` segments; each segment’s pointers move only forward, so the total pointer work is also `O(n²)`.

**Space Complexity**  
`O(n²)` – three `n×n` DP tables (`dp`, `left_best`, `right_best`) plus `O(n)` auxiliary arrays.

**Key Insight**  
The optimal split for a segment is always at a boundary where the left sum is just ≤ the right sum. By maintaining prefix sums and two monotonic pointers per left index, we can find that boundary in amortized constant time and use pre‑computed best scores of sub‑segments to fill the DP table efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 863 ms (Beats 68.73%) |
| 💾 Memory | 33.3 MB (Beats 62.93%) |
| 📅 Solved | 2026-08-17 |
| 💻 Language | Python |