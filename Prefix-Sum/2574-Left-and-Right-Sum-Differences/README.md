> 📌 **Cross-listed:** Primary location is [Array/2574-Left-and-Right-Sum-Differences](../../Array/2574-Left-and-Right-Sum-Differences). This problem also appears under: **Array**, **Prefix Sum**

# 2574. Left and Right Sum Differences


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` of size `n`.

Define two arrays `leftSum` and `rightSum` where:

	- `leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `leftSum[i] = 0`.

	- `rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `rightSum[i] = 0`.

Return an integer array `answer` of size `n` where `answer[i] = |leftSum[i] - rightSum[i]|`.

 

Example 1:**

```

**Input:** nums = [10,4,8,3]
**Output:** [15,1,11,22]
**Explanation:** The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

```

Example 2:**

```

**Input:** nums = [1]
**Output:** [0]
**Explanation:** The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^5`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1 ms (Beats 83.48%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-10 |
| 💻 Language | Python |