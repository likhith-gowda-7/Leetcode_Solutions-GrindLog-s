# 368. Largest Divisible Subset


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-divisible-subset/)


## 📝 Problem Description

Given a set of **distinct** positive integers `nums`, return the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

	- `answer[i] % answer[j] == 0`, or

	- `answer[j] % answer[i] == 0`

If there are multiple solutions, return any of them.

 

Example 1:**

```

**Input:** nums = [1,2,3]
**Output:** [1,2]
**Explanation:** [1,3] is also accepted.

```

Example 2:**

```

**Input:** nums = [1,2,4,8]
**Output:** [1,2,4,8]

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 2 * 10^9`

	- All the integers in `nums` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the largest subset of distinct positive integers such that every pair of elements in the subset satisfies a divisibility condition. The key insight is to use dynamic programming to build up the largest subset by considering each number in the input array and finding the largest subset that includes it.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Initialize an array `div_set` of the same length as `nums` to store the index of the previous element in the largest subset that includes each number.
3. Initialize an array `dp` of the same length as `nums` to store the size of the largest subset that includes each number.
4. Iterate through the sorted array `nums` and for each number, check all previous numbers to see if it is divisible. If it is, and the size of the subset that includes the previous number plus one is greater than the current size of the subset that includes the current number, update `div_set` and `dp` accordingly.
5. Keep track of the maximum size of the subset found so far and the index of the last element in the subset.
6. Once the iteration is complete, use `div_set` to backtrack and construct the largest subset.

**Time Complexity**
O(n^2), where n is the length of the input array `nums`. This is because we have two nested loops that iterate through the array.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because we need to store the `div_set` and `dp` arrays, each of length n.

**Key Insight**
The key insight is to use dynamic programming to build up the largest subset by considering each number in the input array and finding the largest subset that includes it. This allows us to efficiently find the largest subset that satisfies the divisibility condition.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 175 ms (Beats 33.25%) |
| 💾 Memory | 19.5 MB (Beats 30.15%) |
| 📅 Solved | 2026-06-13 |
| 💻 Language | Python |