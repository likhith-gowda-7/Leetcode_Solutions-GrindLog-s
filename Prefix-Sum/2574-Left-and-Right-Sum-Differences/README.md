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

## 🧠 Solution Explanation

**Intuition**
The solution calculates the absolute difference between the sum of elements to the left and right of each index in the input array. This is achieved by maintaining a running sum of the array elements and using it to calculate the right sum for each index.

**Approach**
1. Initialize an empty list `res` to store the results and a variable `total` to store the sum of all elements in the input array `nums`.
2. Calculate the sum of all elements in `nums` and store it in `total`.
3. Initialize a variable `left` to 0, which will store the sum of elements to the left of the current index.
4. Iterate over the indices of `nums` from 0 to `n-1`.
5. For each index `i`, calculate the right sum by subtracting the current element `nums[i]` from the total sum `total` and adding the sum of elements to the left of `i`, which is stored in `left`.
6. Calculate the absolute difference between the left sum and the right sum, and append it to the result list `res`.
7. Update the `left` variable by adding the current element `nums[i]` to it.
8. Return the result list `res`.

**Time Complexity**
O(n), where n is the size of the input array `nums`. This is because we are iterating over the array once and performing constant-time operations for each element.

**Space Complexity**
O(n), where n is the size of the input array `nums`. This is because we are storing the result in a list of size n.

**Key Insight**
The key to this solution is the observation that the right sum for each index can be calculated by subtracting the current element from the total sum and adding the sum of elements to the left of the current index. This allows us to avoid recalculating the sum of elements to the right of each index, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1 ms (Beats 83.48%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-10 |
| 💻 Language | Python |