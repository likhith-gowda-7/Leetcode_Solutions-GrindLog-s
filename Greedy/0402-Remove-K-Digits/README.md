> 📌 **Cross-listed:** Primary location is [String/0402-Remove-K-Digits](../../String/0402-Remove-K-Digits). This problem also appears under: **String**, **Stack**, **Greedy**, **Monotonic Stack**

# 402. Remove K Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-k-digits/)


## 📝 Problem Description

Given string num representing a non-negative integer `num`, and an integer `k`, return *the smallest possible integer after removing* `k` *digits from* `num`.

 

Example 1:**

```

**Input:** num = "1432219", k = 3
**Output:** "1219"
**Explanation:** Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

```

Example 2:**

```

**Input:** num = "10200", k = 1
**Output:** "200"
**Explanation:** Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

```

Example 3:**

```

**Input:** num = "10", k = 2
**Output:** "0"
**Explanation:** Remove all the digits from the number and it is left with nothing which is 0.

```

 

**Constraints:**

	- `1 <= k <= num.length <= 10^5`

	- `num` consists of only digits.

	- `num` does not have any leading zeros except for the zero itself.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the digits that will form the smallest possible number after removing k digits. The key insight is to always remove the largest digit from the stack when it's smaller than the current digit, effectively creating a monotonic stack where each digit is smaller than or equal to the previous one.

**Approach**
1. Initialize an empty stack to store the digits.
2. Iterate through each digit `n` in the input string `num`.
3. While the stack is not empty, `k` is greater than 0, and the current digit `n` is smaller than the top of the stack, pop the top of the stack and decrement `k`. This ensures that the stack always contains the smallest possible digits.
4. Push the current digit `n` onto the stack.
5. After iterating through all digits, remove the last `k` elements from the stack to ensure that we have removed exactly `k` digits.
6. Join the remaining digits in the stack into a string and remove leading zeros using the `lstrip` method. If the resulting string is empty, return "0".

**Time Complexity**
O(n), where n is the length of the input string `num`. This is because we are iterating through each digit in the string once.

**Space Complexity**
O(n), where n is the length of the input string `num`. In the worst case, we may need to push all digits onto the stack.

**Key Insight**
The key to this solution is the use of a monotonic stack, where each digit is smaller than or equal to the previous one. By always removing the largest digit from the stack when it's smaller than the current digit, we ensure that the resulting number is the smallest possible after removing k digits.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 80.15%) |
| 💾 Memory | 19 MB (Beats 100%) |
| 📅 Solved | 2025-02-17 |
| 💻 Language | Python |