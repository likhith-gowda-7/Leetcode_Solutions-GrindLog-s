> 📌 **Cross-listed:** Primary location is [Array/0724-Find-Pivot-Index](../../Array/0724-Find-Pivot-Index). This problem also appears under: **Array**, **Prefix Sum**

# 724. Find Pivot Index


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-pivot-index/)


## 📝 Problem Description

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return *the **leftmost pivot index***. If no such index exists, return `-1`.

 

Example 1:**

```

**Input:** nums = [1,7,3,6,5,6]
**Output:** 3
**Explanation:**
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

```

Example 2:**

```

**Input:** nums = [1,2,3]
**Output:** -1
**Explanation:**
There is no index that satisfies the conditions in the problem statement.
```

Example 3:**

```

**Input:** nums = [2,1,-1]
**Output:** 0
**Explanation:**
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-1000 <= nums[i] <= 1000`

 

**Note:** This question is the same as 1991: [https://leetcode.com/problems/find-the-middle-index-in-array/](https://leetcode.com/problems/find-the-middle-index-in-array/)

## 🧠 Solution Explanation

**Intuition**
The solution relies on the concept of prefix sums, where we maintain a running total of the elements to the left of the current index. By comparing this sum with the total sum minus the current element and the sum to the right of the current element, we can determine if the current index is a pivot index.

**Approach**
1. Calculate the total sum of the array `nums`.
2. Initialize `left_sum` to 0, which represents the sum of elements to the left of the current index.
3. Iterate through the array `nums` using a for loop.
4. For each index `i`, calculate the `right_sum` as the total sum minus `left_sum` minus the current element `nums[i]`.
5. Check if `left_sum` is equal to `right_sum`. If true, return the current index `i` as the pivot index.
6. If not, increment `left_sum` by the current element `nums[i]` and repeat steps 4-5.
7. If the loop completes without finding a pivot index, return -1.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we make a single pass through the array, performing a constant amount of work for each element.

**Space Complexity**
O(1), which means the space required does not grow with the size of the input array. We only use a few extra variables to store the total sum, left sum, and right sum.

**Key Insight**
The key insight is that we can calculate the right sum using the total sum minus the left sum and the current element, rather than iterating through the elements to the right of the current index. This allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2024-12-09 |
| 💻 Language | Python |