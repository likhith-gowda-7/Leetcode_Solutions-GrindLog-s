> 📌 **Cross-listed:** Primary location is [Array/0001-Two-Sum](../../Array/0001-Two-Sum). This problem also appears under: **Array**, **Hash Table**

# 1. Two Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/two-sum/)


## 📝 Problem Description

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

 

Example 1:**

```

**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

```

Example 2:**

```

**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

```

Example 3:**

```

**Input:** nums = [3,3], target = 6
**Output:** [0,1]

```

 

**Constraints:**

	- `2 <= nums.length <= 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- `-10^9 <= target <= 10^9`

	- **Only one valid answer exists.**

 

**Follow-up: **Can you come up with an algorithm that is less than `O(n^2)` time complexity?

## 🧠 Solution Explanation

## Intuition
This approach works by iterating through the array and keeping track of the elements we've seen so far, along with their indices. We use a hash table to store this information, allowing us to look up the complement of the current element in constant time. This enables us to find the two numbers that add up to the target in a single pass through the array. The key idea is to exploit the fact that we only need to find one solution, and we can use the hash table to avoid redundant calculations.

## Approach
1. Create an empty hash table `h1` to store the elements we've seen so far and their indices.
2. Iterate through the array `nums` using `enumerate` to get both the index `i` and the value `val` of each element.
3. For each element, calculate the remainder `rem` by subtracting the current value from the target.
4. Check if the remainder `rem` is already in the hash table `h1`. If it is, return the indices of the current element and its complement.
5. If the remainder is not in the hash table, add the current element and its index to the hash table.

## Time Complexity
The time complexity is O(n), where n is the length of the array `nums`. This is because we make a single pass through the array, and the hash table operations (lookup and insert) take constant time on average.

## Space Complexity
The space complexity is O(n), where n is the length of the array `nums`. This is because in the worst case, we might need to store every element in the hash table.

## Key Insight
The key insight here is that using a hash table allows us to avoid the need for nested loops or other expensive operations, reducing the time complexity from O(n^2) to O(n). This is a classic example of how a well-chosen data structure can greatly simplify a problem and improve performance.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 52.95%) |
| 💾 Memory | 20.5 MB (Beats 42.46%) |
| 📅 Solved | 2026-03-11 |
| 💻 Language | Python |