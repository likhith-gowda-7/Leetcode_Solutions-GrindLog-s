> 📌 **Cross-listed:** Primary location is [Array/0407-Trapping-Rain-Water-II](../../Array/0407-Trapping-Rain-Water-II). This problem also appears under: **Array**, **Breadth-First Search**, **Heap (Priority Queue)**, **Matrix**

# 407. Trapping Rain Water II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/trapping-rain-water-ii/)


## 📝 Problem Description

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return *the volume of water it can trap after raining*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg)
```

**Input:** heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
**Output:** 4
**Explanation:** After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg)
```

**Input:** heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
**Output:** 10

```

 

**Constraints:**

	- `m == heightMap.length`

	- `n == heightMap[i].length`

	- `1 <= m, n <= 200`

	- `0 <= heightMap[i][j] <= 2 * 10^4`

## 🧠 Solution Explanation

### Intuition
The solution to this problem works by using a priority queue (min-heap) to keep track of the cells with the minimum height that have been visited. This approach ensures that we always process the cell with the smallest height first, which is crucial in determining the amount of water that can be trapped. By starting with the border cells and gradually moving inwards, we can effectively simulate the process of water flowing into the area.

### Approach
1. Initialize a min-heap with all the border cells of the height map, marking them as visited.
2. While the min-heap is not empty, remove the cell with the minimum height and update the maximum height encountered so far.
3. Calculate the amount of water that can be trapped at the current cell by subtracting its height from the maximum height.
4. Add all unvisited neighboring cells to the min-heap and mark them as visited.
5. Repeat steps 2-4 until all cells have been processed.

### Time Complexity
The time complexity of this solution is O(m * n * log(m * n)), where m and n are the dimensions of the height map. This is because each cell is added to the min-heap once, and the heap operations (insertion and removal) take O(log(m * n)) time.

### Space Complexity
The space complexity of this solution is O(m * n), where m and n are the dimensions of the height map. This is because in the worst case, all cells might be stored in the min-heap at the same time.

### Key Insight
The key insight behind this solution is the use of a min-heap to prioritize the cells with the smallest height, allowing us to simulate the process of water flowing into the area and calculate the amount of water that can be trapped. By starting with the border cells and moving inwards, we can effectively determine the maximum height of the "walls" that surround each cell, which is essential in calculating the amount of water that can be trapped.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 151 ms (Beats 17.25%) |
| 💾 Memory | 20 MB (Beats 100%) |
| 📅 Solved | 2025-10-04 |
| 💻 Language | Python |