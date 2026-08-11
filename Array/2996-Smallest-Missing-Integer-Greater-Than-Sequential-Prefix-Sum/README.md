# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/)


## 📝 Problem Description

You are given a **0-indexed** array of integers `nums`.

A prefix `nums[0..i]` is **sequential** if, for all `1 <= j <= i`, `nums[j] = nums[j - 1] + 1`. In particular, the prefix consisting only of `nums[0]` is **sequential**.

Return *the **smallest** integer* `x` *missing from* `nums` *such that* `x` *is greater than or equal to the sum of the **longest** sequential prefix.*

 

Example 1:**

```

**Input:** nums = [1,2,3,2,5]
**Output:** 6
**Explanation:** The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

```

Example 2:**

```

**Input:** nums = [3,4,5,1,12,14,13]
**Output:** 15
**Explanation:** The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

```

 

**Constraints:**

	- `1 <= nums.length <= 50`

	- `1 <= nums[i] <= 50`

## 🧠 Solution Explanation

**Intuition**
The solution works by first identifying the longest sequential prefix in the array and calculating its sum. Then, it checks each integer in the array to see if it is greater than or equal to the sum. If not, it increments the sum until it finds the smallest missing integer.

**Approach**
1. Initialize `seq` to the first element of the array, which represents the longest sequential prefix.
2. Iterate through the array starting from the second element. If the current element is one more than the previous element, add it to `seq`.
3. If the current element is not one more than the previous element, break the loop because we've found the end of the longest sequential prefix.
4. Convert the array to a set for efficient lookups.
5. Initialize `seq` to the sum of the longest sequential prefix and check if it exists in the set. If it does, increment `seq` until we find the smallest missing integer.

**Time Complexity**
O(n) - The loop through the array runs in linear time, and the set operations also take linear time.

**Space Complexity**
O(n) - We convert the array to a set, which takes linear space.

**Key Insight**
The key insight is to identify the longest sequential prefix and calculate its sum, which allows us to efficiently find the smallest missing integer greater than or equal to the sum. This approach avoids checking every integer in the array, making it more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 87.89%) |
| 📅 Solved | 2026-08-11 |
| 💻 Language | Python |