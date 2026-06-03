> 📌 **Cross-listed:** Primary location is [Array/0976-Largest-Perimeter-Triangle](../../Array/0976-Largest-Perimeter-Triangle). This problem also appears under: **Array**, **Math**, **Greedy**, **Sorting**

# 976. Largest Perimeter Triangle


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-perimeter-triangle/)


## 📝 Problem Description

Given an integer array `nums`, return *the largest perimeter of a triangle with a non-zero area, formed from three of these lengths*. If it is impossible to form any triangle of a non-zero area, return `0`.

 

Example 1:**

```

**Input:** nums = [2,1,2]
**Output:** 5
**Explanation:** You can form a triangle with three side lengths: 1, 2, and 2.

```

Example 2:**

```

**Input:** nums = [1,2,1,10]
**Output:** 0
**Explanation:** 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

```

 

**Constraints:**

	- `3 <= nums.length <= 10^4`

	- `1 <= nums[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution works by sorting the input array in descending order and then checking each triplet of numbers to see if they can form a triangle with a non-zero area. A triangle can be formed if the sum of the lengths of any two sides is greater than the length of the third side.

**Approach**
1. Sort the input array `nums` in descending order.
2. Iterate over the sorted array, considering each triplet of numbers `a`, `b`, and `c` where `a` is the largest number and `b` and `c` are the next two largest numbers.
3. For each triplet, check if `a` is less than the sum of `b` and `c`. If this condition is true, it means that the triplet can form a triangle with a non-zero area, so return the perimeter of the triangle (`a + b + c`).
4. If no such triplet is found after iterating over the entire array, return 0.

**Time Complexity**
O(n log n) due to the sorting step, where n is the length of the input array. The subsequent iteration over the sorted array takes O(n) time, but it is dominated by the sorting step.

**Space Complexity**
O(1) since we only use a constant amount of space to store the indices and values of the triplet being considered.

**Key Insight**
The key insight is that we can efficiently check if a triplet of numbers can form a triangle by verifying the triangle inequality (`a < b + c`). This allows us to find the largest perimeter of a triangle with a non-zero area in O(n log n) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 82.96%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-09-28 |
| 💻 Language | Python |