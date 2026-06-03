# 1437. Check If All 1's Are at Least Length K Places Away


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/)


## 📝 Problem Description

Given an binary array `nums` and an integer `k`, return `true`* if all *`1`*'s are at least *`k`* places away from each other, otherwise return *`false`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)
```

**Input:** nums = [1,0,0,0,1,0,0,1], k = 2
**Output:** true
**Explanation:** Each of the 1s are at least 2 places away from each other.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)
```

**Input:** nums = [1,0,0,1,0,1], k = 2
**Output:** false
**Explanation:** The second 1 and third 1 are only one apart from each other.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= k <= nums.length`

	- `nums[i]` is `0` or `1`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the binary array and keeping track of the index of the last '1' encountered. If the current index is within k places of the last '1', the function immediately returns False, indicating that the condition is not met. If the function iterates through the entire array without finding any adjacent '1's within k places, it returns True.

**Approach**
1. Initialize a variable `prev_one_idx` to store the index of the last '1' encountered, and set it to None.
2. Iterate through the binary array `nums` using a for loop.
3. For each element in the array, check if it is equal to 1.
4. If the current element is 1, check if `prev_one_idx` is not None and if the difference between the current index `i` and `prev_one_idx` is less than or equal to `k`. If this condition is met, return False.
5. If the condition in step 4 is not met, update `prev_one_idx` to the current index `i`.
6. If the function iterates through the entire array without returning False, return True.

**Time Complexity**
O(n), where n is the length of the binary array. This is because the function iterates through the array once.

**Space Complexity**
O(1), as the function only uses a constant amount of space to store the index of the last '1' encountered.

**Key Insight**
The key insight is that we only need to keep track of the index of the last '1' encountered, and we can immediately return False if the current index is within k places of the last '1'. This allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 51.24%) |
| 💾 Memory | 21.1 MB (Beats 100%) |
| 📅 Solved | 2025-11-17 |
| 💻 Language | Python |