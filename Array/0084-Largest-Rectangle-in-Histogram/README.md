# 84. Largest Rectangle in Histogram


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/)


## 📝 Problem Description

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return *the area of the largest rectangle in the histogram*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)
```

**Input:** heights = [2,1,5,6,2,3]
**Output:** 10
**Explanation:** The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)
```

**Input:** heights = [2,4]
**Output:** 4

```

 

**Constraints:**

	- `1 <= heights.length <= 10^5`

	- `0 <= heights[i] <= 10^4`

## 🧠 Solution Explanation

## Intuition
The solution works by using a monotonic stack to keep track of the indices and heights of the bars in the histogram. This approach allows us to efficiently calculate the area of the largest rectangle that can be formed with each bar as the smallest bar. The key idea is to pop bars from the stack when a smaller bar is encountered and calculate the area of the rectangle that can be formed with the popped bar as the smallest bar.

## Approach
1. Initialize an empty stack to store the indices and heights of the bars.
2. Iterate through the histogram, and for each bar, pop all the bars from the stack that are higher than the current bar.
3. For each popped bar, calculate the area of the rectangle that can be formed with the popped bar as the smallest bar.
4. Update the maximum area if the calculated area is larger.
5. Push the current bar onto the stack with its index as the reachable till index.
6. After iterating through the histogram, pop all the remaining bars from the stack and calculate the area of the rectangle that can be formed with each bar as the smallest bar.

## Time Complexity
The time complexity is O(n), where n is the number of bars in the histogram. This is because each bar is pushed and popped from the stack exactly once.

## Space Complexity
The space complexity is O(n), where n is the number of bars in the histogram. This is because in the worst case, all bars are pushed onto the stack.

## Key Insight
The key insight is to use a monotonic stack to keep track of the indices and heights of the bars, allowing us to efficiently calculate the area of the largest rectangle that can be formed with each bar as the smallest bar. This approach enables us to solve the problem in linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 144 ms (Beats 24.44%) |
| 💾 Memory | 36.2 MB (Beats 27.86%) |
| 📅 Solved | 2025-11-17 |
| 💻 Language | Python |