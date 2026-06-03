# 58. Length of Last Word


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/length-of-last-word/)


## 📝 Problem Description

Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

 

Example 1:**

```

**Input:** s = "Hello World"
**Output:** 5
**Explanation:** The last word is "World" with length 5.

```

Example 2:**

```

**Input:** s = "   fly me   to   the moon  "
**Output:** 4
**Explanation:** The last word is "moon" with length 4.

```

Example 3:**

```

**Input:** s = "luffy is still joyboy"
**Output:** 6
**Explanation:** The last word is "joyboy" with length 6.

```

 

**Constraints:**

	- `1 <= s.length <= 10^4`

	- `s` consists of only English letters and spaces `' '`.

	- There will be at least one word in `s`.

## 🧠 Solution Explanation

**Intuition**
This solution works by splitting the input string into an array of words, then returning the length of the last word in the array. This approach is straightforward because it leverages the built-in string method `split()` to efficiently separate words from spaces.

**Approach**
1. Split the input string `s` into an array of words using the `split()` method, which splits a string into a list where each word is a list item. By default, `split()` separates the string at spaces.
2. Access the last word in the array using the index `-1`, which is a common Python idiom for accessing the last element in a list.
3. Return the length of the last word using the `len()` function.

**Time Complexity**
O(n), where n is the number of words in the input string. This is because the `split()` method needs to iterate over the entire string to separate words from spaces.

**Space Complexity**
O(n), where n is the number of words in the input string. This is because the `split()` method creates a new array of words, which can grow up to the size of the input string.

**Key Insight**
The key insight here is that the `split()` method is a convenient and efficient way to separate words from spaces in a string. By leveraging this method, we can simplify the solution and avoid manual string manipulation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.4 MB (Beats 100%) |
| 📅 Solved | 2024-12-15 |
| 💻 Language | Python |