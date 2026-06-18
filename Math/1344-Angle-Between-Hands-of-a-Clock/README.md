# 1344. Angle Between Hands of a Clock


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/)


## 📝 Problem Description

Given two numbers, `hour` and `minutes`, return *the smaller angle (in degrees) formed between the *`hour`* and the *`minute`* hand*.

Answers within `10^-5` of the actual value will be accepted as correct.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/26/sample_1_1673.png)
```

**Input:** hour = 12, minutes = 30
**Output:** 165

```

Example 2:**

![](https://assets.leetcode.com/uploads/2019/12/26/sample_2_1673.png)
```

**Input:** hour = 3, minutes = 30
**Output:** 75

```

Example 3:**

![](https://assets.leetcode.com/uploads/2019/12/26/sample_3_1673.png)
```

**Input:** hour = 3, minutes = 15
**Output:** 7.5

```

 

**Constraints:**

	- `1 <= hour <= 12`

	- `0 <= minutes <= 59`

## 🧠 Solution Explanation

**Intuition**
The solution uses a mathematical formula to calculate the smaller angle between the hour and minute hands of a clock. The formula is derived from the fact that the hour hand moves 30 degrees per hour and the minute hand moves 6 degrees per minute.

**Approach**
1. The formula `(30 * hour) - (5.5 * minutes)` calculates the absolute difference in degrees between the positions of the hour and minute hands.
2. The `abs` function ensures that the result is always positive, regardless of the direction of the angle.
3. To find the smaller angle, the solution returns the minimum of the calculated angle and its supplement (360 - angle).

**Time Complexity**
O(1) - The solution involves a constant number of operations, regardless of the input values.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the input values and the result.

**Key Insight**
The key insight is that the angle between the hour and minute hands can be calculated using a simple mathematical formula, which takes into account the relative speeds of the two hands. This formula allows for a concise and efficient solution to the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 45.03%) |
| 📅 Solved | 2026-06-18 |
| 💻 Language | Python |