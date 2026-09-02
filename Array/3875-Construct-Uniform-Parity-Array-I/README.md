# 3875. Construct Uniform Parity Array I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-i/)


## 📝 Problem Description

You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

	- `nums2[i] = nums1[i]`

	- `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`

Return `true` if it is possible to construct such an array, otherwise, return `false`.

 

Example 1:**

**Input:** nums1 = [2,3]

**Output:** true

**Explanation:**

	- Choose `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`.

	- Choose `nums2[1] = nums1[1] = 3`.

	- `nums2 = [-1, 3]`, and both elements are odd. Thus, the answer is `true`​​​​​​​.

Example 2:**

**Input:** nums1 = [4,6]

**Output:** true

**Explanation:**​​​​​​​

	- Choose `nums2[0] = nums1[0] = 4`.

	- Choose `nums2[1] = nums1[1] = 6`.

	- `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.

 

**Constraints:**

	- `1 <= n == nums1.length <= 100`

	- `1 <= nums1[i] <= 100`

	- `nums1` consists of distinct integers.

## 🧠 Solution Explanation

**Intuition**  
For any two integers, the parity of their difference is odd iff the numbers have different parity, and even otherwise.  
Because the input numbers are distinct, we can always pick a reference element and use differences to flip parity as needed, guaranteeing a uniform‑parity array.

**Approach**  
1. Observe that if all numbers already share the same parity, we can simply take `nums2[i] = nums1[i]`.  
2. If not, pick any element `x` of one parity and use `nums2[i] = nums1[i] - x` for all `i`.  
   - For indices where `nums1[i]` has the opposite parity of `x`, the difference is odd.  
   - For indices where `nums1[i]` shares parity with `x`, the difference is even.  
   By choosing `x` appropriately (the one with the minority parity), all resulting differences become odd (or all even).  
3. Hence a uniform parity array is always achievable, so the function can simply return `True`.

**Time Complexity**  
`O(1)` – the algorithm performs no iteration or computation based on input size.

**Space Complexity**  
`O(1)` – only a constant amount of auxiliary space is used.

**Key Insight**  
The parity of a difference flips exactly when its operands differ in parity, allowing us to convert any array into all‑odd or all‑even by subtracting a single appropriately chosen element.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 47.47%) |
| 📅 Solved | 2026-09-02 |
| 💻 Language | Python |