> 📌 **Cross-listed:** Primary location is [Array/3024-Type-of-Triangle](../../Array/3024-Type-of-Triangle). This problem also appears under: **Array**, **Math**, **Sorting**

# 3024. Type of Triangle


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/type-of-triangle/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` of size `3` which can form the sides of a triangle.

	- A triangle is called **equilateral** if it has all sides of equal length.

	- A triangle is called **isosceles** if it has exactly two sides of equal length.

	- A triangle is called **scalene** if all its sides are of different lengths.

Return *a string representing* *the type of triangle that can be formed **or *`"none"`* if it **cannot** form a triangle.*

 

Example 1:**

```

**Input:** nums = [3,3,3]
**Output:** "equilateral"
**Explanation:** Since all the sides are of equal length, therefore, it will form an equilateral triangle.

```

Example 2:**

```

**Input:** nums = [3,4,5]
**Output:** "scalene"
**Explanation:** 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.

```

 

**Constraints:**

	- `nums.length == 3`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the input array in ascending order. This allows us to easily determine the type of triangle that can be formed based on the lengths of the sides. The key insight is that a triangle can be formed if the sum of the lengths of any two sides is greater than the length of the third side.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Check if the sum of the lengths of the two smallest sides is less than or equal to the length of the largest side. If so, return "none" as it's impossible to form a triangle.
3. Iterate through the sorted array to check for the following conditions:
	* If all sides are equal, return "equilateral".
	* If exactly two sides are equal and the third side is different, return "isosceles".
	* If all sides are different, return "scalene".

**Time Complexity**
O(n log n) due to the sorting operation, where n is the number of elements in the input array.

**Space Complexity**
O(n) for the sorting operation, where n is the number of elements in the input array.

**Key Insight**
The key to this solution is the triangle inequality theorem, which states that a triangle can be formed if the sum of the lengths of any two sides is greater than the length of the third side. By sorting the input array and checking for this condition, we can efficiently determine the type of triangle that can be formed.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-05-19 |
| 💻 Language | Python |