> 📌 **Cross-listed:** Primary location is [Array/0875-Koko-Eating-Bananas](../../Array/0875-Koko-Eating-Bananas). This problem also appears under: **Array**, **Binary Search**

# 875. Koko Eating Bananas


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)


## 📝 Problem Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i^th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

 

Example 1:**

```

**Input:** piles = [3,6,7,11], h = 8
**Output:** 4

```

Example 2:**

```

**Input:** piles = [30,11,23,4,20], h = 5
**Output:** 30

```

Example 3:**

```

**Input:** piles = [30,11,23,4,20], h = 6
**Output:** 23

```

 

**Constraints:**

	- `1 <= piles.length <= 10^4`

	- `piles.length <= h <= 10^9`

	- `1 <= piles[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the minimum eating speed `k` that allows Koko to eat all the bananas within `h` hours. The idea is to find the smallest `k` such that the total hours required to eat all the bananas is less than or equal to `h`.

**Approach**
1. Initialize the search range `[l, r]` to `[1, maxi]`, where `maxi` is the maximum number of bananas in any pile.
2. While the search range is not empty, perform the following steps:
   1. Calculate the middle value `k` of the search range.
   2. Initialize a variable `hours` to 0.
   3. Iterate over each pile of bananas. For each pile, calculate the number of hours required to eat it by dividing the number of bananas by `k` and rounding up to the nearest integer. Add this value to `hours`.
   4. If `hours` is greater than `h`, update the search range to `[k+1, r]`. Otherwise, update the search range to `[l, k-1]`.
3. Return the minimum value `k` that satisfies the condition.

**Time Complexity**
O(n log maxi), where n is the number of piles and maxi is the maximum number of bananas in any pile. The binary search takes O(log maxi) time, and the iteration over each pile takes O(n) time.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the search range and the `hours` variable.

**Key Insight**
The key insight is to use a binary search approach to find the minimum eating speed `k`. By iteratively dividing the search range in half and checking if the total hours required to eat all the bananas is less than or equal to `h`, we can efficiently find the smallest `k` that satisfies the condition.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 148 ms (Beats 97.27%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-01 |
| 💻 Language | Python |