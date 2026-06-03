# 2300. Successful Pairs of Spells and Potions


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)


## 📝 Problem Description

You are given two positive integer arrays `spells` and `potions`, of length `n` and `m` respectively, where `spells[i]` represents the strength of the `i^th` spell and `potions[j]` represents the strength of the `j^th` potion.

You are also given an integer `success`. A spell and potion pair is considered **successful** if the **product** of their strengths is **at least** `success`.

Return *an integer array *`pairs`* of length *`n`* where *`pairs[i]`* is the number of **potions** that will form a successful pair with the *`i^th`* spell.*

 

Example 1:**

```

**Input:** spells = [5,1,3], potions = [1,2,3,4,5], success = 7
**Output:** [4,0,3]
**Explanation:**
- 0^th spell: 5 * [1,2,3,4,5] = [5,**10**,**15**,**20**,**25**]. 4 pairs are successful.
- 1^st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2^nd spell: 3 * [1,2,3,4,5] = [3,6,**9**,**12**,**15**]. 3 pairs are successful.
Thus, [4,0,3] is returned.

```

Example 2:**

```

**Input:** spells = [3,1,2], potions = [8,5,8], success = 16
**Output:** [2,0,2]
**Explanation:**
- 0^th spell: 3 * [8,5,8] = [**24**,15,**24**]. 2 pairs are successful.
- 1^st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2^nd spell: 2 * [8,5,8] = [**16**,10,**16**]. 2 pairs are successful. 
Thus, [2,0,2] is returned.

```

 

**Constraints:**

	- `n == spells.length`

	- `m == potions.length`

	- `1 <= n, m <= 10^5`

	- `1 <= spells[i], potions[i] <= 10^5`

	- `1 <= success <= 10^10`

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the number of potions that will form a successful pair with each spell. The key insight is that we can use a sorted array of potions to efficiently find the number of successful pairs for each spell.

**Approach**
1. Sort the array of potions in ascending order.
2. Initialize an empty list `pairs` to store the number of successful pairs for each spell.
3. Define a helper function `bs` that performs a binary search on the sorted array of potions.
4. For each spell, use the `bs` function to find the index `success_idx` where the product of the spell's strength and the potion's strength is greater than or equal to the `success` threshold.
5. If `success_idx` is equal to the length of the potions array, it means that no potion forms a successful pair with the current spell, so skip it.
6. Otherwise, calculate the number of successful pairs by subtracting `success_idx` from the length of the potions array.
7. Store the number of successful pairs in the `pairs` list.

**Time Complexity**
O(m log m + n), where m is the length of the potions array and n is the length of the spells array. The binary search function `bs` takes O(log m) time, and we call it n times, resulting in a total time complexity of O(n log m). Additionally, we sort the potions array in O(m log m) time.

**Space Complexity**
O(n), where n is the length of the spells array. We store the number of successful pairs for each spell in the `pairs` list, which requires O(n) space.

**Key Insight**
The key insight is that we can use a sorted array of potions to efficiently find the number of successful pairs for each spell. By performing a binary search on the sorted array, we can find the index where the product of the spell's strength and the potion's strength is greater than or equal to the `success` threshold, which allows us to calculate the number of successful pairs in O(log m) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 677 ms (Beats 53.73%) |
| 💾 Memory | 41.4 MB (Beats 100%) |
| 📅 Solved | 2025-10-09 |
| 💻 Language | Python |