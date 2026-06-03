# 3516. Find Closest Person


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-closest-person/)


## 📝 Problem Description

You are given three integers x`, y`, and z`, representing the positions of three people on a number line:

	x` is the position of Person 1.

	y` is the position of Person 2.

	z` is the position of Person 3, who does **not** move.

Both Person 1 and Person 2 move toward Person 3 at the **same** speed.

Determine which person reaches Person 3 **first**:

	Return 1 if Person 1 arrives first.

	Return 2 if Person 2 arrives first.

	Return 0 if both arrive at the **same** time.

Return the result accordingly.

 

Example 1:**

**Input:** x = 2, y = 7, z = 4

**Output:** 1

**Explanation:**

	Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.

	Person 2 is at position 7 and can reach Person 3 in 3 steps.

Since Person 1 reaches Person 3 first, the output is 1.

Example 2:**

**Input:** x = 2, y = 5, z = 6

**Output:** 2

**Explanation:**

	Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.

	Person 2 is at position 5 and can reach Person 3 in 1 step.

Since Person 2 reaches Person 3 first, the output is 2.

Example 3:**

**Input:** x = 1, y = 5, z = 3

**Output:** 0

**Explanation:**

	Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.

	Person 2 is at position 5 and can reach Person 3 in 2 steps.

Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.

 

**Constraints:**

	- `1 <= x, y, z <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by calculating the absolute difference in steps between each person and Person 3. Since both Person 1 and Person 2 move at the same speed, the person with the smaller absolute difference will reach Person 3 first.

**Approach**
1. Calculate the absolute difference in steps between Person 1 and Person 3 (`time1 = abs(z-x)`).
2. Calculate the absolute difference in steps between Person 2 and Person 3 (`time2 = abs(y-z)`).
3. Compare the two times:
   - If `time1` is less than `time2`, return 1 (Person 1 arrives first).
   - If `time2` is less than `time1`, return 2 (Person 2 arrives first).
   - If `time1` is equal to `time2`, return 0 (both arrive at the same time).

**Time Complexity**
O(1) - The solution involves a constant number of operations, regardless of the input values.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the input values and the calculated times.

**Key Insight**
The key insight is that the absolute difference in steps between two points on a number line is a direct measure of the time it takes to move from one point to the other at a constant speed. By comparing these differences, we can determine which person reaches Person 3 first.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-09-04 |
| 💻 Language | Python |