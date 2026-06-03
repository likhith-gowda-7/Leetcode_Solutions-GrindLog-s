# 307. Range Sum Query - Mutable


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Binary Indexed Tree](https://img.shields.io/badge/Binary%20Indexed%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/range-sum-query-mutable/)


## 📝 Problem Description

Given an integer array `nums`, handle multiple queries of the following types:

	- **Update** the value of an element in `nums`.

	- Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

	- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.

	- `void update(int index, int val)` **Updates** the value of `nums[index]` to be `val`.

	- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

 

Example 1:**

```

**Input**
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
**Output**
[null, 9, null, 8]

**Explanation**
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-100 <= nums[i] <= 100`

	- `0 <= index < nums.length`

	- `-100 <= val <= 100`

	- `0 <= left <= right < nums.length`

	- At most `3 * 10^4` calls will be made to `update` and `sumRange`.

## 🧠 Solution Explanation

## Intuition
The solution utilizes a Binary Indexed Tree (BIT) to efficiently store and update cumulative sums of the input array, allowing for fast range sum queries. By maintaining a separate copy of the original array, we can calculate the difference in values when updating an element and propagate this change to the BIT. This approach enables us to balance the trade-off between update and query operations.

## Approach
1. Initialize the `NumArray` object with the input array, creating a copy of the array and a BIT with the same length plus one.
2. Populate the BIT by iterating through the input array and adding each element's value to the corresponding indices in the BIT.
3. When updating an element, calculate the difference between the new and old values, update the copy of the array, and add this difference to the BIT.
4. To query the sum of a range, use the BIT to calculate the cumulative sum up to the right endpoint and subtract the cumulative sum up to the left endpoint minus one.

## Time Complexity
The time complexity is O(log n) for both update and query operations, where n is the length of the input array. This is because BIT operations (add and query) involve traversing the tree, which has a height of log n.

## Space Complexity
The space complexity is O(n), where n is the length of the input array. This is because we need to store the input array, its copy, and the BIT, all of which have a length of n or n+1.

## Key Insight
The key insight is using the BIT to store cumulative sums, which allows for efficient range sum queries by exploiting the properties of the BIT. By maintaining a separate copy of the original array, we can calculate the difference in values when updating an element and propagate this change to the BIT, enabling fast updates and queries.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 408 ms (Beats 69.13%) |
| 💾 Memory | 36.1 MB (Beats 100%) |
| 📅 Solved | 2025-07-02 |
| 💻 Language | Python |