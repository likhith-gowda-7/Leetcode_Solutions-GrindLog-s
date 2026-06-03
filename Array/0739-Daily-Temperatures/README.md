# 739. Daily Temperatures


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/daily-temperatures/)


## 📝 Problem Description

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `i^th` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

 

Example 1:**

```
**Input:** temperatures = [73,74,75,71,69,72,76,73]
**Output:** [1,1,4,2,1,1,0,0]

```
Example 2:**

```
**Input:** temperatures = [30,40,50,60]
**Output:** [1,1,1,0]

```
Example 3:**

```
**Input:** temperatures = [30,60,90]
**Output:** [1,1,0]

```

 

**Constraints:**

	- `1 <= temperatures.length <= 10^5`

	- `30 <= temperatures[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the days with temperatures that are yet to be surpassed by a warmer temperature. By iterating through the temperatures array, we can pop elements from the stack whenever we encounter a temperature that is higher than the one at the top of the stack, and update the corresponding answer array with the number of days to wait.

**Approach**
1. Initialize an answer array `res` of the same length as the input temperatures array, filled with zeros.
2. Initialize an empty stack `stack` to store tuples of (day, temperature).
3. Iterate through the temperatures array using `enumerate` to get both the index `curr_day` and the temperature `curr_temp`.
4. While the stack is not empty and the temperature at the top of the stack is less than the current temperature:
   - Pop the top element from the stack, which represents a day with a temperature that has been surpassed.
   - Update the answer array at the popped day's index with the difference between the current day and the popped day.
5. Push the current day and temperature onto the stack.
6. Return the answer array.

**Time Complexity**
O(n), where n is the length of the temperatures array. This is because we make a single pass through the array, and each operation (push, pop, comparison) takes constant time.

**Space Complexity**
O(n), where n is the length of the temperatures array. This is because in the worst case, we might need to store all elements in the stack.

**Key Insight**
The key insight is to use a stack to keep track of the days with temperatures that are yet to be surpassed, allowing us to efficiently pop elements and update the answer array whenever we encounter a warmer temperature. This approach takes advantage of the fact that the temperatures array is monotonic, meaning that once a temperature is surpassed, it will not be surpassed again.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 112 ms (Beats 31.11%) |
| 💾 Memory | 33.1 MB (Beats 27.57%) |
| 📅 Solved | 2025-11-15 |
| 💻 Language | Python |