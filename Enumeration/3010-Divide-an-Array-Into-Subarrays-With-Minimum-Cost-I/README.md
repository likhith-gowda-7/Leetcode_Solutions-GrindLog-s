> 📌 **Cross-listed:** Primary location is [Array/3010-Divide-an-Array-Into-Subarrays-With-Minimum-Cost-I](../../Array/3010-Divide-an-Array-Into-Subarrays-With-Minimum-Cost-I). This problem also appears under: **Array**, **Sorting**, **Enumeration**

# 3010. Divide an Array Into Subarrays With Minimum Cost I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/)


## 📝 Problem Description

You are given an array of integers `nums` of length `n`.

The **cost** of an array is the value of its **first** element. For example, the cost of `[1,2,3]` is `1` while the cost of `[3,4,1]` is `3`.

You need to divide `nums` into `3` **disjoint contiguous **subarrays.

Return *the **minimum** possible **sum** of the cost of these subarrays*.

 

Example 1:**

```

**Input:** nums = [1,2,3,12]
**Output:** 6
**Explanation:** The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
The other possible ways to form 3 subarrays are:
- [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
- [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.

```

Example 2:**

```

**Input:** nums = [5,4,3]
**Output:** 12
**Explanation:** The best possible way to form 3 subarrays is: [5], [4], and [3] at a total cost of 5 + 4 + 3 = 12.
It can be shown that 12 is the minimum cost achievable.

```

Example 3:**

```

**Input:** nums = [10,3,1,1]
**Output:** 12
**Explanation:** The best possible way to form 3 subarrays is: [10,3], [1], and [1] at a total cost of 10 + 1 + 1 = 12.
It can be shown that 12 is the minimum cost achievable.

```

 

**Constraints:**

	- `3 <= n <= 50`

	- `1 <= nums[i] <= 50`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a running total of the minimum costs and updating it with the smallest two elements in the array. This approach leverages the fact that the cost of each subarray is the value of its first element, and we want to minimize the sum of these costs.

**Approach**
1. Initialize the total cost with the first element of the array (`nums[0]`).
2. Initialize two variables, `mini1` and `mini2`, to store the smallest and second smallest elements in the array, respectively. Initialize them to infinity.
3. Iterate through the array starting from the second element (`nums[1:]`).
4. If the current element is smaller than `mini1`, update `mini2` to be the old value of `mini1` and update `mini1` to be the current element.
5. If the current element is smaller than `mini2` but not smaller than `mini1`, update `mini2` to be the current element.
6. After the iteration, add `mini1` and `mini2` to the total cost.
7. Return the total cost.

**Time Complexity**
O(n), where n is the length of the array. This is because we make a single pass through the array to find the smallest two elements.

**Space Complexity**
O(1), as we only use a constant amount of space to store the total cost and the smallest two elements.

**Key Insight**
The key insight is that we only need to keep track of the smallest two elements in the array, as the cost of each subarray is the value of its first element. By updating the total cost with the smallest two elements, we can efficiently find the minimum possible sum of the costs of the subarrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 87.03%) |
| 📅 Solved | 2026-02-01 |
| 💻 Language | Python |