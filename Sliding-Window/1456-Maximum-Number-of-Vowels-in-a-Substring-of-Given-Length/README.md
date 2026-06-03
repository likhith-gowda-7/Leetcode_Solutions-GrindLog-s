> 📌 **Cross-listed:** Primary location is [String/1456-Maximum-Number-of-Vowels-in-a-Substring-of-Given-Length](../../String/1456-Maximum-Number-of-Vowels-in-a-Substring-of-Given-Length). This problem also appears under: **String**, **Sliding Window**

# 1456. Maximum Number of Vowels in a Substring of Given Length


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)


## 📝 Problem Description

Given a string `s` and an integer `k`, return *the maximum number of vowel letters in any substring of *`s`* with length *`k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

 

Example 1:**

```

**Input:** s = "abciiidef", k = 3
**Output:** 3
**Explanation:** The substring "iii" contains 3 vowel letters.

```

Example 2:**

```

**Input:** s = "aeiou", k = 2
**Output:** 2
**Explanation:** Any substring of length 2 contains 2 vowels.

```

Example 3:**

```

**Input:** s = "leetcode", k = 3
**Output:** 2
**Explanation:** "lee", "eet" and "ode" contain 2 vowels.

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.

	- `1 <= k <= s.length`

## 🧠 Solution Explanation

**Intuition**
This solution uses a sliding window approach to track the maximum number of vowels in a substring of length `k`. It maintains a count of vowels in the current window and expands the window to the right, updating the count as necessary. When the window exceeds the length `k`, it contracts the window from the left, updating the count again.

**Approach**
1. Initialize variables to keep track of the maximum sum of vowels (`max_sum`), the current sum of vowels (`curr`), and the left and right pointers of the sliding window (`l` and `r`).
2. Iterate over the string `s` using the right pointer `r`.
3. If the character at the right pointer is a vowel, increment the current sum `curr`.
4. If the window size exceeds `k`, increment the left pointer `l` and decrement the current sum `curr` if the character at the left pointer is a vowel.
5. Update the maximum sum `max_sum` if the current sum `curr` is greater.
6. Repeat steps 2-5 until the right pointer reaches the end of the string.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we iterate over the string once, using a single pass through the characters.

**Space Complexity**
O(1), since we only use a constant amount of space to store the variables `max_sum`, `curr`, `l`, and `r`.

**Key Insight**
The key insight here is that we only need to keep track of the maximum sum of vowels in the current window, and we can do this by maintaining a count of vowels in the window and updating it as we expand and contract the window. This allows us to solve the problem in linear time, without having to consider all possible substrings of length `k`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 62 ms (Beats 47.5%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2024-12-12 |
| 💻 Language | Python |