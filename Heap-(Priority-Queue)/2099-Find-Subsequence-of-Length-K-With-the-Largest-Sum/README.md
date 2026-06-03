> 📌 **Cross-listed:** Primary location is [Array/2099-Find-Subsequence-of-Length-K-With-the-Largest-Sum](../../Array/2099-Find-Subsequence-of-Length-K-With-the-Largest-Sum). This problem also appears under: **Array**, **Hash Table**, **Sorting**, **Heap (Priority Queue)**

# 2099. Find Subsequence of Length K With the Largest Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`. You want to find a **subsequence **of `nums` of length `k` that has the **largest** sum.

Return* ****any** such subsequence as an integer array of length *`k`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:**

```

**Input:** nums = [2,1,3,3], k = 2
**Output:** [3,3]
**Explanation:**
The subsequence has the largest sum of 3 + 3 = 6.
```

Example 2:**

```

**Input:** nums = [-1,-2,3,4], k = 3
**Output:** [-1,3,4]
**Explanation:** 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

```

Example 3:**

```

**Input:** nums = [3,4,3,3], k = 2
**Output:** [3,4]
**Explanation:**
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `-10^5 <= nums[i] <= 10^5`

	- `1 <= k <= nums.length`

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the input array in descending order, which ensures that the largest numbers are at the beginning of the array. Then, it uses a hash table (Counter) to keep track of the frequency of each number in the last `k` elements of the sorted array. Finally, it iterates through the original array and appends the numbers that are present in the hash table and have a non-zero frequency.

**Approach**
1. Create a copy of the input array `nums` and sort it in descending order.
2. Calculate the index `last` which is `len(nums) - k`.
3. Create a hash table `h1` using the Counter class from the collections module, and populate it with the frequency of each number in the last `k` elements of the sorted array.
4. Initialize an empty list `res` to store the result.
5. Iterate through the original array `nums`. For each number, check if it is present in the hash table `h1` and has a non-zero frequency. If both conditions are true, append the number to the result list `res` and decrement its frequency in the hash table.
6. If the length of the result list `res` reaches `k`, break the loop.
7. Return the result list `res`.

**Time Complexity**
The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the input array `nums`. The subsequent operations (creating the hash table, iterating through the array) take O(n) time, but they are dominated by the sorting operation.

**Space Complexity**
The space complexity of this solution is O(n) due to the creation of the sorted array and the hash table.

**Key Insight**
The key insight behind this solution is that the largest subsequence of length `k` must contain the `k` largest numbers from the input array. By sorting the array in descending order and using a hash table to keep track of the frequency of each number, we can efficiently construct the largest subsequence.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-06-28 |
| 💻 Language | Python |