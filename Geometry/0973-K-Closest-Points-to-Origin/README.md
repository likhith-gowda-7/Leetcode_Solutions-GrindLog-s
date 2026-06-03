> 📌 **Cross-listed:** Primary location is [Array/0973-K-Closest-Points-to-Origin](../../Array/0973-K-Closest-Points-to-Origin). This problem also appears under: **Array**, **Math**, **Divide and Conquer**, **Geometry**, **Sorting**, **Heap (Priority Queue)**, **Quickselect**

# 973. K Closest Points to Origin


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Geometry](https://img.shields.io/badge/Geometry-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)


## 📝 Problem Description

Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `&radic;(x_1 - x_2)^2 + (y_1 - y_2)^2`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)
```

**Input:** points = [[1,3],[-2,2]], k = 1
**Output:** [[-2,2]]
**Explanation:**
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

```

Example 2:**

```

**Input:** points = [[3,3],[5,-1],[-2,4]], k = 2
**Output:** [[3,3],[-2,4]]
**Explanation:** The answer [[-2,4],[3,3]] would also be accepted.

```

 

**Constraints:**

	- `1 <= k <= points.length <= 10^4`

	- `-10^4 <= x_i, y_i <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses a priority queue (implemented using a heap) to efficiently select the k closest points to the origin. By storing the negative square of the distance (to simulate a max heap) and the point itself, the solution can quickly identify the k points with the smallest distance.

**Approach**
1. Initialize an empty heap to store the points along with their distances.
2. Iterate through each point in the input array.
3. For each point, calculate the negative square of its distance from the origin (to simulate a max heap).
4. If the heap is full (i.e., it contains k points), check if the point with the smallest distance in the heap is smaller than the current point's distance.
5. If it is, remove the smallest point from the heap and insert the current point.
6. If the heap is not full, simply insert the current point into the heap.
7. After iterating through all points, extract the k points with the smallest distances from the heap.

**Time Complexity**
O(n log k), where n is the number of points. The heap operations (insertion and removal) take O(log k) time, and we perform these operations n times.

**Space Complexity**
O(k), as we need to store the k closest points in the heap.

**Key Insight**
The key insight is to use a priority queue to efficiently select the k closest points. By storing the negative square of the distance, we can simulate a max heap and quickly identify the points with the smallest distance. This approach allows us to solve the problem in linear time with respect to the number of points, making it much more efficient than a naive approach that would involve sorting all points.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 60 ms (Beats 62.12%) |
| 💾 Memory | 22.4 MB (Beats 100%) |
| 📅 Solved | 2025-07-06 |
| 💻 Language | Python |