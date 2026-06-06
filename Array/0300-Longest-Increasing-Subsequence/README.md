# 300. Longest Increasing Subsequence


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)


## 📝 Problem Description

Given an integer array `nums`, return *the length of the longest **strictly increasing ******subsequence***.

 

Example 1:**

```

**Input:** nums = [10,9,2,5,3,7,101,18]
**Output:** 4
**Explanation:** The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

```

Example 2:**

```

**Input:** nums = [0,1,0,3,2,3]
**Output:** 4

```

Example 3:**

```

**Input:** nums = [7,7,7,7,7,7,7]
**Output:** 1

```

 

**Constraints:**

	- `1 <= nums.length <= 2500`

	- `-10^4 <= nums[i] <= 10^4`

 

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## 🧠 Solution Explanation

## Intuition
The solution works by maintaining a dynamic programming (DP) table where each entry represents the length of the longest increasing subsequence ending at that index. This approach allows us to efficiently explore all possible subsequences and keep track of the longest one found so far. By comparing each element with its predecessors, we can determine whether it can be appended to an existing subsequence or if it starts a new one.

## Approach
1. Initialize a DP table `dp` with the same length as the input array `nums`, where each entry is set to 1 (since a single element is an increasing subsequence of length 1).
2. Iterate through the array from the second element to the end, and for each element, compare it with all its predecessors.
3. If the current element is greater than a predecessor, update the DP table entry for the current element to be the maximum of its current value and the length of the subsequence ending at the predecessor plus one.
4. Keep track of the maximum length found so far in the `res` variable.

## Time Complexity
The time complexity is O(n^2), where n is the length of the input array. This is because we have two nested loops: one iterating through the array and another comparing each element with its predecessors.

## Space Complexity
The space complexity is O(n), as we need to store the DP table and the result variable, both of which have a size proportional to the input array.

## Key Insight
The key insight behind this solution is the realization that we can build the longest increasing subsequence by iteratively extending existing subsequences or starting new ones, and that the DP table allows us to efficiently keep track of these subsequences and their lengths. However, this solution does not meet the follow-up challenge of achieving O(n log(n)) time complexity, which would require a more advanced approach involving binary search.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 77.59%) |
| 💾 Memory | 19.6 MB (Beats 32.89%) |
| 📅 Solved | 2026-06-06 |
| 💻 Language | Python |