> 📌 **Cross-listed:** Primary location is [Array/0875-Koko-Eating-Bananas](../../Array/0875-Koko-Eating-Bananas). This problem also appears under: **Array**, **Binary Search**

# 875. Koko Eating Bananas


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)


## 📝 Problem Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i^th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

 

Example 1:**

```

**Input:** piles = [3,6,7,11], h = 8
**Output:** 4

```

Example 2:**

```

**Input:** piles = [30,11,23,4,20], h = 5
**Output:** 30

```

Example 3:**

```

**Input:** piles = [30,11,23,4,20], h = 6
**Output:** 23

```

 

**Constraints:**

	- `1 <= piles.length <= 10^4`

	- `piles.length <= h <= 10^9`

	- `1 <= piles[i] <= 10^9`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 148 ms (Beats 97.27%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-01 |
| 💻 Language | Python |