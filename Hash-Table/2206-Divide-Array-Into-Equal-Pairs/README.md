> 📌 **Cross-listed:** Primary location is [Array/2206-Divide-Array-Into-Equal-Pairs](../../Array/2206-Divide-Array-Into-Equal-Pairs). This problem also appears under: **Array**, **Hash Table**, **Bit Manipulation**, **Counting**

# 2206. Divide Array Into Equal Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/divide-array-into-equal-pairs/)


## 📝 Problem Description

You are given an integer array `nums` consisting of `2 * n` integers.

You need to divide `nums` into `n` pairs such that:

	- Each element belongs to **exactly one** pair.

	- The elements present in a pair are **equal**.

Return `true` *if nums can be divided into* `n` *pairs, otherwise return* `false`.

 

Example 1:**

```

**Input:** nums = [3,2,3,2,2,2]
**Output:** true
**Explanation:** 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

```

Example 2:**

```

**Input:** nums = [1,2,3,4]
**Output:** false
**Explanation:** 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

```

 

**Constraints:**

	- `nums.length == 2 * n`

	- `1 <= n <= 500`

	- `1 <= nums[i] <= 500`

## 🧠 Solution Explanation

**Intuition**
The solution works by utilizing a set to keep track of the elements in the array. Since a set only stores unique elements, if the array can be divided into pairs of equal elements, the set should contain no elements after processing the array. This is because each element will be paired with another instance of the same element, effectively removing it from the set.

**Approach**
1. Initialize an empty set `check` to store unique elements from the array.
2. Iterate through each element `val` in the array `nums`.
3. If `val` is already present in the set `check`, remove it from the set.
4. If `val` is not present in the set `check`, add it to the set.
5. After processing all elements in the array, check if the set `check` is empty. If it is, return `True`, indicating that the array can be divided into pairs of equal elements. Otherwise, return `False`.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we are iterating through each element in the array once.

**Space Complexity**
O(n), where n is the length of the array `nums`. In the worst-case scenario, all elements in the array are unique, and we need to store them in the set `check`.

**Key Insight**
The key insight is that a set can be used to efficiently check if all elements in the array can be paired with another instance of the same element. This is because a set automatically removes duplicates, and if the array can be divided into pairs, the set should be empty after processing all elements.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2 ms (Beats 79.57%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-03-17 |
| 💻 Language | Python |