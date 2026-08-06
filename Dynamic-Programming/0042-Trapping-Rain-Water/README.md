> 📌 **Cross-listed:** Primary location is [Array/0042-Trapping-Rain-Water](../../Array/0042-Trapping-Rain-Water). This problem also appears under: **Array**, **Two Pointers**, **Dynamic Programming**, **Stack**, **Monotonic Stack**

# 42. Trapping Rain Water


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/trapping-rain-water/)


## 📝 Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
```

**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]
**Output:** 6
**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

Example 2:**

```

**Input:** height = [4,2,0,3,2,5]
**Output:** 9

```

 

**Constraints:**

	- `n == height.length`

	- `1 <= n <= 2 * 10^4`

	- `0 <= height[i] <= 10^5`

## 🧠 Solution Explanation

## Intuition
The solution works by using two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. This approach allows us to calculate the trapped water by comparing the height of the current bar with the maximum height on the left and right sides. The key idea is to move the pointer that is pointing to the smaller bar, as the water trapped is determined by the smaller bar.

## Approach
1. Initialize two pointers, `l` and `r`, to the start and end of the elevation map, respectively.
2. Initialize `lm` and `rm` to the height of the bars at the `l` and `r` indices, respectively.
3. While `l` is less than `r`, compare `lm` and `rm` to determine which pointer to move.
4. If `lm` is less than `rm`, move the `l` pointer to the right and update `lm` to be the maximum of the current `lm` and the height of the bar at the new `l` index.
5. Add the difference between `lm` and the height of the bar at the new `l` index to the result, as this represents the trapped water.
6. Repeat steps 3-5 until `l` is no longer less than `r`.

## Time Complexity
The time complexity is O(n), where n is the number of bars in the elevation map, as we only need to traverse the map once.

## Space Complexity
The space complexity is O(1), as we only use a constant amount of space to store the pointers and the maximum heights.

## Key Insight
The key insight is that by moving the pointer that is pointing to the smaller bar, we can ensure that the water trapped is calculated correctly, as the water level is determined by the smaller bar. This allows us to avoid having to calculate the maximum height on both sides for each bar, reducing the time complexity to O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 84.04%) |
| 💾 Memory | 21.1 MB (Beats 48.35%) |
| 📅 Solved | 2026-08-06 |
| 💻 Language | Python |