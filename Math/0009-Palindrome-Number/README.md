# 9. Palindrome Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/palindrome-number/)


## 📝 Problem Description

Given an integer `x`, return `true`* if *`x`* is a ****palindrome****, and *`false`* otherwise*.

 

Example 1:**

```

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

```

Example 2:**

```

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

Example 3:**

```

**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

```

 

**Constraints:**

	- `-2^31 <= x <= 2^31 - 1`

 

**Follow up:** Could you solve it without converting the integer to a string?

## 🧠 Solution Explanation

**Intuition**
The solution checks if a given integer `x` is a palindrome by comparing it with its reverse. This approach works because a palindrome remains the same when its digits are reversed.

**Approach**
1. First, we check if the input `x` is negative. If it is, we immediately return `False` because negative numbers cannot be palindromes.
2. We define a helper function `rev(num)` that calculates the reverse of a given number `num`.
3. Inside `rev(num)`, we use a while loop to extract the last digit of `num` using the modulo operator (`num % 10`).
4. We then remove the last digit from `num` by performing integer division (`num //= 10`).
5. We add the last digit to `reversed_num` by multiplying it by 10 and adding the last digit.
6. We repeat steps 3-5 until `num` becomes 0.
7. Finally, we compare `x` with its reverse `rev(x)` using the `==` operator. If they are equal, we return `True`; otherwise, we return `False`.

**Time Complexity**
O(log x), where x is the input integer. This is because the while loop in the `rev(num)` function runs until `num` becomes 0, which happens in log(x) iterations.

**Space Complexity**
O(1), which means the space complexity is constant. This is because we only use a fixed amount of space to store the variables `reversed_num`, `last`, and `num`, regardless of the input size.

**Key Insight**
The key insight here is that we can reverse a number by repeatedly extracting its last digit and adding it to the reversed number. This approach allows us to check if a number is a palindrome without converting it to a string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 40.99%) |
| 💾 Memory | 19.3 MB (Beats 18.55%) |
| 📅 Solved | 2026-04-02 |
| 💻 Language | Python |