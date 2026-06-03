# 1929. Concatenation of Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/concatenation-of-array/)


## 📝 Problem Description

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return *the array *`ans`.

 

Example 1:**

```

**Input:** nums = [1,2,1]
**Output:** [1,2,1,1,2,1]
**Explanation:** The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

Example 2:**

```

**Input:** nums = [1,3,2,1]
**Output:** [1,3,2,1,1,3,2,1]
**Explanation:** The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 1000`

	- `1 <= nums[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to create a new array `ans` that is the concatenation of the input array `nums` with itself. This means we need to create a new array that contains all the elements of `nums` followed by all the elements of `nums` again.

**Approach**
To solve this problem, we can simply create a new array that is the concatenation of `nums` with itself. This can be done by using the `+` operator in Python, which concatenates two lists.

1. Create a new list `nums` that is the concatenation of the input array `nums` with itself.
2. Return the new list `nums`.

**Time Complexity**
The time complexity of this solution is O(n), where n is the length of the input array `nums`. This is because we are creating a new list that is the concatenation of `nums` with itself, which takes linear time.

**Space Complexity**
The space complexity of this solution is O(n), where n is the length of the input array `nums`. This is because we are creating a new list that is the concatenation of `nums` with itself, which requires additional space proportional to the length of `nums`.

**Key Insight**
The key insight here is that we can use the `+` operator in Python to concatenate two lists, which makes the solution very simple and efficient. This is a common pattern in programming, where we can use built-in operators or functions to simplify complex operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-11-13 |
| 💻 Language | Python |