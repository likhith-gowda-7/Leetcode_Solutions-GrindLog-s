# 189. Rotate Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotate-array/)


## 📝 Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

 

Example 1:**

```

**Input:** nums = [1,2,3,4,5,6,7], k = 3
**Output:** [5,6,7,1,2,3,4]
**Explanation:**
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

```

Example 2:**

```

**Input:** nums = [-1,-100,3,99], k = 2
**Output:** [3,99,-1,-100]
**Explanation:** 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-2^31 <= nums[i] <= 2^31 - 1`

	- `0 <= k <= 10^5`

 

**Follow up:**

	- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.

	- Could you do it in-place with `O(1)` extra space?

## 🧠 Solution Explanation

## Intuition
The approach works by first reducing the number of rotations `k` to its equivalent within the length of the array `nums`, as any rotation beyond the length of the array is redundant. Then, it reverses the entire array and subsequently reverses the first `k` elements and the rest of the array to achieve the desired rotation.

## Approach
1. Calculate the effective number of rotations `k` by taking the modulus of `k` with the length of the array `nums`.
2. Reverse the entire array `nums`.
3. Reverse the first `k` elements of the reversed array.
4. Reverse the rest of the array (from index `k` to the end).

## Time Complexity
The time complexity is O(n), where n is the length of the array `nums`, because each element in the array is visited and reversed a constant number of times.

## Space Complexity
The space complexity is O(1), as the solution only uses a constant amount of space to store the variables and does not allocate any additional space that scales with the input size.

## Key Insight
The key insight is that rotating an array to the right by `k` steps is equivalent to reversing the entire array and then reversing the first `k` elements and the rest of the array, which simplifies the problem and allows for an efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 25.1 MB (Beats 100%) |
| 📅 Solved | 2024-12-16 |
| 💻 Language | Python |