# 2784. Check if Array is Good


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-array-is-good/)


## 📝 Problem Description

You are given an integer array `nums`. We consider an array **good **if it is a permutation of an array `base[n]`.

`base[n] = [1, 2, ..., n - 1, n, n] `(in other words, it is an array of length `n + 1` which contains `1` to `n - 1 `exactly once, plus two occurrences of `n`). For example, `base[1] = [1, 1]` and` base[3] = [1, 2, 3, 3]`.

Return `true` *if the given array is good, otherwise return** *`false`.

**Note: **A permutation of integers represents an arrangement of these numbers.

 

Example 1:**

```

**Input:** nums = [2, 1, 3]
**Output:** false
**Explanation:** Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

```

Example 2:**

```

**Input:** nums = [1, 3, 3, 2]
**Output:** true
**Explanation:** Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
```

Example 3:**

```

**Input:** nums = [1, 1]
**Output:** true
**Explanation:** Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.
```

Example 4:**

```

**Input:** nums = [3, 4, 4, 1, 2, 1]
**Output:** false
**Explanation:** Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= num[i] <= 200`

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the input array and checking if it's a permutation of the base array. It does this by comparing the frequency of each number in the array with the expected frequency in the base array. The key insight is that the base array has exactly one duplicate of the largest number, so the solution checks for this condition.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Find the maximum element `n` in the sorted array.
3. Initialize a counter `dup` to keep track of the number of duplicates in the array.
4. Initialize a counter `curr` to keep track of the current number in the array.
5. Check if the first element of the array is 1. If not, return False.
6. Iterate through the array starting from the second element. For each element:
   * If the current element is the same as the previous one, increment `dup` and check if it's not equal to `n`. If so, return False.
   * If the current element is different from the previous one, increment `curr`.
7. After iterating through the array, check if `curr` is equal to `n` and `dup` is equal to 1. If both conditions are met, return True; otherwise, return False.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the length of the input array.

**Space Complexity**
O(1) since the space used does not grow with the size of the input array, excluding the space needed for the output.

**Key Insight**
The solution relies on the fact that the base array has exactly one duplicate of the largest number, which is a crucial property that allows us to determine if the input array is a good array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 21.32%) |
| 📅 Solved | 2026-05-14 |
| 💻 Language | Python |