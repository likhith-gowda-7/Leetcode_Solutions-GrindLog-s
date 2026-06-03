> 📌 **Cross-listed:** Primary location is [Array/0594-Longest-Harmonious-Subsequence](../../Array/0594-Longest-Harmonious-Subsequence). This problem also appears under: **Array**, **Hash Table**, **Sliding Window**, **Sorting**, **Counting**

# 594. Longest Harmonious Subsequence


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-harmonious-subsequence/)


## 📝 Problem Description

We define a harmonious array as an array where the difference between its maximum value and its minimum value is **exactly** `1`.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:**

**Input:** nums = [1,3,2,2,5,2,3,7]

**Output:** 5

**Explanation:**

The longest harmonious subsequence is `[3,2,2,2,3]`.

Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** 2

**Explanation:**

The longest harmonious subsequences are `[1,2]`, `[2,3]`, and `[3,4]`, all of which have a length of 2.

Example 3:**

**Input:** nums = [1,1,1,1]

**Output:** 0

**Explanation:**

No harmonic subsequence exists.

 

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by leveraging the properties of a harmonious array, where the difference between its maximum and minimum value is exactly 1. This insight allows us to focus on pairs of numbers that have a difference of 1, which can be efficiently counted using a hash table.

**Approach**
1. Create a hash table `h1` to store the frequency of each number in the input array `nums`.
2. Initialize a variable `res` to store the length of the longest harmonious subsequence found so far.
3. Iterate over the keys of the hash table `h1`.
4. For each key `n`, check if `n+1` is also a key in the hash table `h1`.
5. If `n+1` is a key, calculate the total frequency of the pair `(n, n+1)` by adding the frequencies of `n` and `n+1`.
6. Update `res` if the total frequency of the pair is greater than the current value of `res`.
7. Return the value of `res` as the length of the longest harmonious subsequence.

**Time Complexity**
O(n), where n is the number of unique elements in the input array `nums`. This is because we iterate over the keys of the hash table `h1` once, and each key is visited at most twice (once for `n` and once for `n+1`).

**Space Complexity**
O(n), where n is the number of unique elements in the input array `nums`. This is because we store the frequency of each unique element in the hash table `h1`.

**Key Insight**
The key insight behind this solution is that a harmonious array can be formed by pairing numbers that have a difference of 1. By counting the frequency of each number and its successor, we can efficiently identify the longest harmonious subsequence. This insight allows us to simplify the problem and focus on a specific pattern, making the solution more efficient and scalable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 12 ms (Beats 97.68%) |
| 💾 Memory | 19.4 MB (Beats 100%) |
| 📅 Solved | 2025-06-30 |
| 💻 Language | Python |