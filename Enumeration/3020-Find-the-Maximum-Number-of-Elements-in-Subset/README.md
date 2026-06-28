> 📌 **Cross-listed:** Primary location is [Array/3020-Find-the-Maximum-Number-of-Elements-in-Subset](../../Array/3020-Find-the-Maximum-Number-of-Elements-in-Subset). This problem also appears under: **Array**, **Hash Table**, **Enumeration**

# 3020. Find the Maximum Number of Elements in Subset


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/)


## 📝 Problem Description

You are given an array of **positive** integers `nums`.

You need to select a subset of `nums` which satisfies the following condition:

	- You can place the selected elements in a **0-indexed** array such that it follows the pattern: `[x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x^4, x^2, x]` (**Note** that `k` can be be any **non-negative** power of `2`). For example, `[2, 4, 16, 4, 2]` and `[3, 9, 3]` follow the pattern while `[2, 4, 8, 4, 2]` does not.

Return *the **maximum** number of elements in a subset that satisfies these conditions.*

 

Example 1:**

```

**Input:** nums = [5,4,1,2,2]
**Output:** 3
**Explanation:** We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 2^2 == 4. Hence the answer is 3.

```

Example 2:**

```

**Input:** nums = [1,3,2,4]
**Output:** 1
**Explanation:** We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {3}, or {4}, there may be multiple subsets which provide the same answer. 

```

 

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first counting the frequency of each number in the input array. It then iterates over the frequency map, checking for numbers that can be squared to form a larger number in the pattern. For each such number, it calculates the maximum number of elements that can be included in the subset, considering both the number itself and its square. The maximum number of elements found is then returned.

**Approach**
1. Count the frequency of each number in the input array using a `Counter` object.
2. Initialize the result (`res`) to the frequency of the number 1 minus 1, then bitwise OR with 1 to ensure it's at least 1.
3. Iterate over the frequency map:
   1. Check if the current number is a perfect square and its square is in the frequency map with a count greater than 1. If so, skip to the next iteration.
   2. Initialize a counter (`n`) to 0.
   3. While the current number is less than 31623 and its frequency is greater than 1:
      1. Increment `n` by 2.
      2. Square the current number.
   4. Update the result (`res`) to be the maximum of the current result and `n` plus twice the indicator function of whether the current number is in the frequency map minus 1.
5. Return the result.

**Time Complexity**
O(n log^2 m), where n is the number of elements in the input array and m is the maximum number in the array. This is because we iterate over the frequency map, and for each number, we perform a binary search-like operation to find the maximum number of elements that can be included in the subset.

**Space Complexity**
O(n), where n is the number of elements in the input array. This is because we use a `Counter` object to store the frequency of each number.

**Key Insight**
The key insight is that for each number, we can include either the number itself or its square in the subset, but not both. By iterating over the frequency map and considering both the number and its square, we can find the maximum number of elements that can be included in the subset.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 96 ms (Beats 87.2%) |
| 💾 Memory | 32 MB (Beats 25.6%) |
| 📅 Solved | 2026-06-27 |
| 💻 Language | Python |