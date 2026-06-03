> 📌 **Cross-listed:** Primary location is [Two Pointers/0125-Valid-Palindrome](../../Two-Pointers/0125-Valid-Palindrome). This problem also appears under: **Two Pointers**, **String**

# 125. Valid Palindrome


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/valid-palindrome/)


## 📝 Problem Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or *`false`* otherwise*.

 

Example 1:**

```

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

```

Example 2:**

```

**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

```

Example 3:**

```

**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

**Constraints:**

	- `1 <= s.length <= 2 * 10^5`

	- `s` consists only of printable ASCII characters.

## 🧠 Solution Explanation

**Intuition**
The solution works by first filtering out non-alphanumeric characters from the input string and converting it to lowercase. Then, it checks if the resulting string is equal to its reverse. This is a common approach to solving palindrome problems, as it simplifies the problem to a basic string comparison.

**Approach**
1. Initialize an empty string `pal` to store the filtered alphanumeric characters.
2. Iterate over each character `i` in the input string `s`, converted to lowercase.
3. Check if `i` is alphanumeric using the `isalnum()` method.
4. If `i` is alphanumeric, append it to the `pal` string.
5. After iterating over the entire string, check if `pal` is equal to its reverse (`pal[::-1]`).
6. Return `True` if `pal` is equal to its reverse, and `False` otherwise.

**Time Complexity**
O(n), where n is the length of the input string. This is because we iterate over the string once to filter out non-alphanumeric characters and again to check if the resulting string is a palindrome.

**Space Complexity**
O(n), where n is the length of the input string. This is because we store the filtered alphanumeric characters in the `pal` string, which can grow up to the length of the input string.

**Key Insight**
The key insight here is that we can simplify the problem of checking if a string is a palindrome by first filtering out non-alphanumeric characters and converting it to lowercase. This allows us to focus on the core problem of comparing two strings, rather than dealing with the complexities of case sensitivity and non-alphanumeric characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 98.98%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-02 |
| 💻 Language | Python |