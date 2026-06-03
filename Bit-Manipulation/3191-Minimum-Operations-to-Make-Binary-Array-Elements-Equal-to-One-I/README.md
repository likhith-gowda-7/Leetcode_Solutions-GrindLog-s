> 📌 **Cross-listed:** Primary location is [Array/3191-Minimum-Operations-to-Make-Binary-Array-Elements-Equal-to-One-I](../../Array/3191-Minimum-Operations-to-Make-Binary-Array-Elements-Equal-to-One-I). This problem also appears under: **Array**, **Bit Manipulation**, **Queue**, **Sliding Window**, **Prefix Sum**

# 3191. Minimum Operations to Make Binary Array Elements Equal to One I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/)


## 📝 Problem Description

You are given a binary array `nums`.

You can do the following operation on the array **any** number of times (possibly zero):

	- Choose **any** 3 **consecutive** elements from the array and **flip** **all** of them.

**Flipping** an element means changing its value from 0 to 1, and from 1 to 0.

Return the **minimum** number of operations required to make all elements in `nums` equal to 1. If it is impossible, return -1.

 

Example 1:**

**Input:** nums = [0,1,1,1,0,0]

**Output:** 3

**Explanation:**

We can do the following operations:

	- Choose the elements at indices 0, 1 and 2. The resulting array is `nums = [**1**,**0**,**0**,1,0,0]`.

	- Choose the elements at indices 1, 2 and 3. The resulting array is `nums = [1,**1**,**1**,**0**,0,0]`.

	- Choose the elements at indices 3, 4 and 5. The resulting array is `nums = [1,1,1,**1**,**1**,**1**]`.

Example 2:**

**Input:** nums = [0,1,1,1]

**Output:** -1

**Explanation:**

It is impossible to make all elements equal to 1.

 

**Constraints:**

	- `3 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 1`

## 🧠 Solution Explanation

**Intuition**
The key insight here is that we can only flip 3 consecutive elements at a time. This means that we can only change the parity of the number of 1s in a window of 3 elements. Therefore, we need to find the minimum number of such operations required to make all elements equal to 1.

**Approach**
1. Initialize a counter `c` to keep track of the number of 0s encountered so far.
2. Iterate over the array `nums` with a sliding window of size 3. If the current element is 0, increment the counter `c` and flip all 3 elements in the current window.
3. After the iteration, check if the last two elements are 1. If they are, it means that we can make all elements equal to 1 by flipping the last two elements. Return the counter `c` as the minimum number of operations required.
4. If the last two elements are not 1, it means that it's impossible to make all elements equal to 1, so return -1.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we are iterating over the array once with a sliding window of size 3.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the counter `c` and the length of the array `n`.

**Key Insight**
The key insight here is that we can only change the parity of the number of 1s in a window of 3 elements. This means that we need to find the minimum number of such operations required to make all elements equal to 1.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 107 ms (Beats 71.65%) |
| 💾 Memory | 21.7 MB (Beats 100%) |
| 📅 Solved | 2025-04-01 |
| 💻 Language | Python |