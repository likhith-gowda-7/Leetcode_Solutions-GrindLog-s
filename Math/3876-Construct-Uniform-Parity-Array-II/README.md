> 📌 **Cross-listed:** Primary location is [Array/3876-Construct-Uniform-Parity-Array-II](../../Array/3876-Construct-Uniform-Parity-Array-II). This problem also appears under: **Array**, **Math**

# 3876. Construct Uniform Parity Array II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-ii/)


## 📝 Problem Description

You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

	- `nums2[i] = nums1[i]`​​​​​​​

	- `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`, such that `nums1[i] - nums1[j] >= 1`

Return `true` if it is possible to construct such an array, otherwise return `false`.

 

Example 1:**

**Input:** nums1 = [1,4,7]

**Output:** true

**Explanation:**​​​​​​​​​​​​​​

	- Set `nums2[0] = nums1[0] = 1`.

	- Set `nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3`.

	- Set `nums2[2] = nums1[2] = 7`.

	- `nums2 = [1, 3, 7]`, and all elements are odd. Thus, the answer is `true`.

Example 2:**

**Input:** nums1 = [2,3]

**Output:** false

**Explanation:**

It is not possible to construct `nums2` such that all elements have the same parity. Thus, the answer is `false`.

Example 3:**

**Input:** nums1 = [4,6]

**Output:** true

**Explanation:**

	- Set `nums2[0] = nums1[0] = 4`.

	- Set `nums2[1] = nums1[1] = 6`.

	- `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.

 

**Constraints:**

	- `1 <= n == nums1.length <= 10^5`

	- `1 <= nums1[i] <= 10^9`

	- `nums1` consists of distinct integers.

## 🧠 Solution Explanation

**Intuition**  
If we pick the smallest number `m` in the array, every other element can be turned into an odd or even number by either keeping it or subtracting `m`.  
The parity of `m` determines the target parity: if `m` is even we aim for all evens, otherwise all odds. Any element that already has the target parity is fine; otherwise we can subtract `m` to flip its parity, but only if the difference is positive.

**Approach**  
1. Find `m = min(nums)`.  
2. Let `need = 0` if `m` is even, else `1` (desired parity).  
3. For each `val` in `nums`:  
   - If `val % 2 == need`, it already matches the target.  
   - Else check `(val - m) % 2 == need`. If true, we can use `val - m`.  
   - If neither condition holds, construction is impossible → return `False`.  
4. If all elements pass the test, return `True`.

**Time Complexity**  
`O(n)` – one pass to find the minimum and another to validate each element.  
**Space Complexity**  
`O(1)` – only a few integer variables are used regardless of input size.

**Key Insight**  
Subtracting the minimum element from any other element flips its parity while keeping the result positive. Thus, the feasibility depends solely on whether each number can match the target parity directly or after this single subtraction.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 51 ms (Beats 68.9%) |
| 💾 Memory | 35.4 MB (Beats 51.83%) |
| 📅 Solved | 2026-09-03 |
| 💻 Language | Python |