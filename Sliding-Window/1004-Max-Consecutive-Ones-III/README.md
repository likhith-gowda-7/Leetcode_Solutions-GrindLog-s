> 📌 **Cross-listed:** Primary location is [Array/1004-Max-Consecutive-Ones-III](../../Array/1004-Max-Consecutive-Ones-III). This problem also appears under: **Array**, **Binary Search**, **Sliding Window**, **Prefix Sum**

# 1004. Max Consecutive Ones III


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)


## 📝 Problem Description

Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive *`1`*'s in the array if you can flip at most* `k` `0`'s.

 

Example 1:**

```

**Input:** nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
**Output:** 6
**Explanation:** [1,1,1,0,0,**1**,1,1,1,1,**1**]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

Example 2:**

```

**Input:** nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
**Output:** 10
**Explanation:** [0,0,1,1,**1**,**1**,1,1,1,**1**,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `nums[i]` is either `0` or `1`.

	- `0 <= k <= nums.length`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to find the maximum number of consecutive 1's in the array by flipping at most k 0's. The key idea is to maintain a window of elements where the number of zeros is less than or equal to k, and expand the window to the right while minimizing the number of zeros.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start of the array, and a variable `zeros` to count the number of zeros in the current window.
2. Iterate through the array with the `r` pointer, incrementing `zeros` whenever a zero is encountered.
3. If `zeros` exceeds `k`, move the `l` pointer to the right, decrementing `zeros` whenever a zero is encountered.
4. Update the maximum length of the window (`res`) whenever a longer window is found.
5. Repeat steps 2-4 until the `r` pointer reaches the end of the array.

**Time Complexity**
O(n), where n is the length of the array. This is because each element in the array is visited at most twice, once by the `r` pointer and once by the `l` pointer.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the pointers and the count of zeros.

**Key Insight**
The key insight is to maintain a window of elements where the number of zeros is less than or equal to k, and expand the window to the right while minimizing the number of zeros. This is achieved by moving the `l` pointer to the right when `zeros` exceeds `k`, effectively "flipping" the zeros to ones.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 67 ms (Beats 28.81%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-03-09 |
| 💻 Language | Python |