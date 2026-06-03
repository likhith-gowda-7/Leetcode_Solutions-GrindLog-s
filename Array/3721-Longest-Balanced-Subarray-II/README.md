# 3721. Longest Balanced Subarray II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-balanced-subarray-ii/)


## 📝 Problem Description

You are given an integer array `nums`.

A **subarray** is called **balanced** if the number of **distinct even** numbers in the subarray is equal to the number of **distinct odd** numbers.

Return the length of the **longest** balanced subarray.

 

Example 1:**

**Input:** nums = [2,5,4,3]

**Output:** 4

**Explanation:**

	- The longest balanced subarray is `[2, 5, 4, 3]`.

	- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

Example 2:**

**Input:** nums = [3,2,2,5,4]

**Output:** 5

**Explanation:**

	- The longest balanced subarray is `[3, 2, 2, 5, 4]`.

	- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[3, 5]`. Thus, the answer is 5.

Example 3:**

**Input:** nums = [1,2,3,2]

**Output:** 3

**Explanation:**

	- The longest balanced subarray is `[2, 3, 2]`.

	- It has 1 distinct even number `[2]` and 1 distinct odd number `[3]`. Thus, the answer is 3.

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a Segment Tree to efficiently update and query the number of distinct even and odd numbers in a subarray. By maintaining a balance between even and odd numbers, it can find the longest balanced subarray.

**Approach**
1. Initialize a Segment Tree with `n` nodes, where `n` is the length of the input array `nums`.
2. Create a hash table `pos` to store the indices of each number in `nums`.
3. Iterate through `nums` and for each number `v`, add a range of indices to the Segment Tree using the `add_range` method. The range corresponds to the indices of `v` in `pos`, and the value to add is `1` if `v` is odd and `-1` if `v` is even.
4. Initialize a pointer `ptr` to keep track of the current index for each number in `pos`.
5. Iterate through `nums` again and for each number `x`, find the rightmost index `r` such that the number of distinct even and odd numbers in the subarray `[l, r]` is balanced using the `find` method of the Segment Tree.
6. Update the answer `ans` with the maximum length of the balanced subarray found so far.
7. Update the pointer `ptr` for each number `x` and add a range of indices to the Segment Tree using the `add` method. The range corresponds to the indices of `x` in `pos`, and the value to add is `-1` if `x` is odd and `1` if `x` is even.

**Time Complexity**
The time complexity of the solution is O(n log n), where n is the length of the input array `nums`. This is because the `add_range` and `find` methods of the Segment Tree take O(log n) time, and we perform these operations n times.

**Space Complexity**
The space complexity of the solution is O(n), where n is the length of the input array `nums`. This is because we need to store the indices of each number in `nums` in the hash table `pos`, and the Segment Tree requires O(n) space.

**Key Insight**
The key insight behind the solution is to use a Segment Tree to efficiently update and query the number of distinct even and odd numbers in a subarray. By maintaining a balance between even and odd numbers, we can find the longest balanced subarray. The use of a hash table to store the indices of each number in `nums` allows us to efficiently update the pointer `ptr` and add ranges to the Segment Tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 12300 ms (Beats 5.69%) |
| 💾 Memory | 62.1 MB (Beats 52.03%) |
| 📅 Solved | 2026-02-28 |
| 💻 Language | Python |