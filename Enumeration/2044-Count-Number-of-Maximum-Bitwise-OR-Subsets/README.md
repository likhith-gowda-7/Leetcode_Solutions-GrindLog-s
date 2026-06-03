> 📌 **Cross-listed:** Primary location is [Array/2044-Count-Number-of-Maximum-Bitwise-OR-Subsets](../../Array/2044-Count-Number-of-Maximum-Bitwise-OR-Subsets). This problem also appears under: **Array**, **Backtracking**, **Bit Manipulation**, **Enumeration**

# 2044. Count Number of Maximum Bitwise-OR Subsets


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)


## 📝 Problem Description

Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a subset of `nums` and return *the **number of different non-empty subsets** with the maximum bitwise OR*.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`. Two subsets are considered **different** if the indices of the elements chosen are different.

The bitwise OR of an array `a` is equal to `a[0] **OR** a[1] **OR** ... **OR** a[a.length - 1]` (**0-indexed**).

 

Example 1:**

```

**Input:** nums = [3,1]
**Output:** 2
**Explanation:** The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

```

Example 2:**

```

**Input:** nums = [2,2,2]
**Output:** 7
**Explanation:** All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 2^3 - 1 = 7 total subsets.

```

Example 3:**

```

**Input:** nums = [3,2,1,5]
**Output:** 6
**Explanation:** The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
```

 

**Constraints:**

	- `1 <= nums.length <= 16`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the maximum possible bitwise OR of a subset of the given array `nums` and returning the number of different non-empty subsets with this maximum bitwise OR. The key insight is that the maximum bitwise OR can be achieved by including the maximum element in the subset, and the number of subsets with this maximum bitwise OR can be found by considering all possible combinations of including or excluding each element.

**Approach**
1. Calculate the maximum possible bitwise OR of the entire array `nums` using a helper function `bit_or`.
2. Initialize a counter `count` to store the number of subsets with the maximum bitwise OR.
3. Define a recursive helper function `backtrack` that takes the current index `idx` and the current bitwise OR `curr_or` as parameters.
4. In the `backtrack` function, if the current index `idx` is equal to the length of the array `n`, check if the current bitwise OR `curr_or` is equal to the maximum bitwise OR `t`. If it is, increment the counter `count`.
5. Recursively call the `backtrack` function with the next index `idx+1` and the current bitwise OR `curr_or|nums[idx]` (including the current element) and with the next index `idx+1` and the current bitwise OR `curr_or` (excluding the current element).

**Time Complexity**
The time complexity of this solution is O(2^n * n), where n is the length of the array `nums`. This is because in the worst case, the `backtrack` function is called 2^n times (once for each possible subset), and in each call, we perform a constant amount of work.

**Space Complexity**
The space complexity of this solution is O(n), which is the space required to store the recursive call stack of the `backtrack` function.

**Key Insight**
The key insight is that the maximum bitwise OR can be achieved by including the maximum element in the subset, and the number of subsets with this maximum bitwise OR can be found by considering all possible combinations of including or excluding each element. This is achieved by using a recursive backtracking approach to explore all possible subsets of the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 215 ms (Beats 71.43%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-07-28 |
| 💻 Language | Python |