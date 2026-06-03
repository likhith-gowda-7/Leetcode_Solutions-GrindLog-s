> 📌 **Cross-listed:** Primary location is [Array/1498-Number-of-Subsequences-That-Satisfy-the-Given-Sum-Condition](../../Array/1498-Number-of-Subsequences-That-Satisfy-the-Given-Sum-Condition). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Sorting**

# 1498. Number of Subsequences That Satisfy the Given Sum Condition


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)


## 📝 Problem Description

You are given an array of integers `nums` and an integer `target`.

Return *the number of **non-empty** subsequences of *`nums`* such that the sum of the minimum and maximum element on it is less or equal to *`target`. Since the answer may be too large, return it **modulo** `10^9 + 7`.

 

Example 1:**

```

**Input:** nums = [3,5,6,7], target = 9
**Output:** 4
**Explanation:** There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

```

Example 2:**

```

**Input:** nums = [3,3,6,8], target = 10
**Output:** 6
**Explanation:** There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

```

Example 3:**

```

**Input:** nums = [2,3,3,4,6,7], target = 12
**Output:** 61
**Explanation:** There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`

	- `1 <= target <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the number of non-empty subsequences of `nums` such that the sum of the minimum and maximum element on it is less or equal to `target`. We can use a two-pointer technique to solve this problem efficiently. The key insight is that we can generate all possible subsequences by choosing the minimum and maximum elements from the sorted array.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Initialize two pointers, `left` and `right`, to the start and end of the sorted array, respectively.
3. Initialize a variable `res` to store the count of valid subsequences.
4. While `left` is less than or equal to `right`, calculate the sum of the elements at the `left` and `right` indices.
5. If the sum is less than or equal to `target`, add 2 to the power of `right - left` to `res` (since we can choose any subset of the elements between `left` and `right`), and increment `left`.
6. If the sum is greater than `target`, decrement `right`.
7. Return `res` modulo `10^9 + 7`.

**Time Complexity**
O(n log n) due to the sorting step, where n is the length of the input array `nums`.

**Space Complexity**
O(1) since we only use a constant amount of space to store the pointers and the result.

**Key Insight**
The key insight is that we can generate all possible subsequences by choosing the minimum and maximum elements from the sorted array. This allows us to use a two-pointer technique to efficiently count the number of valid subsequences.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 147 ms (Beats 68.38%) |
| 💾 Memory | 27.8 MB (Beats 100%) |
| 📅 Solved | 2025-06-29 |
| 💻 Language | Python |