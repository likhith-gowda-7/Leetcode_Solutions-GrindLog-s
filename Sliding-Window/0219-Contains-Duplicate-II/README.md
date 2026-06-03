> 📌 **Cross-listed:** Primary location is [Array/0219-Contains-Duplicate-II](../../Array/0219-Contains-Duplicate-II). This problem also appears under: **Array**, **Hash Table**, **Sliding Window**

# 219. Contains Duplicate II


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices** *`i`* and *`j`* in the array such that *`nums[i] == nums[j]`* and *`abs(i - j) <= k`.

 

Example 1:**

```

**Input:** nums = [1,2,3,1], k = 3
**Output:** true

```

Example 2:**

```

**Input:** nums = [1,0,1,1], k = 1
**Output:** true

```

Example 3:**

```

**Input:** nums = [1,2,3,1,2,3], k = 2
**Output:** false

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

	- `0 <= k <= 10^5`

## 🧠 Solution Explanation

## Intuition
This approach works by maintaining a dictionary to store the most recent index of each number in the array. It iterates through the array, checking if the current number has been seen before and if its previous index is within the specified distance `k`. This allows for efficient detection of duplicates within the given range.

## Approach
1. Initialize an empty dictionary `seen` to store the most recent index of each number.
2. Iterate through the array `nums` using `enumerate` to get both the index `ind` and the value `val`.
3. For each number, check if it is already in the `seen` dictionary and if the difference between the current index and the previous index is less than or equal to `k`.
4. If the condition is met, return `True` as a duplicate is found within the specified distance.
5. Otherwise, update the `seen` dictionary with the current index for the current number.
6. If the loop completes without finding any duplicates within the specified distance, return `False`.

## Time Complexity
The time complexity is O(n), where n is the length of the array `nums`, because we are iterating through the array once and performing constant-time operations for each element.

## Space Complexity
The space complexity is O(n), where n is the length of the array `nums`, because in the worst-case scenario, we might need to store every element in the `seen` dictionary.

## Key Insight
The key insight here is using a dictionary to keep track of the most recent index of each number, allowing for efficient lookups and updates, which enables us to solve the problem in linear time complexity. This approach takes advantage of the fact that dictionaries provide constant-time access and update operations on average.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 27 ms (Beats 88.5%) |
| 💾 Memory | 36.7 MB (Beats 29.53%) |
| 📅 Solved | 2025-11-26 |
| 💻 Language | Python |