> 📌 **Cross-listed:** Primary location is [Array/2918-Minimum-Equal-Sum-of-Two-Arrays-After-Replacing-Zeros](../../Array/2918-Minimum-Equal-Sum-of-Two-Arrays-After-Replacing-Zeros). This problem also appears under: **Array**, **Greedy**

# 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/)


## 📝 Problem Description

You are given two arrays `nums1` and `nums2` consisting of positive integers.

You have to replace **all** the `0`'s in both arrays with **strictly** positive integers such that the sum of elements of both arrays becomes **equal**.

Return *the **minimum** equal sum you can obtain, or *`-1`* if it is impossible*.

 

Example 1:**

```

**Input:** nums1 = [3,2,0,1,0], nums2 = [6,5,0]
**Output:** 12
**Explanation:** We can replace 0's in the following way:
- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.

```

Example 2:**

```

**Input:** nums1 = [2,0,2,0], nums2 = [1,4]
**Output:** -1
**Explanation:** It is impossible to make the sum of both arrays equal.

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 10^5`

	- `0 <= nums1[i], nums2[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution involves calculating the total sum of each array, counting the number of zeros in each array, and then replacing the zeros with the minimum positive integer (1) to make the sums equal. The key insight is that we can always replace zeros with 1 to increase the sum, and we need to find the minimum sum that makes the two arrays equal.

**Approach**
1. Calculate the total sum of each array using the `sum()` function.
2. Count the number of zeros in each array using the `count()` method.
3. Replace each zero in both arrays with 1, effectively increasing the sum of each array by the number of zeros.
4. Compare the sums of the two arrays and determine the minimum sum that makes them equal.
5. If it's impossible to make the sums equal, return -1.

**Time Complexity**
O(n + m), where n and m are the lengths of the input arrays. This is because we need to iterate over each element in the arrays to calculate the sum and count the zeros.

**Space Complexity**
O(1), as we only use a constant amount of space to store the sums and counts, regardless of the input size.

**Key Insight**
The key insight is that we can always replace zeros with 1 to increase the sum, and we need to find the minimum sum that makes the two arrays equal. This is a classic example of a greedy algorithm, where we make the locally optimal choice (replacing zeros with 1) to achieve the globally optimal solution (making the sums equal).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 841 ms (Beats 59.4%) |
| 💾 Memory | 34.8 MB (Beats 100%) |
| 📅 Solved | 2025-05-10 |
| 💻 Language | Python |