> 📌 **Cross-listed:** Primary location is [Array/0011-Container-With-Most-Water](../../Array/0011-Container-With-Most-Water). This problem also appears under: **Array**, **Two Pointers**, **Greedy**

# 11. Container With Most Water


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/container-with-most-water/)


## 📝 Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i^th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

 

Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
```

**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

Example 2:**

```

**Input:** height = [1,1]
**Output:** 1

```

 

**Constraints:**

	- `n == height.length`

	- `2 <= n <= 10^5`

	- `0 <= height[i] <= 10^4`

## 🧠 Solution Explanation

## Intuition
The solution works by using a two-pointer approach, starting from both ends of the array and moving towards the center. This approach is effective because the area of the container is determined by the shorter line, so moving the pointer of the shorter line towards the center has the potential to increase the area. The key idea is to maximize the area by considering all possible pairs of lines.

## Approach
1. Initialize two pointers, `L` and `R`, to the start and end of the array, respectively.
2. Calculate the area of the container formed by the lines at `L` and `R` by multiplying the distance between them (`R - L`) by the height of the shorter line (`min(height[L], height[R])`).
3. Update the maximum area if the calculated area is greater than the current maximum.
4. Move the pointer of the shorter line towards the center by incrementing `L` if `height[L] < height[R]`, or decrementing `R` otherwise.
5. Repeat steps 2-4 until `L` meets or crosses `R`.

## Time Complexity
The time complexity is O(n), where n is the length of the input array, because each element is visited at most once by the two pointers.

## Space Complexity
The space complexity is O(1), because only a constant amount of space is used to store the pointers and the maximum area, regardless of the input size.

## Key Insight
The key insight is that moving the pointer of the shorter line towards the center has the potential to increase the area, because the area is determined by the shorter line. This greedy approach allows us to find the maximum area in a single pass through the array, making the solution efficient and scalable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 75 ms (Beats 5.13%) |
| 💾 Memory | 28.5 MB (Beats 99.88%) |
| 📅 Solved | 2025-10-05 |
| 💻 Language | Python |