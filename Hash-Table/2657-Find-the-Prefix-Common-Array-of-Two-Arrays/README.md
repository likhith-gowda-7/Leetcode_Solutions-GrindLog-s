> 📌 **Cross-listed:** Primary location is [Array/2657-Find-the-Prefix-Common-Array-of-Two-Arrays](../../Array/2657-Find-the-Prefix-Common-Array-of-Two-Arrays). This problem also appears under: **Array**, **Hash Table**, **Bit Manipulation**

# 2657. Find the Prefix Common Array of Two Arrays


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)


## 📝 Problem Description

You are given two **0-indexed **integer** **permutations `A` and `B` of length `n`.

A **prefix common array** of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return *the **prefix common array** of *`A`* and *`B`.

A sequence of `n` integers is called a **permutation** if it contains all integers from `1` to `n` exactly once.

 

Example 1:**

```

**Input:** A = [1,3,2,4], B = [3,1,2,4]
**Output:** [0,2,3,4]
**Explanation:** At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

```

Example 2:**

```

**Input:** A = [2,3,1], B = [3,1,2]
**Output:** [0,1,3]
**Explanation:** At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

```

 

**Constraints:**

	- `1 <= A.length == B.length == n <= 50`

	- `1 <= A[i], B[i] <= n`

	- `It is guaranteed that A and B are both a permutation of n integers.`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a frequency count of elements from both arrays A and B. It iterates through the arrays, incrementing the frequency count for each element. When the frequency count reaches 2, it means the element is present in both arrays at the current index, so the count of common elements is incremented. This count is then appended to the result array.

**Approach**
1. Initialize an array `freq` of size `n+1` to store the frequency count of elements from both arrays.
2. Initialize an empty array `ans` to store the prefix common array.
3. Initialize a variable `cnt` to keep track of the count of common elements.
4. Iterate through the arrays A and B simultaneously using a single loop.
5. For each element at index `i`, increment the frequency count in `freq` for both elements A[i] and B[i].
6. If the frequency count reaches 2 for either element, increment the count of common elements `cnt`.
7. Append the current count of common elements `cnt` to the result array `ans`.
8. Return the result array `ans`.

**Time Complexity**
O(n), where n is the length of the arrays A and B. This is because we are iterating through the arrays once, and the operations within the loop (incrementing frequency counts and checking for duplicates) take constant time.

**Space Complexity**
O(n), where n is the length of the arrays A and B. This is because we are using an array `freq` of size `n+1` to store the frequency counts, and an array `ans` of size n to store the prefix common array.

**Key Insight**
The key insight is to use a frequency count array to efficiently keep track of the elements from both arrays. By incrementing the frequency count for each element and checking for duplicates, we can accurately count the number of common elements at each index. This approach allows us to solve the problem in linear time and space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 61.42%) |
| 💾 Memory | 19.4 MB (Beats 5.19%) |
| 📅 Solved | 2026-05-21 |
| 💻 Language | Python |