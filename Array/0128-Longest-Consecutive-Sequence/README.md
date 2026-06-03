# 128. Longest Consecutive Sequence


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)


## 📝 Problem Description

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

 

Example 1:**

```

**Input:** nums = [100,4,200,1,3,2]
**Output:** 4
**Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

```

Example 2:**

```

**Input:** nums = [0,3,7,2,5,8,4,6,0,1]
**Output:** 9

```

Example 3:**

```

**Input:** nums = [1,0,1,2]
**Output:** 3

```

 

**Constraints:**

	- `0 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

## Intuition
The solution works by first converting the input list into a set for efficient lookups. It then iterates over each number in the set, checking if it's the start of a consecutive sequence. If it is, the solution counts the length of the sequence by continuously checking for the presence of the next number in the set.

## Approach
1. Convert the input list into a set to remove duplicates and enable O(1) lookups.
2. Initialize a variable `maxi` to store the length of the longest consecutive sequence found so far.
3. Iterate over each number `num` in the set.
4. For each `num`, check if `num - 1` is not in the set. If it's not, then `num` is the start of a consecutive sequence.
5. If `num` is the start of a sequence, count the length of the sequence by continuously checking for the presence of `prev + 1` in the set, where `prev` is the current number in the sequence.
6. Update `maxi` if the length of the current sequence is greater than the previous maximum.

## Time Complexity
The time complexity is O(n), where n is the number of elements in the input list. This is because each number in the input list is processed at most twice: once in the outer loop and once in the inner while loop.

## Space Complexity
The space complexity is O(n), where n is the number of elements in the input list. This is because the input list is converted into a set, which requires additional space proportional to the size of the input list.

## Key Insight
The key insight behind this solution is the use of a set to enable efficient lookups, allowing the solution to check for the presence of consecutive numbers in O(1) time. This, combined with the strategy of only counting sequences that start with a number that has no predecessor in the set, ensures that each number is processed at most twice, resulting in a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 85.41%) |
| 💾 Memory | 33.2 MB (Beats 91.74%) |
| 📅 Solved | 2025-06-26 |
| 💻 Language | Python |