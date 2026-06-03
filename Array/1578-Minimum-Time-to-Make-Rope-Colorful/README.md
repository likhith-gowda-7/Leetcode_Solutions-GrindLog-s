# 1578. Minimum Time to Make Rope Colorful


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)


## 📝 Problem Description

Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string `colors` where `colors[i]` is the color of the `i^th` balloon.

Alice wants the rope to be **colorful**. She does not want **two consecutive balloons** to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it **colorful**. You are given a **0-indexed** integer array `neededTime` where `neededTime[i]` is the time (in seconds) that Bob needs to remove the `i^th` balloon from the rope.

Return *the **minimum time** Bob needs to make the rope **colorful***.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg)
```

**Input:** colors = "abaac", neededTime = [1,2,3,4,5]
**Output:** 3
**Explanation:** In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg)
```

**Input:** colors = "abc", neededTime = [1,2,3]
**Output:** 0
**Explanation:** The rope is already colorful. Bob does not need to remove any balloons from the rope.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg)
```

**Input:** colors = "aabaa", neededTime = [1,2,3,4,1]
**Output:** 2
**Explanation:** Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

```

 

**Constraints:**

	- `n == colors.length == neededTime.length`

	- `1 <= n <= 10^5`

	- `1 <= neededTime[i] <= 10^4`

	- `colors` contains only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The key insight here is that we can break down the problem into smaller subproblems by considering each color group separately. We want to minimize the time spent by Bob in removing balloons from each group, while ensuring that no two consecutive balloons are of the same color.

**Approach**
1. Initialize variables to keep track of the minimum time spent so far (`min_time`), the current time spent in the current color group (`curr`), and the maximum time spent in the current color group (`maxi`).
2. Iterate through the `colors` string and the `neededTime` array simultaneously.
3. If the current balloon is of the same color as the previous one, add its time to `curr` and update `maxi` if necessary.
4. If the current balloon is of a different color, calculate the time spent in the previous color group by subtracting `maxi` from `curr`, add this to `min_time`, and reset `curr` and `maxi` for the new color group.
5. After the loop, add the time spent in the last color group to `min_time` and return the result.

**Time Complexity**
O(n), where n is the length of the `colors` string, since we only iterate through the string once.

**Space Complexity**
O(1), since we only use a constant amount of space to store the variables `min_time`, `curr`, and `maxi`.

**Key Insight**
The key insight is to recognize that we can minimize the time spent by Bob by considering each color group separately and minimizing the time spent in each group. This is achieved by keeping track of the maximum time spent in each group and subtracting it from the total time spent in the group to get the minimum time spent.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 87 ms (Beats 48.14%) |
| 💾 Memory | 26.4 MB (Beats 100%) |
| 📅 Solved | 2025-11-03 |
| 💻 Language | Python |