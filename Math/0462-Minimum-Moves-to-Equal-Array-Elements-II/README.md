> 📌 **Cross-listed:** Primary location is [Array/0462-Minimum-Moves-to-Equal-Array-Elements-II](../../Array/0462-Minimum-Moves-to-Equal-Array-Elements-II). This problem also appears under: **Array**, **Math**, **Sorting**

# 462. Minimum Moves to Equal Array Elements II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)


## 📝 Problem Description

Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

In one move, you can increment or decrement an element of the array by `1`.

Test cases are designed so that the answer will fit in a **32-bit** integer.

 

Example 1:**

```

**Input:** nums = [1,2,3]
**Output:** 2
**Explanation:**
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

```

Example 2:**

```

**Input:** nums = [1,10,2,9]
**Output:** 16

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by finding the median of the array, which will be the target value that all elements will be moved towards. Since the median is the middle value in the sorted array, it has the property that at least half of the elements are less than or equal to it, and at least half of the elements are greater than or equal to it. This makes it the optimal target value to minimize the total number of moves.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Find the median of the sorted array, which will be the target value `target_element`.
3. Initialize a variable `min_ops` to store the minimum number of moves required.
4. Iterate through each element `val` in the sorted array and calculate the absolute difference between `val` and `target_element`. Add this difference to `min_ops`.
5. Return the total number of moves `min_ops`.

**Time Complexity**
O(n log n), where n is the number of elements in the array. This is because sorting the array takes O(n log n) time.

**Space Complexity**
O(1), excluding the space required for the input array. This is because the solution only uses a constant amount of extra space to store the target element and the minimum number of moves.

**Key Insight**
The key insight is that the median of the array is the optimal target value to minimize the total number of moves. This is because the median has the property that at least half of the elements are less than or equal to it, and at least half of the elements are greater than or equal to it, making it the value that requires the minimum number of moves to reach.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 78.76%) |
| 💾 Memory | 20.5 MB (Beats 14.8%) |
| 📅 Solved | 2026-05-17 |
| 💻 Language | Python |