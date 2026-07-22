> 📌 **Cross-listed:** Primary location is [Array/0673-Number-of-Longest-Increasing-Subsequence](../../Array/0673-Number-of-Longest-Increasing-Subsequence). This problem also appears under: **Array**, **Dynamic Programming**, **Binary Indexed Tree**, **Segment Tree**

# 673. Number of Longest Increasing Subsequence


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Binary Indexed Tree](https://img.shields.io/badge/Binary%20Indexed%20Tree-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)


## 📝 Problem Description

Given an integer array `nums`, return *the number of longest increasing subsequences.*

**Notice** that the sequence has to be **strictly** increasing.

 

Example 1:**

```

**Input:** nums = [1,3,5,4,7]
**Output:** 2
**Explanation:** The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

```

Example 2:**

```

**Input:** nums = [2,2,2,2,2]
**Output:** 5
**Explanation:** The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

```

 

**Constraints:**

	- `1 <= nums.length <= 2000`

	- `-10^6 <= nums[i] <= 10^6`

	- The answer is guaranteed to fit inside a 32-bit integer.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the number of longest increasing subsequences in a given array. We can use dynamic programming to solve this problem by maintaining two arrays: `dp` to store the length of the longest increasing subsequence ending at each position, and `counts` to store the number of such subsequences.

**Approach**
1. Initialize two arrays `dp` and `counts` of size `n` with all elements as 1, where `n` is the length of the input array `nums`.
2. Iterate through the array from the second element to the last element.
3. For each element at index `i`, compare it with all previous elements at index `prev`.
4. If the current element is greater than the previous element and the length of the longest increasing subsequence ending at the previous element plus one is greater than the length of the longest increasing subsequence ending at the current element, update `dp[i]` and `counts[i]` accordingly.
5. If the length of the longest increasing subsequence ending at the previous element plus one is equal to the length of the longest increasing subsequence ending at the current element, add the count of the longest increasing subsequence ending at the previous element to `counts[i]`.
6. Update the maximum length of the longest increasing subsequence `maxi` if a longer subsequence is found.
7. Finally, iterate through the `dp` array and add the count of the longest increasing subsequences ending at each position to `no_of_lis` if their length is equal to `maxi`.

**Time Complexity**
The time complexity of this solution is O(n^2), where n is the length of the input array `nums`. This is because we have two nested loops that iterate through the array.

**Space Complexity**
The space complexity of this solution is O(n), where n is the length of the input array `nums`. This is because we need to store two arrays `dp` and `counts` of size `n`.

**Key Insight**
The key insight here is to use dynamic programming to maintain the length and count of the longest increasing subsequences ending at each position. By iterating through the array and updating these values accordingly, we can efficiently find the number of longest increasing subsequences.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 623 ms (Beats 14.86%) |
| 💾 Memory | 19.5 MB (Beats 63.88%) |
| 📅 Solved | 2026-07-22 |
| 💻 Language | Python |