# 217. Contains Duplicate


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/contains-duplicate/)


## 📝 Problem Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

 

Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

## Intuition
This approach works by comparing the length of the original list to the length of a set created from the list. A set in Python is an unordered collection of unique elements, so any duplicates in the original list are automatically removed in the set. If the lengths are not equal, it means there were duplicates in the original list.

## Approach
1. Create a set from the input list `nums`. This set will contain only unique elements from `nums`.
2. Compare the length of the original list `nums` to the length of the set.
3. If the lengths are not equal, return `True` because there are duplicates in `nums`.
4. If the lengths are equal, return `False` because all elements in `nums` are distinct.

## Time Complexity
The time complexity is O(n), where n is the number of elements in `nums`. This is because creating a set from a list in Python takes linear time.

## Space Complexity
The space complexity is also O(n), where n is the number of elements in `nums`. This is because in the worst-case scenario (all elements are unique), the set will contain the same number of elements as the original list.

## Key Insight
The key insight here is that sets automatically eliminate duplicate values, making them a perfect data structure for this problem. By comparing the lengths of the original list and the set, we can efficiently determine if there are any duplicates in the list.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 93.8%) |
| 💾 Memory | 31.5 MB (Beats 53.93%) |
| 📅 Solved | 2025-01-17 |
| 💻 Language | Python |