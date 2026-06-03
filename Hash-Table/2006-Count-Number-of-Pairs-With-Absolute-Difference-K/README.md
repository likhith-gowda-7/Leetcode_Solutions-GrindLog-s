> 📌 **Cross-listed:** Primary location is [Array/2006-Count-Number-of-Pairs-With-Absolute-Difference-K](../../Array/2006-Count-Number-of-Pairs-With-Absolute-Difference-K). This problem also appears under: **Array**, **Hash Table**, **Counting**

# 2006. Count Number of Pairs With Absolute Difference K


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return *the number of pairs* `(i, j)` *where* `i < j` *such that* `|nums[i] - nums[j]| == k`.

The value of `|x|` is defined as:

	- `x` if `x >= 0`.

	- `-x` if `x < 0`.

 

Example 1:**

```

**Input:** nums = [1,2,2,1], k = 1
**Output:** 4
**Explanation:** The pairs with an absolute difference of 1 are:
- [**1**,**2**,2,1]
- [**1**,2,**2**,1]
- [1,**2**,2,**1**]
- [1,2,**2**,**1**]

```

Example 2:**

```

**Input:** nums = [1,3], k = 3
**Output:** 0
**Explanation:** There are no pairs with an absolute difference of 3.

```

Example 3:**

```

**Input:** nums = [3,2,1,5,4], k = 2
**Output:** 3
**Explanation:** The pairs with an absolute difference of 2 are:
- [**3**,2,**1**,5,4]
- [**3**,2,1,**5**,4]
- [3,**2**,1,5,**4**]

```

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 100`

	- `1 <= k <= 99`

## 🧠 Solution Explanation

**Intuition**
This solution works by utilizing a hash table (implemented as a Counter object in Python) to store the frequency of each number in the input array. It then iterates over the hash table, checking for pairs of numbers with an absolute difference of `k`. The key insight is that for each number `key` in the hash table, we can calculate its corresponding "difference" number `diff` by subtracting `k` from `key`. If `diff` is also present in the hash table, we can calculate the total number of pairs by multiplying the frequency of `key` and `diff`.

**Approach**
1. Create a hash table `h1` to store the frequency of each number in the input array `nums` using the Counter class.
2. Initialize a variable `pairs` to store the total number of pairs with an absolute difference of `k`.
3. Iterate over the hash table `h1` using a for loop.
4. For each key `key` in the hash table, calculate its corresponding "difference" number `diff` by subtracting `k` from `key`.
5. Check if `diff` is also present in the hash table `h1`. If it is, calculate the total number of pairs by multiplying the frequency of `key` and `diff` and add it to the `pairs` variable.
6. Return the total number of pairs `pairs`.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we are iterating over the hash table once, which takes O(n) time in the worst case.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because we are storing the frequency of each number in the hash table, which takes O(n) space in the worst case.

**Key Insight**
The key insight is that for each number `key` in the hash table, we can calculate its corresponding "difference" number `diff` by subtracting `k` from `key`. This allows us to efficiently calculate the total number of pairs by multiplying the frequency of `key` and `diff`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-06-10 |
| 💻 Language | Python |