> 📌 **Cross-listed:** Primary location is [Array/0561-Array-Partition](../../Array/0561-Array-Partition). This problem also appears under: **Array**, **Greedy**, **Sorting**, **Counting Sort**

# 561. Array Partition


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting Sort](https://img.shields.io/badge/Counting%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/array-partition/)


## 📝 Problem Description

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a_1, b_1), (a_2, b_2), ..., (a_n, b_n)` such that the sum of `min(a_i, b_i)` for all `i` is **maximized**. Return* the maximized sum*.

 

Example 1:**

```

**Input:** nums = [1,4,3,2]
**Output:** 4
**Explanation:** All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
```

Example 2:**

```

**Input:** nums = [6,2,6,5,1,2]
**Output:** 9
**Explanation:** The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

```

 

**Constraints:**

	- `1 <= n <= 10^4`

	- `nums.length == 2 * n`

	- `-10^4 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The problem requires us to maximize the sum of the minimum values in each pair of integers. To achieve this, we can sort the array and then select every other element, starting from the smallest one. This approach ensures that we always choose the smallest possible value for each pair, thereby maximizing the sum.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Initialize a variable `total` to store the sum of the minimum values in each pair.
3. Iterate over the sorted array, selecting every other element starting from the first one (at index 0).
4. For each selected element, add its value to the `total` variable.
5. Return the final value of `total` as the maximized sum.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the number of elements in the input array.

**Space Complexity**
O(1) since we only use a constant amount of space to store the `total` variable and do not allocate any additional space that scales with the input size.

**Key Insight**
The key to this solution is to recognize that sorting the array allows us to easily select the smallest possible value for each pair, which maximizes the sum. By iterating over the sorted array and selecting every other element, we ensure that we always choose the smallest value for each pair, resulting in the maximum possible sum.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.7 MB (Beats 6.48%) |
| 📅 Solved | 2026-01-25 |
| 💻 Language | Python |