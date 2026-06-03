> 📌 **Cross-listed:** Primary location is [Array/2294-Partition-Array-Such-That-Maximum-Difference-Is-K](../../Array/2294-Partition-Array-Such-That-Maximum-Difference-Is-K). This problem also appears under: **Array**, **Greedy**, **Sorting**

# 2294. Partition Array Such That Maximum Difference Is K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`. You may partition `nums` into one or more **subsequences** such that each element in `nums` appears in **exactly** one of the subsequences.

Return *the **minimum **number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is **at most** *`k`*.*

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:**

```

**Input:** nums = [3,6,1,2,5], k = 2
**Output:** 2
**Explanation:**
We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.

```

Example 2:**

```

**Input:** nums = [1,2,3], k = 1
**Output:** 2
**Explanation:**
We can partition nums into the two subsequences [1,2] and [3].
The difference between the maximum and minimum value in the first subsequence is 2 - 1 = 1.
The difference between the maximum and minimum value in the second subsequence is 3 - 3 = 0.
Since two subsequences were created, we return 2. Note that another optimal solution is to partition nums into the two subsequences [1] and [2,3].

```

Example 3:**

```

**Input:** nums = [2,2,4,5], k = 0
**Output:** 3
**Explanation:**
We can partition nums into the three subsequences [2,2], [4], and [5].
The difference between the maximum and minimum value in the first subsequences is 2 - 2 = 0.
The difference between the maximum and minimum value in the second subsequences is 4 - 4 = 0.
The difference between the maximum and minimum value in the third subsequences is 5 - 5 = 0.
Since three subsequences were created, we return 3. It can be shown that 3 is the minimum number of subsequences needed.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`

	- `0 <= k <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the unique elements in the array and then iterating through the sorted array to find the minimum number of subsequences needed. The key insight is that we can always start a new subsequence whenever the difference between the current element and the minimum element in the previous subsequence exceeds `k`.

**Approach**
1. Remove duplicates from the array by converting it to a set and then sorting the set to get the unique elements in ascending order.
2. Initialize a variable `count` to keep track of the minimum number of subsequences needed, and a variable `mini` to keep track of the minimum element in the previous subsequence.
3. Iterate through the sorted array starting from the second element (index 1).
4. For each element, calculate the difference between the current element and the minimum element in the previous subsequence.
5. If the difference exceeds `k`, increment the `count` variable and update the `mini` variable to the current element.
6. After iterating through the entire array, return `count + 1`, which represents the minimum number of subsequences needed.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the number of unique elements in the array.

**Space Complexity**
O(n) for storing the unique elements in the array, where n is the number of unique elements in the array.

**Key Insight**
The key insight is that we can always start a new subsequence whenever the difference between the current element and the minimum element in the previous subsequence exceeds `k`, which allows us to minimize the number of subsequences needed.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 47 ms (Beats 99.26%) |
| 💾 Memory | 33.2 MB (Beats 74.94%) |
| 📅 Solved | 2025-06-19 |
| 💻 Language | Python |