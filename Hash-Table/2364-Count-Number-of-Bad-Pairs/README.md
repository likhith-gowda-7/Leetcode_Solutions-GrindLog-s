> 📌 **Cross-listed:** Primary location is [Array/2364-Count-Number-of-Bad-Pairs](../../Array/2364-Count-Number-of-Bad-Pairs). This problem also appears under: **Array**, **Hash Table**, **Math**, **Counting**

# 2364. Count Number of Bad Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-number-of-bad-pairs/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

Return* the total number of **bad pairs** in *`nums`.

 

Example 1:**

```

**Input:** nums = [4,1,3,3]
**Output:** 5
**Explanation:** The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

```

Example 2:**

```

**Input:** nums = [1,2,3,4,5]
**Output:** 0
**Explanation:** There are no bad pairs.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by counting the total number of pairs and subtracting the number of good pairs. A good pair is defined as a pair where the difference between the indices is equal to the difference between the corresponding values in the array. The key insight is to use a hash table to store the frequency of the differences between the values and the indices, which allows us to efficiently count the good pairs.

**Approach**
1. Initialize a hash table `h1` to store the frequency of the differences between the values and the indices.
2. Calculate the total number of pairs using the formula `n*(n-1)/2`, where `n` is the length of the array.
3. Initialize a variable `good_pair` to store the number of good pairs.
4. Iterate through the array, for each element at index `ind` with value `val`, do the following:
   - Increment `good_pair` by the frequency of the difference `val-ind` in the hash table `h1`.
   - Increment the frequency of the difference `val-ind` in the hash table `h1`.
5. Return the total number of pairs minus the number of good pairs.

**Time Complexity**
The time complexity is O(n), where n is the length of the array. This is because we are iterating through the array once and performing constant time operations for each element.

**Space Complexity**
The space complexity is O(n), where n is the length of the array. This is because in the worst case, we need to store all the differences between the values and the indices in the hash table.

**Key Insight**
The key insight is to use a hash table to store the frequency of the differences between the values and the indices, which allows us to efficiently count the good pairs. This approach avoids the need to compare each pair of elements, resulting in a significant improvement in time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 98 ms (Beats 32.06%) |
| 💾 Memory | 38.9 MB (Beats 5.88%) |
| 📅 Solved | 2025-02-09 |
| 💻 Language | Python |