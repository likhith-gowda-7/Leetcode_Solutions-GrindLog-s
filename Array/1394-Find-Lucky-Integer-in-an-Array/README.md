# 1394. Find Lucky Integer in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-lucky-integer-in-an-array/)


## 📝 Problem Description

Given an array of integers `arr`, a **lucky integer** is an integer that has a frequency in the array equal to its value.

Return *the largest **lucky integer** in the array*. If there is no **lucky integer** return `-1`.

 

Example 1:**

```

**Input:** arr = [2,2,3,4]
**Output:** 2
**Explanation:** The only lucky number in the array is 2 because frequency[2] == 2.

```

Example 2:**

```

**Input:** arr = [1,2,2,3,3,3]
**Output:** 3
**Explanation:** 1, 2 and 3 are all lucky numbers, return the largest of them.

```

Example 3:**

```

**Input:** arr = [2,2,2,3,3]
**Output:** -1
**Explanation:** There are no lucky numbers in the array.

```

 

**Constraints:**

	- `1 <= arr.length <= 500`

	- `1 <= arr[i] <= 500`

## 🧠 Solution Explanation

**Intuition**
The solution works by first counting the frequency of each number in the array using a hash table (implemented as an array `freq` of size 501). Then, it iterates over the frequency array in reverse order to find the largest number whose frequency equals its value.

**Approach**
1. Create a hash table `freq` of size 501 to store the frequency of each number in the array.
2. Iterate over the input array `arr`, incrementing the corresponding frequency in `freq` for each number.
3. Iterate over `freq` in reverse order, starting from the largest possible value (500) down to 1.
4. As soon as a frequency matches its index, return that number as the largest lucky integer.
5. If no lucky integer is found, return -1.

**Time Complexity**
O(n + k), where n is the length of the input array and k is the maximum possible value in the array (500). The first loop iterates over the array once, and the second loop iterates over the frequency array at most k times.

**Space Complexity**
O(k), where k is the maximum possible value in the array (500). The frequency array has a fixed size of 501, which is used to store the frequency of each number.

**Key Insight**
The key insight is to use a hash table to count the frequency of each number efficiently, and then iterate over the frequency array in reverse order to find the largest lucky integer. This approach allows us to solve the problem in linear time and space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-05 |
| 💻 Language | Python |