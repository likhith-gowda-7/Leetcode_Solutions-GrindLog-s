> 📌 **Cross-listed:** Primary location is [Array/1395-Count-Number-of-Teams](../../Array/1395-Count-Number-of-Teams). This problem also appears under: **Array**, **Dynamic Programming**, **Binary Indexed Tree**, **Segment Tree**

# 1395. Count Number of Teams


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Binary Indexed Tree](https://img.shields.io/badge/Binary%20Indexed%20Tree-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-number-of-teams/)


## 📝 Problem Description

There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

You have to form a team of 3 soldiers amongst them under the following rules:

	- Choose 3 soldiers with index (`i`, `j`, `k`) with rating (`rating[i]`, `rating[j]`, `rating[k]`).

	- A team is valid if: (`rating[i] < rating[j] < rating[k]`) or (`rating[i] > rating[j] > rating[k]`) where (`0 <= i < j < k < n`).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:**

```

**Input:** rating = [2,5,3,4,1]
**Output:** 3
**Explanation:** We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

```

Example 2:**

```

**Input:** rating = [2,1,3]
**Output:** 0
**Explanation:** We can't form any team given the conditions.

```

Example 3:**

```

**Input:** rating = [1,2,3,4]
**Output:** 4

```

 

**Constraints:**

	- `n == rating.length`

	- `3 <= n <= 1000`

	- `1 <= rating[i] <= 10^5`

	- All the integers in `rating` are **unique**.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 467 ms (Beats 55.93%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-06-28 |
| 💻 Language | Python |