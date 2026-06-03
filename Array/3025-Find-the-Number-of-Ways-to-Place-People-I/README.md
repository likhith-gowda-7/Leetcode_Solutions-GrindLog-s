# 3025. Find the Number of Ways to Place People I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Geometry](https://img.shields.io/badge/Geometry-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/)


## 📝 Problem Description

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D plane, where `points[i] = [x_i, y_i]`.

Count the number of pairs of points `(A, B)`, where

	- `A` is on the **upper left** side of `B`, and

	- there are no other points in the rectangle (or line) they make (**including the border**), except for the points `A` and `B`.

Return the count.

 

Example 1:**

**Input:** points = [[1,1],[2,2],[3,3]]

**Output:** 0

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/01/04/example1alicebob.png)

There is no way to choose `A` and `B` such that `A` is on the upper left side of `B`.

Example 2:**

**Input:** points = [[6,2],[4,4],[2,6]]

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/25/t2.jpg)

	- The left one is the pair `(points[1], points[0])`, where `points[1]` is on the upper left side of `points[0]` and the rectangle is empty.

	- The middle one is the pair `(points[2], points[1])`, same as the left one it is a valid pair.

	- The right one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]`, but `points[1]` is inside the rectangle so it's not a valid pair.

Example 3:**

**Input:** points = [[3,1],[1,3],[1,1]]

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/25/t3.jpg)

	- The left one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]` and there are no other points on the line they form. Note that it is a valid state when the two points form a line.

	- The middle one is the pair `(points[1], points[2])`, it is a valid pair same as the left one.

	- The right one is the pair `(points[1], points[0])`, it is not a valid pair as `points[2]` is on the border of the rectangle.

 

**Constraints:**

	- `2 <= n <= 50`

	- `points[i].length == 2`

	- `0 <= points[i][0], points[i][1] <= 50`

	- All `points[i]` are distinct.

## 🧠 Solution Explanation

**Intuition**
The solution works by sorting the points based on their x-coordinates in descending order and then iterating through each pair of points. For each pair, it checks if there are any other points to the right of the current point and below the current point. If such a point exists, it increments the count of valid pairs.

**Approach**
1. Sort the points based on their x-coordinates in descending order.
2. Initialize a variable `max_y` to store the maximum y-coordinate of the points to the right of the current point.
3. Iterate through each pair of points. For each pair, check if there are any other points to the right of the current point and below the current point.
4. If such a point exists, increment the count of valid pairs and update `max_y` to store the maximum y-coordinate of the points to the right of the current point.
5. Return the count of valid pairs.

**Time Complexity**
O(n^2) - The solution has a nested loop structure, where the outer loop iterates through each point and the inner loop checks for other points to the right and below the current point. This results in a quadratic time complexity.

**Space Complexity**
O(1) - The solution only uses a constant amount of space to store the `count` variable and the `max_y` variable, regardless of the input size.

**Key Insight**
The key insight behind this solution is to take advantage of the sorted order of the points based on their x-coordinates. By iterating through each pair of points and checking for other points to the right and below the current point, we can efficiently count the number of valid pairs. This approach avoids the need to check all possible pairs of points, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 67.24%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-09-03 |
| 💻 Language | Python |