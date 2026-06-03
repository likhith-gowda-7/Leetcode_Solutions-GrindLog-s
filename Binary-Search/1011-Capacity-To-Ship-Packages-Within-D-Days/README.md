> 📌 **Cross-listed:** Primary location is [Array/1011-Capacity-To-Ship-Packages-Within-D-Days](../../Array/1011-Capacity-To-Ship-Packages-Within-D-Days). This problem also appears under: **Array**, **Binary Search**

# 1011. Capacity To Ship Packages Within D Days


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)


## 📝 Problem Description

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `i^th` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

 

Example 1:**

```

**Input:** weights = [1,2,3,4,5,6,7,8,9,10], days = 5
**Output:** 15
**Explanation:** A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

```

Example 2:**

```

**Input:** weights = [3,2,2,4,1,4], days = 3
**Output:** 6
**Explanation:** A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

```

Example 3:**

```

**Input:** weights = [1,2,3,1,1], days = 4
**Output:** 3
**Explanation:**
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

```

 

**Constraints:**

	- `1 <= days <= weights.length <= 5 * 10^4`

	- `1 <= weights[i] <= 500`

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the minimum weight capacity of the ship that will result in all packages being shipped within the given number of days. The idea is to find the smallest capacity that can ship all packages in the given number of days.

**Approach**
1. If there's only one day, return the sum of all weights as the minimum capacity.
2. Define a helper function `helper` that takes a mid capacity, weights, and days as input. It simulates shipping packages with the given capacity and returns True if more than the given number of days are required, False otherwise.
3. Initialize the left and right boundaries of the search space to the maximum weight and the sum of all weights, respectively.
4. Perform a binary search to find the minimum capacity that can ship all packages within the given number of days. In each iteration, calculate the mid capacity and check if it's sufficient using the `helper` function.
5. If the mid capacity is not sufficient, update the left boundary to mid + 1. Otherwise, update the right boundary to mid.
6. Return the left boundary as the minimum capacity.

**Time Complexity**
O(n log m), where n is the number of packages and m is the sum of all weights. The binary search takes O(log m) time, and the helper function takes O(n) time in the worst case.

**Space Complexity**
O(1), as the space complexity is constant and does not depend on the input size.

**Key Insight**
The key insight is to use a binary search approach to find the minimum capacity that can ship all packages within the given number of days. By simulating shipping packages with the given capacity and checking if it's sufficient, we can efficiently find the minimum capacity required.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 123 ms (Beats 99.47%) |
| 💾 Memory | 22.2 MB (Beats 100%) |
| 📅 Solved | 2025-03-02 |
| 💻 Language | Python |