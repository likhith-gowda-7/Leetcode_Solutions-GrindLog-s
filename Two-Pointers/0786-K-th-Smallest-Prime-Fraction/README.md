> 📌 **Cross-listed:** Primary location is [Array/0786-K-th-Smallest-Prime-Fraction](../../Array/0786-K-th-Smallest-Prime-Fraction). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Sorting**, **Heap (Priority Queue)**

# 786. K-th Smallest Prime Fraction


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/k-th-smallest-prime-fraction/)


## 📝 Problem Description

You are given a sorted integer array `arr` containing `1` and **prime** numbers, where all the integers of `arr` are unique. You are also given an integer `k`.

For every `i` and `j` where `0 <= i < j < arr.length`, we consider the fraction `arr[i] / arr[j]`.

Return *the* `k^th` *smallest fraction considered*. Return your answer as an array of integers of size `2`, where `answer[0] == arr[i]` and `answer[1] == arr[j]`.

 

Example 1:**

```

**Input:** arr = [1,2,3,5], k = 3
**Output:** [2,5]
**Explanation:** The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

```

Example 2:**

```

**Input:** arr = [1,7], k = 1
**Output:** [1,7]

```

 

**Constraints:**

	- `2 <= arr.length <= 1000`

	- `1 <= arr[i] <= 3 * 10^4`

	- `arr[0] == 1`

	- `arr[i]` is a **prime** number for `i > 0`.

	- All the numbers of `arr` are **unique** and sorted in **strictly increasing** order.

	- `1 <= k <= arr.length * (arr.length - 1) / 2`

 

**Follow up:** Can you solve the problem with better than `O(n^2)` complexity?

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1256 ms (Beats 25.17%) |
| 💾 Memory | 109.1 MB (Beats 12.47%) |
| 📅 Solved | 2025-07-09 |
| 💻 Language | Python |