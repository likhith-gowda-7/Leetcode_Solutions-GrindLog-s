# 2615. Sum of Distances


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-of-distances/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`. There exists an array `arr` of length `nums.length`, where `arr[i]` is the sum of `|i - j|` over all `j` such that `nums[j] == nums[i]` and `j != i`. If there is no such `j`, set `arr[i]` to be `0`.

Return *the array *`arr`*.*

 

Example 1:**

```

**Input:** nums = [1,3,1,1,2]
**Output:** [5,0,3,4,0]
**Explanation:** 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

```

Example 2:**

```

**Input:** nums = [0,5,3]
**Output:** [0,0,0]
**Explanation:** Since each element in nums is distinct, arr[i] = 0 for all i.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

 

**Note:** This question is the same as [ 2121: Intervals Between Identical Elements.](https://leetcode.com/problems/intervals-between-identical-elements/description/)

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a hash table to group indices with the same value, then calculates the sum of distances for each group. This approach simplifies the problem by reducing it to a series of prefix sum calculations.

**Approach**
1. Create a hash table `mp` to store the indices of each unique value in the input array `nums`.
2. For each group of indices in `mp`, calculate the total sum of indices and the prefix sum of indices.
3. For each index in the group, calculate the sum of distances by considering the left and right distances separately.
4. Update the answer array `ans` with the calculated sum of distances for each index.
5. Return the completed answer array `ans`.

**Time Complexity**
O(n^2) where n is the length of the input array `nums`. This is because for each group of indices, we iterate over the indices to calculate the sum of distances.

**Space Complexity**
O(n) where n is the length of the input array `nums`. This is because we use a hash table to store the indices of each unique value.

**Key Insight**
The key insight is to break down the problem into smaller sub-problems by grouping indices with the same value, and then using prefix sum calculations to efficiently compute the sum of distances for each group. This approach allows us to avoid redundant calculations and achieve a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 119 ms (Beats 69.64%) |
| 💾 Memory | 56.1 MB (Beats 22.06%) |
| 📅 Solved | 2026-04-24 |
| 💻 Language | Python |