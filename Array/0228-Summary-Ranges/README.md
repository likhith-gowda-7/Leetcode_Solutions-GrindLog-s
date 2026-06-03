# 228. Summary Ranges


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/summary-ranges/)


## 📝 Problem Description

You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

	- `"a->b"` if `a != b`

	- `"a"` if `a == b`

 

Example 1:**

```

**Input:** nums = [0,1,2,4,5,7]
**Output:** ["0->2","4->5","7"]
**Explanation:** The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

```

Example 2:**

```

**Input:** nums = [0,2,3,4,6,8,9]
**Output:** ["0","2->4","6","8->9"]
**Explanation:** The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

```

 

**Constraints:**

	- `0 <= nums.length <= 20`

	- `-2^31 <= nums[i] <= 2^31 - 1`

	- All the values of `nums` are **unique**.

	- `nums` is sorted in ascending order.

## 🧠 Solution Explanation

### Intuition
The solution works by iterating through the sorted array and identifying continuous ranges of numbers. It checks if the current number is consecutive to the next number, and if so, it continues to the next number. This approach takes advantage of the fact that the input array is sorted and unique. By doing so, it can efficiently group consecutive numbers into ranges.

### Approach
1. Initialize an empty list `res` to store the result and a pointer `i` to traverse the array.
2. Iterate through the array, and for each number, check if it is the start of a new range.
3. If the current number is consecutive to the next number, move the pointer `i` forward until it reaches a number that is not consecutive.
4. Once the end of a range is found, append the range to the result list in the required format.
5. Move the pointer `i` forward to start the next range.

### Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because the solution iterates through the array once, and each operation within the loop takes constant time.

### Space Complexity
The space complexity is O(n), where n is the length of the input array. This is because in the worst-case scenario (when all numbers are non-consecutive), the solution will store each number as a separate range in the result list.

### Key Insight
The key insight is to take advantage of the fact that the input array is sorted and unique, allowing for efficient identification of continuous ranges by simply checking if the current number is consecutive to the next number. This simplifies the problem and enables a straightforward iterative solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-01-07 |
| 💻 Language | Python |