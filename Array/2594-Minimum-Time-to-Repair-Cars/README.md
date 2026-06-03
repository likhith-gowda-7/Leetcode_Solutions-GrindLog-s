# 2594. Minimum Time to Repair Cars


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-time-to-repair-cars/)


## 📝 Problem Description

You are given an integer array `ranks` representing the **ranks** of some mechanics. ranks_i is the rank of the i^th mechanic. A mechanic with a rank `r` can repair n cars in `r * n^2` minutes.

You are also given an integer `cars` representing the total number of cars waiting in the garage to be repaired.

Return *the **minimum** time taken to repair all the cars.*

**Note:** All the mechanics can repair the cars simultaneously.

 

Example 1:**

```

**Input:** ranks = [4,2,3,1], cars = 10
**Output:** 16
**Explanation:** 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

```

Example 2:**

```

**Input:** ranks = [5,1,8], cars = 6
**Output:** 16
**Explanation:** 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

```

 

**Constraints:**

	- `1 <= ranks.length <= 10^5`

	- `1 <= ranks[i] <= 100`

	- `1 <= cars <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution uses binary search to find the minimum time required to repair all the cars. The key insight is that the time required to repair all the cars is a function of the ranks of the mechanics and the number of cars. We can use binary search to find the minimum time by iterating through the possible times and checking if it's sufficient to repair all the cars.

**Approach**
1. Initialize the minimum and maximum possible times to repair all the cars. The minimum time is the time taken by the mechanic with the lowest rank to repair all the cars, while the maximum time is the time taken by the mechanic with the highest rank to repair all the cars.
2. Perform a binary search on the possible times. For each mid value, calculate the total number of cars that can be repaired by each mechanic.
3. If the total number of cars that can be repaired is greater than or equal to the total number of cars, update the maximum time to mid - 1. Otherwise, update the minimum time to mid + 1.
4. Repeat steps 2-3 until the minimum and maximum times converge.

**Time Complexity**
O(n log m), where n is the number of mechanics and m is the maximum possible time to repair all the cars. The binary search takes O(log m) time, and the calculation of the total number of cars that can be repaired by each mechanic takes O(n) time.

**Space Complexity**
O(1), as we only use a constant amount of space to store the minimum and maximum times, and the mid value.

**Key Insight**
The key insight is that the time required to repair all the cars is a function of the ranks of the mechanics and the number of cars. By using binary search, we can efficiently find the minimum time required to repair all the cars.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 347 ms (Beats 77.53%) |
| 💾 Memory | 21.8 MB (Beats 100%) |
| 📅 Solved | 2025-03-16 |
| 💻 Language | Python |