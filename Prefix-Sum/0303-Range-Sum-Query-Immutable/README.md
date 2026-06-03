> 📌 **Cross-listed:** Primary location is [Array/0303-Range-Sum-Query-Immutable](../../Array/0303-Range-Sum-Query-Immutable). This problem also appears under: **Array**, **Design**, **Prefix Sum**

# 303. Range Sum Query - Immutable


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/range-sum-query-immutable/)


## 📝 Problem Description

Given an integer array `nums`, handle multiple queries of the following type:

	- Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

	- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.

	- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

 

Example 1:**

```

**Input**
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
**Output**
[null, 1, -1, -3]

**Explanation**
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^5 <= nums[i] <= 10^5`

	- `0 <= left <= right < nums.length`

	- At most `10^4` calls will be made to `sumRange`.

## 🧠 Solution Explanation

## Intuition
The solution works by precomputing the prefix sum of the input array, which allows for efficient calculation of the sum of elements within any range. By storing the cumulative sum at each index, we can quickly calculate the sum of elements between two indices. This approach takes advantage of the fact that the input array is immutable, enabling us to perform the precomputation step.

## Approach
1. Initialize a prefix sum array with the same length as the input array.
2. Set the first element of the prefix sum array to the first element of the input array.
3. Iterate through the input array, starting from the second element, and calculate the prefix sum at each index by adding the current element to the previous prefix sum.
4. To calculate the sum of elements within a range, subtract the prefix sum at the index before the start of the range from the prefix sum at the end of the range. If the range starts at index 0, return the prefix sum at the end of the range.

## Time Complexity
The time complexity is O(n) for initialization and O(1) for each sumRange query, where n is the length of the input array. This is because the prefix sum array is computed only once during initialization, and subsequent queries only involve constant-time calculations.

## Space Complexity
The space complexity is O(n), where n is the length of the input array. This is because we need to store the prefix sum array, which has the same length as the input array.

## Key Insight
The key insight behind this solution is the use of prefix sums to enable efficient range sum queries. By precomputing the cumulative sum at each index, we can avoid having to iterate through the input array for each query, resulting in a significant reduction in query time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.7 MB (Beats 100%) |
| 📅 Solved | 2024-12-17 |
| 💻 Language | Python |