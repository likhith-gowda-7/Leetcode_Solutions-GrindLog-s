# 1674. Minimum Moves to Make Array Complementary


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/)


## 📝 Problem Description

You are given an integer array `nums` of **even** length `n` and an integer `limit`. In one move, you can replace any integer from `nums` with another integer between `1` and `limit`, inclusive.

The array `nums` is **complementary** if for all indices `i` (**0-indexed**), `nums[i] + nums[n - 1 - i]` equals the same number. For example, the array `[1,2,3,4]` is complementary because for all indices `i`, `nums[i] + nums[n - 1 - i] = 5`.

Return the ***minimum** number of moves required to make *`nums`* **complementary***.

 

Example 1:**

```

**Input:** nums = [1,2,4,3], limit = 4
**Output:** 1
**Explanation:** In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

```

Example 2:**

```

**Input:** nums = [1,2,2,1], limit = 2
**Output:** 2
**Explanation:** In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.

```

Example 3:**

```

**Input:** nums = [1,2,1,2], limit = 2
**Output:** 0
**Explanation:** nums is already complementary.

```

 

**Constraints:**

	- `n == nums.length`

	- `2 <= n <= 10^5`

	- `1 <= nums[i] <= limit <= 10^5`

	- `n` is even.

## 🧠 Solution Explanation

**Intuition**
The solution uses a prefix sum array to efficiently calculate the minimum number of moves required to make the array complementary. The key insight is to consider the sum of pairs of elements from both ends of the array and use a prefix sum array to keep track of the cumulative count of such pairs.

**Approach**
1. Initialize a prefix sum array `delta` of size `2 * limit + 2` to keep track of the cumulative count of pairs with a given sum.
2. Iterate through the first half of the array `nums`, and for each pair of elements `nums[i]` and `nums[-1 - i]`, update the prefix sum array `delta` accordingly.
3. For each pair, increment the count of pairs with a sum of 2, decrement the count of pairs with a sum of `mini + 1`, decrement the count of pairs with a sum of `mini + maxi`, increment the count of pairs with a sum of `mini + maxi + 1`, and increment the count of pairs with a sum of `maxi + limit + 1`.
4. Initialize the minimum number of moves `res` to the length of the array `n` and the current number of moves `moves` to 0.
5. Iterate through the prefix sum array `delta` and update the minimum number of moves `res` by taking the minimum of `res` and `moves` for each target sum `targ`.

**Time Complexity**
O(n), where n is the length of the array `nums`. The time complexity is linear because we are iterating through the array once and updating the prefix sum array in a single pass.

**Space Complexity**
O(limit), where limit is the given limit. The space complexity is linear because we are using a prefix sum array of size `2 * limit + 2` to keep track of the cumulative count of pairs.

**Key Insight**
The key insight is to use a prefix sum array to efficiently calculate the minimum number of moves required to make the array complementary. By updating the prefix sum array in a single pass, we can avoid iterating through the array multiple times and achieve a linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 207 ms (Beats 43.08%) |
| 💾 Memory | 31 MB (Beats 76.13%) |
| 📅 Solved | 2026-05-30 |
| 💻 Language | Python |