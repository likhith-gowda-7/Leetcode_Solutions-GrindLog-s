> 📌 **Cross-listed:** Primary location is [Array/1991-Find-the-Middle-Index-in-Array](../../Array/1991-Find-the-Middle-Index-in-Array). This problem also appears under: **Array**, **Prefix Sum**

# 1991. Find the Middle Index in Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-middle-index-in-array/)


## 📝 Problem Description

Given a **0-indexed** integer array `nums`, find the **leftmost** `middleIndex` (i.e., the smallest amongst all the possible ones).

A `middleIndex` is an index where `nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]`.

If `middleIndex == 0`, the left side sum is considered to be `0`. Similarly, if `middleIndex == nums.length - 1`, the right side sum is considered to be `0`.

Return *the **leftmost** *`middleIndex`* that satisfies the condition, or *`-1`* if there is no such index*.

 

Example 1:**

```

**Input:** nums = [2,3,-1,8,4]
**Output:** 3
**Explanation:** The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4

```

Example 2:**

```

**Input:** nums = [1,-1,4]
**Output:** 2
**Explanation:** The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0

```

Example 3:**

```

**Input:** nums = [2,5]
**Output:** -1
**Explanation:** There is no valid middleIndex.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-1000 <= nums[i] <= 1000`

 

**Note:** This question is the same as 724: [https://leetcode.com/problems/find-pivot-index/](https://leetcode.com/problems/find-pivot-index/)

## 🧠 Solution Explanation

**Intuition**
The solution uses the concept of prefix sum to efficiently calculate the sum of elements before and after each index. By maintaining the total sum of the array and the sum of elements before the current index, we can compare these sums to find the middle index.

**Approach**
1. Calculate the total sum of the array.
2. Initialize the left sum to 0.
3. Iterate through the array, for each index:
   1. Calculate the right sum by subtracting the current element and the left sum from the total sum.
   2. If the left sum equals the right sum, return the current index as the middle index.
   3. Otherwise, add the current element to the left sum.
4. If no middle index is found, return -1.

**Time Complexity**
O(n), where n is the length of the array. This is because we make a single pass through the array, performing constant-time operations at each index.

**Space Complexity**
O(1), excluding the input array. We only use a constant amount of space to store the total sum, left sum, and right sum.

**Key Insight**
The key insight is that we can efficiently calculate the sum of elements after each index by subtracting the current element and the sum of elements before the current index from the total sum. This allows us to compare the sums before and after each index to find the middle index.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-10 |
| 💻 Language | Python |