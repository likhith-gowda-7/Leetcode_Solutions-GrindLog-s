# 1726. Tuple with Same Product


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/tuple-with-same-product/)


## 📝 Problem Description

Given an array `nums` of **distinct** positive integers, return *the number of tuples *`(a, b, c, d)`* such that *`a * b = c * d`* where *`a`*, *`b`*, *`c`*, and *`d`* are elements of *`nums`*, and *`a != b != c != d`*.*

 

Example 1:**

```

**Input:** nums = [2,3,4,6]
**Output:** 8
**Explanation:** There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

```

Example 2:**

```

**Input:** nums = [1,2,4,5,10]
**Output:** 16
**Explanation:** There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^4`

	- All elements in `nums` are **distinct**.

## 🧠 Solution Explanation

**Intuition**
The problem requires counting the number of tuples `(a, b, c, d)` where `a * b = c * d` and `a != b != c != d`. The key insight is that for each pair of numbers `a` and `b`, we can form four tuples by swapping `a` and `c` and `b` and `d`. We can use a hash table to count the occurrences of each product `a * b` and then calculate the number of tuples for each product.

**Approach**
1. Initialize an empty hash table `h1` to store the count of each product `a * b`.
2. Iterate through the array `nums` and for each pair of numbers `nums[i]` and `nums[j]` (where `i < j`), calculate the product `pro = nums[i] * nums[j]`.
3. Increment the count of `pro` in the hash table `h1`.
4. Initialize a variable `res` to store the total count of tuples.
5. Iterate through the values in the hash table `h1` and for each value `val`, calculate the number of tuples that can be formed using this value. This is done by multiplying `val` with `(val - 1) / 2` (since we can form `val` pairs and each pair can be swapped to form two tuples). Multiply this result by 8 to account for the four tuples that can be formed for each pair.
6. Add the result from step 5 to `res`.
7. Return `res` as the total count of tuples.

**Time Complexity**
O(n^2 * m), where n is the length of the array `nums` and m is the maximum possible product of two numbers in the array. The reason is that we are iterating through the array `nums` and for each pair of numbers, we are calculating the product and incrementing the count in the hash table.

**Space Complexity**
O(m), where m is the maximum possible product of two numbers in the array. The reason is that we are using a hash table to store the count of each product, and the size of the hash table is proportional to the maximum possible product.

**Key Insight**
The key insight is that for each pair of numbers `a` and `b`, we can form four tuples by swapping `a` and `c` and `b` and `d`. This allows us to count the number of tuples for each product `a * b` and then calculate the total count of tuples.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 391 ms (Beats 45.7%) |
| 💾 Memory | 46.4 MB (Beats 99.46%) |
| 📅 Solved | 2025-02-06 |
| 💻 Language | Python |