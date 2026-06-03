> 📌 **Cross-listed:** Primary location is [Array/2616-Minimize-the-Maximum-Difference-of-Pairs](../../Array/2616-Minimize-the-Maximum-Difference-of-Pairs). This problem also appears under: **Array**, **Binary Search**, **Dynamic Programming**, **Greedy**, **Sorting**

# 2616. Minimize the Maximum Difference of Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` and an integer `p`. Find `p` pairs of indices of `nums` such that the **maximum** difference amongst all the pairs is **minimized**. Also, ensure no index appears more than once amongst the `p` pairs.

Note that for a pair of elements at the index `i` and `j`, the difference of this pair is `|nums[i] - nums[j]|`, where `|x|` represents the **absolute** **value** of `x`.

Return *the **minimum** **maximum** difference among all *`p` *pairs.* We define the maximum of an empty set to be zero.

 

Example 1:**

```

**Input:** nums = [10,1,2,7,1,3], p = 2
**Output:** 1
**Explanation:** The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

```

Example 2:**

```

**Input:** nums = [4,2,1,2], p = 1
**Output:** 0
**Explanation:** Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

	- `0 <= p <= (nums.length)/2`

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the minimum maximum difference among all pairs of indices in the given array `nums` such that the number of pairs is `p`. The key insight is to use binary search to find the minimum maximum difference by considering the pairs formed by consecutive elements in the sorted array.

**Approach**

1. First, sort the array `nums` in ascending order.
2. Define a helper function `check(mid, length)` to check if it's possible to form at least `p` pairs with a maximum difference of `mid`.
   - Initialize `pairs` to 0 and `i` to 1.
   - Iterate through the array from index 1 to the end.
   - If the difference between the current element and the previous element is less than or equal to `mid`, increment `pairs` and move to the next pair (i.e., increment `i` by 2).
   - Otherwise, increment `i` by 1.
   - Return `True` if `pairs` is greater than or equal to `p`, and `False` otherwise.
3. Initialize `left` to 0 (minimum possible maximum difference) and `right` to the maximum possible maximum difference (difference between the last and first elements of the array).
4. Perform binary search to find the minimum maximum difference.
   - Calculate the mid value and call the `check(mid, length)` function.
   - If it's possible to form at least `p` pairs with a maximum difference of `mid`, update `right` to `mid - 1`.
   - Otherwise, update `left` to `mid + 1`.
5. Return the minimum maximum difference found.

**Time Complexity**
The time complexity is O(n log n) due to the sorting of the array, where n is the length of the array. The binary search has a time complexity of O(log n), but it's dominated by the sorting step.

**Space Complexity**
The space complexity is O(1) (excluding the space required for the input array), as we only use a constant amount of space to store the variables.

**Key Insight**
The key insight is to use binary search to find the minimum maximum difference by considering the pairs formed by consecutive elements in the sorted array. This approach allows us to efficiently find the minimum maximum difference among all pairs of indices.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 307 ms (Beats 95.16%) |
| 💾 Memory | 32.6 MB (Beats 99.65%) |
| 📅 Solved | 2025-06-14 |
| 💻 Language | Python |