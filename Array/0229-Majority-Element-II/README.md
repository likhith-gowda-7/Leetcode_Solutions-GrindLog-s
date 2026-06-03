# 229. Majority Element II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/majority-element-ii/)


## 📝 Problem Description

Given an integer array of size `n`, find all elements that appear more than `&lfloor; n/3 &rfloor;` times.

 

Example 1:**

```

**Input:** nums = [3,2,3]
**Output:** [3]

```

Example 2:**

```

**Input:** nums = [1]
**Output:** [1]

```

Example 3:**

```

**Input:** nums = [1,2]
**Output:** [1,2]

```

 

**Constraints:**

	- `1 <= nums.length <= 5 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`

 

**Follow up:** Could you solve the problem in linear time and in `O(1)` space?

## 🧠 Solution Explanation

## Intuition
The solution works by first counting the frequency of each element in the array using a hash table. This allows us to efficiently determine which elements appear more than `n/3` times. The key idea is to leverage the hash table's ability to store and retrieve frequency information in constant time.

## Approach
1. Initialize a hash table to store the frequency of each element in the array.
2. Iterate through the array and update the frequency count for each element in the hash table.
3. Initialize an empty list to store the result.
4. Iterate through the hash table and check if the frequency of each element exceeds `n/3`.
5. If an element's frequency exceeds `n/3`, add it to the result list.

## Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because we perform a constant amount of work for each element in the array, both when counting frequencies and when checking for majority elements.

## Space Complexity
The space complexity is O(n), where n is the length of the input array. This is because in the worst case, we may need to store every element in the hash table.

## Key Insight
The key insight is to use a hash table to efficiently count the frequency of each element, allowing us to solve the problem in linear time. However, this solution does not meet the follow-up requirement of O(1) space complexity, suggesting that a more optimized approach may be necessary to achieve this goal.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1 ms (Beats 95.45%) |
| 💾 Memory | 19.3 MB (Beats 100%) |
| 📅 Solved | 2025-02-06 |
| 💻 Language | Python |