> 📌 **Cross-listed:** Primary location is [Array/3206-Alternating-Groups-I](../../Array/3206-Alternating-Groups-I). This problem also appears under: **Array**, **Sliding Window**

# 3206. Alternating Groups I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/alternating-groups-i/)


## 📝 Problem Description

There is a circle of red and blue tiles. You are given an array of integers `colors`. The color of tile `i` is represented by `colors[i]`:

	- `colors[i] == 0` means that tile `i` is **red**.

	- `colors[i] == 1` means that tile `i` is **blue**.

Every 3 contiguous tiles in the circle with **alternating** colors (the middle tile has a different color from its **left** and **right** tiles) is called an **alternating** group.

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.

 

Example 1:**

**Input:** colors = [1,1,1]

**Output:** 0

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-53-171.png)

Example 2:**

**Input:** colors = [0,1,0,0,1]

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-47-491.png)

Alternating groups:

![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-50-441.png)**![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-48-211.png)![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-49-351.png)**

 

**Constraints:**

	- `3 <= colors.length <= 100`

	- `0 <= colors[i] <= 1`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the number of alternating groups in a circular array of red and blue tiles. An alternating group consists of 3 contiguous tiles with alternating colors. We can solve this problem by iterating through the array and counting the number of times we find a group of 3 tiles with alternating colors.

**Approach**
1. Initialize variables to keep track of the result (res) and the length of the current group (l).
2. Iterate through the array using a sliding window approach, where the window size is 3.
3. For each window, check if the colors of the current tile and the previous tile are the same. If they are, reset the length of the current group (l) to the current index (r).
4. If the length of the current group (l) plus 1 is equal to 3, it means we have found an alternating group, so increment the result (res) and update the length of the current group (l).
5. Return the result (res) at the end of the iteration.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating through the array once, and the operations inside the loop are constant time.

**Space Complexity**
O(1), because we are using a constant amount of space to store the result and the length of the current group.

**Key Insight**
The key insight here is to use a sliding window approach with a window size of 3 to efficiently count the number of alternating groups in the array. By resetting the length of the current group whenever we find a group of 3 tiles with the same color, we can accurately count the number of alternating groups.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 50 ms (Beats 95.89%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-03-09 |
| 💻 Language | Python |