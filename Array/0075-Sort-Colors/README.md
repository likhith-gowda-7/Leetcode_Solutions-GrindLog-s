# 75. Sort Colors


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sort-colors/)


## 📝 Problem Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm) **so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:**

```

**Input:** nums = [2,0,2,1,1,0]
**Output:** [0,0,1,1,2,2]

```

Example 2:**

```

**Input:** nums = [2,0,1]
**Output:** [0,1,2]

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 300`

	- `nums[i]` is either `0`, `1`, or `2`.

 

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

## 🧠 Solution Explanation

## Intuition
This approach works by first counting the frequency of each color in the array, and then reconstructing the array in the correct order based on these counts. By using a separate count array, we can efficiently keep track of the number of each color and place them in the correct positions.

## Approach
1. Initialize a count array of size 3 to store the frequency of each color (0, 1, and 2).
2. Iterate through the input array and increment the corresponding count in the count array for each color encountered.
3. Iterate through the count array and for each non-zero count, place the corresponding color in the input array, decrementing the count and incrementing the index.

## Time Complexity
The time complexity is O(n), where n is the number of elements in the input array. This is because we make two passes through the input array: one to count the frequencies and another to reconstruct the array.

## Space Complexity
The space complexity is O(1), as we use a fixed-size count array of size 3, regardless of the size of the input array.

## Key Insight
The key insight here is that we can solve this problem in linear time and constant extra space by using a count array to keep track of the frequency of each color, allowing us to efficiently reconstruct the array in the correct order. This approach avoids the need for explicit sorting or swapping of elements.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 22.49%) |
| 📅 Solved | 2026-01-28 |
| 💻 Language | Python |