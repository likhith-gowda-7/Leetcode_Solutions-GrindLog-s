> 📌 **Cross-listed:** Primary location is [Array/3027-Find-the-Number-of-Ways-to-Place-People-II](../../Array/3027-Find-the-Number-of-Ways-to-Place-People-II). This problem also appears under: **Array**, **Math**, **Geometry**, **Sorting**, **Enumeration**

# 3027. Find the Number of Ways to Place People II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Geometry](https://img.shields.io/badge/Geometry-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/)


## 📝 Problem Description

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x_i, y_i]`.

We define the **right** direction as positive x-axis (**increasing x-coordinate**) and the **left** direction as negative x-axis (**decreasing x-coordinate**). Similarly, we define the **up** direction as positive y-axis (**increasing y-coordinate**) and the **down** direction as negative y-axis (**decreasing y-coordinate**)

You have to place `n` people, including Alice and Bob, at these points such that there is **exactly one** person at every point. Alice wants to be alone with Bob, so Alice will build a rectangular fence with Alice's position as the **upper left corner** and Bob's position as the **lower right corner** of the fence (**Note** that the fence **might not** enclose any area, i.e. it can be a line). If any person other than Alice and Bob is either **inside** the fence or **on** the fence, Alice will be sad.

Return *the number of **pairs of points** where you can place Alice and Bob, such that Alice **does not** become sad on building the fence*.

**Note** that Alice can only build a fence with Alice's position as the upper left corner, and Bob's position as the lower right corner. For example, Alice cannot build either of the fences in the picture below with four corners `(1, 1)`, `(1, 3)`, `(3, 1)`, and `(3, 3)`, because:

	- With Alice at `(3, 3)` and Bob at `(1, 1)`, Alice's position is not the upper left corner and Bob's position is not the lower right corner of the fence.

	- With Alice at `(1, 3)` and Bob at `(1, 1)` (as the rectangle shown in the image instead of a line), Bob's position is not the lower right corner of the fence.

![](https://assets.leetcode.com/uploads/2024/01/04/example0alicebob-1.png)
 

Example 1:**

![](https://assets.leetcode.com/uploads/2024/01/04/example1alicebob.png)
```

**Input:** points = [[1,1],[2,2],[3,3]]
**Output:** 0
**Explanation:** There is no way to place Alice and Bob such that Alice can build a fence with Alice's position as the upper left corner and Bob's position as the lower right corner. Hence we return 0. 

```

Example 2:**

![](https://assets.leetcode.com/uploads/2024/02/04/example2alicebob.png)
```

**Input:** points = [[6,2],[4,4],[2,6]]
**Output:** 2
**Explanation:** There are two ways to place Alice and Bob such that Alice will not be sad:
- Place Alice at (4, 4) and Bob at (6, 2).
- Place Alice at (2, 6) and Bob at (4, 4).
You cannot place Alice at (2, 6) and Bob at (6, 2) because the person at (4, 4) will be inside the fence.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2024/02/04/example4alicebob.png)
```

**Input:** points = [[3,1],[1,3],[1,1]]
**Output:** 2
**Explanation:** There are two ways to place Alice and Bob such that Alice will not be sad:
- Place Alice at (1, 1) and Bob at (3, 1).
- Place Alice at (1, 3) and Bob at (1, 1).
You cannot place Alice at (1, 3) and Bob at (3, 1) because the person at (1, 1) will be on the fence.
Note that it does not matter if the fence encloses any area, the first and second fences in the image are valid.

```

 

**Constraints:**

	- `2 <= n <= 1000`

	- `points[i].length == 2`

	- `-10^9 <= points[i][0], points[i][1] <= 10^9`

	- All `points[i]` are distinct.

## 🧠 Solution Explanation

**Intuition**
The solution works by sorting the points based on their x-coordinates and then iterating through the sorted points to find pairs of points that can form a valid rectangular fence for Alice and Bob. The key insight is to find the maximum y-coordinate for each pair of points to ensure that the rectangular fence is valid.

**Approach**
1. Sort the points based on their x-coordinates and then by their y-coordinates in descending order.
2. Initialize a counter `count` to store the number of valid pairs of points.
3. Iterate through the sorted points, starting from the first point.
4. For each point, iterate through the remaining points to find a point that can form a valid pair.
5. Check if the current point's y-coordinate is greater than or equal to the y-coordinate of the next point and also greater than the maximum y-coordinate found so far.
6. If the condition is met, increment the `count` and update the maximum y-coordinate.
7. Return the total count of valid pairs.

**Time Complexity**
O(n^2) - The solution has a nested loop structure, where the outer loop iterates through the points and the inner loop also iterates through the points. This results in a quadratic time complexity.

**Space Complexity**
O(n log n) - The solution sorts the points using the `sort` method, which has a time complexity of O(n log n) in Python. This results in a space complexity of O(n log n) due to the sorting operation.

**Key Insight**
The key insight is to find the maximum y-coordinate for each pair of points to ensure that the rectangular fence is valid. This is achieved by iterating through the points and keeping track of the maximum y-coordinate found so far.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1458 ms (Beats 57.89%) |
| 💾 Memory | 18.3 MB (Beats 100%) |
| 📅 Solved | 2025-09-03 |
| 💻 Language | Python |