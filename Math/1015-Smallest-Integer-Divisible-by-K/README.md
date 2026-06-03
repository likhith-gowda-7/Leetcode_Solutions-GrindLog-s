> 📌 **Cross-listed:** Primary location is [Hash Table/1015-Smallest-Integer-Divisible-by-K](../../Hash-Table/1015-Smallest-Integer-Divisible-by-K). This problem also appears under: **Hash Table**, **Math**

# 1015. Smallest Integer Divisible by K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-integer-divisible-by-k/)


## 📝 Problem Description

Given a positive integer `k`, you need to find the **length** of the **smallest** positive integer `n` such that `n` is divisible by `k`, and `n` only contains the digit `1`.

Return *the **length** of *`n`. If there is no such `n`, return -1.

**Note:** `n` may not fit in a 64-bit signed integer.

 

Example 1:**

```

**Input:** k = 1
**Output:** 1
**Explanation:** The smallest answer is n = 1, which has length 1.

```

Example 2:**

```

**Input:** k = 2
**Output:** -1
**Explanation:** There is no such positive integer n divisible by 2.

```

Example 3:**

```

**Input:** k = 3
**Output:** 3
**Explanation:** The smallest answer is n = 111, which has length 3.

```

 

**Constraints:**

	- `1 <= k <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by iteratively constructing a number consisting only of the digit 1 and checking if it's divisible by the given number `k`. The key insight is that we can use the properties of modular arithmetic to efficiently calculate the remainder of the constructed number when divided by `k`.

**Approach**
1. First, we check if `k` is divisible by 2 or 5, in which case there's no possible number `n` consisting only of the digit 1 that's divisible by `k`, so we return -1.
2. We initialize `n` to 1, which is the smallest possible number consisting only of the digit 1.
3. We then enter a loop that runs from 1 to `k` (inclusive).
4. Inside the loop, we check if `n` is divisible by `k` by calculating the remainder of `n` when divided by `k` using the modulo operator (`n % k == 0`).
5. If `n` is divisible by `k`, we return the current iteration number `i`, which is the length of the smallest number `n` consisting only of the digit 1 that's divisible by `k`.
6. If `n` is not divisible by `k`, we update `n` by appending a digit 1 to its end using the expression `10 * (n % k) + 1`.
7. If the loop completes without finding a number `n` that's divisible by `k`, we return -1.

**Time Complexity**
O(k), where k is the input number. This is because we're iterating from 1 to k in the worst case.

**Space Complexity**
O(1), which means the space complexity is constant. This is because we're only using a fixed amount of space to store the variables `n` and `i`, regardless of the input size.

**Key Insight**
The key insight is that we can use the properties of modular arithmetic to efficiently calculate the remainder of the constructed number when divided by `k`. By appending a digit 1 to the end of `n` and taking the remainder modulo `k`, we can simulate the effect of appending a digit 1 to the end of `n` without having to actually construct the entire number.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 99.93%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-11-25 |
| 💻 Language | Python |