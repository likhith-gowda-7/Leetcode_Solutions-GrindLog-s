> 📌 **Cross-listed:** Primary location is [Array/1980-Find-Unique-Binary-String](../../Array/1980-Find-Unique-Binary-String). This problem also appears under: **Array**, **Hash Table**, **String**, **Backtracking**

# 1980. Find Unique Binary String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-unique-binary-string/)


## 📝 Problem Description

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return *a binary string of length *`n`* that **does not appear** in *`nums`*. If there are multiple answers, you may return **any** of them*.

 

Example 1:**

```

**Input:** nums = ["01","10"]
**Output:** "11"
**Explanation:** "11" does not appear in nums. "00" would also be correct.

```

Example 2:**

```

**Input:** nums = ["00","01"]
**Output:** "11"
**Explanation:** "11" does not appear in nums. "10" would also be correct.

```

Example 3:**

```

**Input:** nums = ["111","011","001"]
**Output:** "101"
**Explanation:** "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 16`

	- `nums[i].length == n`

	- `nums[i] `is either `'0'` or `'1'`.

	- All the strings of `nums` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution works by generating a binary string that is the bitwise XOR of the characters at each index in the input strings. This approach is based on the property that XORing a bit with itself results in 0, and XORing a bit with its complement results in 1.

**Approach**
1. Initialize an empty string `res` to store the result.
2. Iterate over the indices of the input strings `nums`.
3. For each index `i`, calculate the XOR of the character at index `i` in the current string and 1.
4. Convert the result to a string and append it to `res`.
5. Return the resulting binary string `res`.

**Time Complexity**
O(n), where n is the length of the input strings. This is because we are iterating over the indices of the input strings once.

**Space Complexity**
O(n), where n is the length of the input strings. This is because we are storing the result in a string of length n.

**Key Insight**
The key insight is that XORing a bit with itself results in 0, and XORing a bit with its complement results in 1. This property allows us to generate a binary string that is the bitwise XOR of the characters at each index in the input strings, which is guaranteed to be different from any of the input strings.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 92.5%) |
| 📅 Solved | 2026-03-08 |
| 💻 Language | Python |