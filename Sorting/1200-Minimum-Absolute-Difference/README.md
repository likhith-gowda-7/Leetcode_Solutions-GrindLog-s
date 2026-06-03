> 📌 **Cross-listed:** Primary location is [Array/1200-Minimum-Absolute-Difference](../../Array/1200-Minimum-Absolute-Difference). This problem also appears under: **Array**, **Sorting**

# 1200. Minimum Absolute Difference


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-absolute-difference/)


## 📝 Problem Description

Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

	- `a, b` are from `arr`

	- `a < b`

	- `b - a` equals to the minimum absolute difference of any two elements in `arr`

 

Example 1:**

```

**Input:** arr = [4,2,1,3]
**Output:** [[1,2],[2,3],[3,4]]
**Explanation: **The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
```

Example 2:**

```

**Input:** arr = [1,3,6,10,15]
**Output:** [[1,3]]

```

Example 3:**

```

**Input:** arr = [3,8,-10,23,19,-4,-14,27]
**Output:** [[-14,-10],[19,23],[23,27]]

```

 

**Constraints:**

	- `2 <= arr.length <= 10^5`

	- `-10^6 <= arr[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the input array in ascending order. Then, it iterates through the sorted array to find the minimum absolute difference between any two elements. Once the minimum difference is found, it iterates through the array again to find all pairs of elements with the minimum difference.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Initialize `min_diff` to infinity and `res` to an empty list.
3. Iterate through the sorted array from index 1 to `n-1` (where `n` is the length of the array).
4. For each iteration, calculate the absolute difference `curr_diff` between the current element and the previous element.
5. If `curr_diff` is less than `min_diff`, update `min_diff` to `curr_diff`.
6. After finding the minimum difference, iterate through the sorted array again from index 1 to `n-1`.
7. For each iteration, calculate the absolute difference `curr_diff` between the current element and the previous element.
8. If `curr_diff` is equal to `min_diff`, append a pair of elements `[nums[i-1], nums[i]]` to the `res` list.
9. Return the `res` list.

**Time Complexity**
The time complexity is O(n log n) due to the sorting step, where n is the length of the input array. The subsequent two loops have a time complexity of O(n), but they are dominated by the sorting step.

**Space Complexity**
The space complexity is O(n) for the sorting step, where n is the length of the input array. The space complexity of the subsequent two loops is O(1) since they only iterate through the array and do not use any additional space that scales with the input size.

**Key Insight**
The key insight is that after sorting the array, we can find the minimum absolute difference by iterating through the array only once. Once the minimum difference is found, we can then iterate through the array again to find all pairs of elements with the minimum difference. This approach avoids unnecessary comparisons and makes the solution efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 55 ms (Beats 52.19%) |
| 💾 Memory | 31.7 MB (Beats 17.05%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | Python |