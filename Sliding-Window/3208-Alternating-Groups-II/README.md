> 📌 **Cross-listed:** Primary location is [Array/3208-Alternating-Groups-II](../../Array/3208-Alternating-Groups-II). This problem also appears under: **Array**, **Sliding Window**

# 3208. Alternating Groups II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/alternating-groups-ii/)


## 📝 Problem Description

There is a circle of red and blue tiles. You are given an array of integers `colors` and an integer `k`. The color of tile `i` is represented by `colors[i]`:

	- `colors[i] == 0` means that tile `i` is **red**.

	- `colors[i] == 1` means that tile `i` is **blue**.

An **alternating** group is every `k` contiguous tiles in the circle with **alternating** colors (each tile in the group except the first and last one has a different color from its **left** and **right** tiles).

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.

 

Example 1:**

**Input:** colors = [0,1,0,1,0], k = 3

**Output:** 3

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183519.png)**

Alternating groups:

![](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182448.png)![](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182844.png)![](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-183057.png)

Example 2:**

**Input:** colors = [0,1,0,0,1,0,1], k = 6

**Output:** 2

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183907.png)**

Alternating groups:

![](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184128.png)![](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184240.png)

Example 3:**

**Input:** colors = [1,1,0,1], k = 4

**Output:** 0

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184516.png)

 

**Constraints:**

	- `3 <= colors.length <= 10^5`

	- `0 <= colors[i] <= 1`

	- `3 <= k <= colors.length`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a sliding window of size `k` and counting the number of times the colors inside the window alternate. The key insight is that when the colors inside the window stop alternating, we can reset the window to the next tile and start counting again.

**Approach**
1. First, we append the first `k-1` elements of the `colors` array to the end of the array to form a circle.
2. We initialize two pointers, `l` and `r`, to the start of the array and a variable `res` to count the number of alternating groups.
3. We iterate through the array with the `r` pointer, and for each tile, we check if the color is the same as the previous tile. If it is, we reset the `l` pointer to the current `r` index.
4. When the window size (`r-l+1`) equals `k`, we increment the `l` pointer and the `res` counter, indicating that we have found an alternating group.
5. We repeat steps 3-4 until we reach the end of the array.

**Time Complexity**
O(n), where n is the length of the `colors` array. This is because we make a single pass through the array.

**Space Complexity**
O(n), where n is the length of the `colors` array. This is because we append the first `k-1` elements of the `colors` array to the end of the array.

**Key Insight**
The key insight is that when the colors inside the window stop alternating, we can reset the window to the next tile and start counting again. This allows us to efficiently count the number of alternating groups in the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 724 ms (Beats 14.85%) |
| 💾 Memory | 22.6 MB (Beats 43.75%) |
| 📅 Solved | 2025-03-09 |
| 💻 Language | Python |