# 1480. Running Sum of 1d Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)


## 📝 Problem Description

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]&hellip;nums[i])`.

Return the running sum of `nums`.

 

Example 1:**

```

**Input:** nums = [1,2,3,4]
**Output:** [1,3,6,10]
**Explanation:** Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

Example 2:**

```

**Input:** nums = [1,1,1,1,1]
**Output:** [1,2,3,4,5]
**Explanation:** Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

Example 3:**

```

**Input:** nums = [3,1,2,10,1]
**Output:** [3,4,6,16,17]

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `-10^6 <= nums[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The running sum of an array can be calculated by iterating through the array and adding each element to the sum of the previous elements. This approach is efficient because it only requires a single pass through the array.

**Approach**
1. Initialize an empty list to store the running sum.
2. Iterate through the input array `nums` starting from the second element (index 1).
3. For each element `nums[i]`, add the previous element `nums[i-1]` to it and store the result back in `nums[i]`.
4. Repeat step 3 until the end of the array is reached.
5. Return the modified array `nums`, which now contains the running sum of each element.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we only need to iterate through the array once to calculate the running sum.

**Space Complexity**
O(1), excluding the space required for the output array. We only use a constant amount of space to store the index `i` and the previous element `nums[i-1]`, and the input array `nums` is modified in-place.

**Key Insight**
The key insight here is that we can calculate the running sum by modifying the input array `nums` in-place, without the need to create a separate output array. This approach reduces the space complexity to O(1) and makes the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.2 MB (Beats 100%) |
| 📅 Solved | 2024-12-15 |
| 💻 Language | Python |