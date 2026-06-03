# 3495. Minimum Operations to Make Array Elements Zero


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/)


## 📝 Problem Description

You are given a 2D array `queries`, where `queries[i]` is of the form `[l, r]`. Each `queries[i]` defines an array of integers `nums` consisting of elements ranging from `l` to `r`, both **inclusive**.

In one operation, you can:

	- Select two integers `a` and `b` from the array.

	- Replace them with `floor(a / 4)` and `floor(b / 4)`.

Your task is to determine the **minimum** number of operations required to reduce all elements of the array to zero for each query. Return the sum of the results for all queries.

 

Example 1:**

**Input:** queries = [[1,2],[2,4]]

**Output:** 3

**Explanation:**

For `queries[0]`:

	- The initial array is `nums = [1, 2]`.

	- In the first operation, select `nums[0]` and `nums[1]`. The array becomes `[0, 0]`.

	- The minimum number of operations required is 1.

For `queries[1]`:

	- The initial array is `nums = [2, 3, 4]`.

	- In the first operation, select `nums[0]` and `nums[2]`. The array becomes `[0, 3, 1]`.

	- In the second operation, select `nums[1]` and `nums[2]`. The array becomes `[0, 0, 0]`.

	- The minimum number of operations required is 2.

The output is `1 + 2 = 3`.

Example 2:**

**Input:** queries = [[2,6]]

**Output:** 4

**Explanation:**

For `queries[0]`:

	- The initial array is `nums = [2, 3, 4, 5, 6]`.

	- In the first operation, select `nums[0]` and `nums[3]`. The array becomes `[0, 3, 4, 1, 6]`.

	- In the second operation, select `nums[2]` and `nums[4]`. The array becomes `[0, 3, 1, 1, 1]`.

	- In the third operation, select `nums[1]` and `nums[2]`. The array becomes `[0, 0, 0, 1, 1]`.

	- In the fourth operation, select `nums[3]` and `nums[4]`. The array becomes `[0, 0, 0, 0, 0]`.

	- The minimum number of operations required is 4.

The output is 4.

 

**Constraints:**

	- `1 <= queries.length <= 10^5`

	- `queries[i].length == 2`

	- `queries[i] == [l, r]`

	- `1 <= l < r <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a power map to store the minimum number of operations required to reduce all elements in a range to zero. The power map is constructed by iterating over the powers of 4, where each power represents the number of operations required to reduce an element to zero. The solution then iterates over the queries and uses the power map to calculate the minimum number of operations required for each query.

**Approach**
1. Construct a power map by iterating over the powers of 4, where each power represents the number of operations required to reduce an element to zero.
2. For each query, traverse the power map to identify the ranges that the query belongs to.
3. For each range, calculate the number of elements in the range and the number of operations required to reduce all elements in the range to zero.
4. Add the number of operations required for each range to the total number of operations.
5. Divide the total number of operations by 2 and round up to the nearest integer to get the minimum number of operations required for the query.

**Time Complexity**
O(n * m), where n is the number of queries and m is the maximum range size. The solution iterates over the queries and the power map, where each iteration takes constant time.

**Space Complexity**
O(m), where m is the maximum range size. The solution stores the power map, which has a size of O(m).

**Key Insight**
The key insight is that the number of operations required to reduce an element to zero is proportional to the power of 4 of the element. By constructing a power map and iterating over the queries, the solution can efficiently calculate the minimum number of operations required for each query.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1516 ms (Beats 25.53%) |
| 💾 Memory | 54.4 MB (Beats 100%) |
| 📅 Solved | 2025-09-07 |
| 💻 Language | Python |