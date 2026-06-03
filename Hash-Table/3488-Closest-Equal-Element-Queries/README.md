> 📌 **Cross-listed:** Primary location is [Array/3488-Closest-Equal-Element-Queries](../../Array/3488-Closest-Equal-Element-Queries). This problem also appears under: **Array**, **Hash Table**, **Binary Search**

# 3488. Closest Equal Element Queries


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/closest-equal-element-queries/)


## 📝 Problem Description

You are given a **circular** array `nums` and an array `queries`.

For each query `i`, you have to find the following:

	- The **minimum** distance between the element at index `queries[i]` and **any** other index `j` in the **circular** array, where `nums[j] == nums[queries[i]]`. If no such index exists, the answer for that query should be -1.

Return an array `answer` of the **same** size as `queries`, where `answer[i]` represents the result for query `i`.

 

Example 1:**

**Input:** nums = [1,3,1,4,1,3,2], queries = [0,3,5]

**Output:** [2,-1,3]

**Explanation:**

	- Query 0: The element at `queries[0] = 0` is `nums[0] = 1`. The nearest index with the same value is 2, and the distance between them is 2.

	- Query 1: The element at `queries[1] = 3` is `nums[3] = 4`. No other index contains 4, so the result is -1.

	- Query 2: The element at `queries[2] = 5` is `nums[5] = 3`. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: `5 -> 6 -> 0 -> 1`).

Example 2:**

**Input:** nums = [1,2,3,4], queries = [0,1,2,3]

**Output:** [-1,-1,-1,-1]

**Explanation:**

Each value in `nums` is unique, so no index shares the same value as the queried element. This results in -1 for all queries.

 

**Constraints:**

	- `1 <= queries.length <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`

	- `0 <= queries[i] < nums.length`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a hash table to store the indices of each unique element in the circular array. It then applies binary search to find the minimum distance between the query index and any other index with the same value. The key insight is that the circular array can be treated as a linear array by considering the indices modulo the array length.

**Approach**
1. Create a hash table `h1` to store the indices of each unique element in the circular array `nums`.
2. Initialize an empty list `res` to store the results for each query.
3. Iterate through each query `i` in `queries`.
4. For each query, find the value `val` at the query index `q`.
5. Get the list of indices `h1[val]` for the value `val`.
6. If there are more than one indices for the value `val`, apply binary search to find the index `idx` that is closest to the query index `q`.
7. Calculate the minimum distance `front` between the query index `q` and the next index with the same value, and the minimum distance `back` between the query index `q` and the previous index with the same value.
8. If the index `idx` is 0, calculate the minimum distance `back` by considering the indices modulo the array length.
9. If the index `idx` is the last index, calculate the minimum distance `front` by considering the indices modulo the array length.
10. Update the result `res[i]` with the minimum distance between the query index `q` and any other index with the same value.
11. Return the list of results `res`.

**Time Complexity**
O(n + m * log(m)), where n is the length of the array `nums` and m is the number of unique elements in the array. The binary search operation takes O(log(m)) time, and the hash table operations take O(n) time.

**Space Complexity**
O(n), where n is the length of the array `nums`. The hash table `h1` stores the indices of each unique element in the array.

**Key Insight**
The key insight is that the circular array can be treated as a linear array by considering the indices modulo the array length. This allows us to apply binary search to find the minimum distance between the query index and any other index with the same value.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 291 ms (Beats 77.72%) |
| 💾 Memory | 53.2 MB (Beats 86.61%) |
| 📅 Solved | 2026-04-16 |
| 💻 Language | Python |