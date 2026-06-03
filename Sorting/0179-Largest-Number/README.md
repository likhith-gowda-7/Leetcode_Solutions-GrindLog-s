> 📌 **Cross-listed:** Primary location is [Array/0179-Largest-Number](../../Array/0179-Largest-Number). This problem also appears under: **Array**, **String**, **Greedy**, **Sorting**

# 179. Largest Number


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-number/)


## 📝 Problem Description

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:**

```

**Input:** nums = [10,2]
**Output:** "210"

```

Example 2:**

```

**Input:** nums = [3,30,34,5,9]
**Output:** "9534330"

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

## Intuition
The solution works by first converting all numbers to strings, then sorting them in descending order based on a custom key. This key is designed to compare the numbers as if they were concatenated, allowing the largest possible number to be formed. The intuition behind this approach is to prioritize numbers that, when concatenated, produce the largest possible result.

## Approach
1. Convert all numbers in the input list to strings.
2. Sort the list of strings in descending order using a custom key function that repeats each string 10 times (or any number greater than the maximum length of the strings) to simulate concatenation.
3. Check if the first element in the sorted list is "0". If so, return "0" as the largest number, since all other numbers in the list are also "0".
4. Join the sorted list of strings into a single string to form the largest possible number.

## Time Complexity
The time complexity is O(n log n) due to the sorting operation, where n is the number of elements in the input list. The custom key function adds a constant factor to the comparison, but does not change the overall time complexity.

## Space Complexity
The space complexity is O(n) as we need to store the list of strings, where n is the number of elements in the input list. The sorting operation may also require additional space, depending on the implementation.

## Key Insight
The key insight behind this solution is the use of a custom key function to compare numbers as if they were concatenated, allowing the sorting algorithm to prioritize numbers that produce the largest possible result when combined. This approach enables the solution to efficiently find the largest possible number that can be formed from the input list.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 24.3%) |
| 📅 Solved | 2026-03-20 |
| 💻 Language | Python |