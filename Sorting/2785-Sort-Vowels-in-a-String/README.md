> 📌 **Cross-listed:** Primary location is [String/2785-Sort-Vowels-in-a-String](../../String/2785-Sort-Vowels-in-a-String). This problem also appears under: **String**, **Sorting**

# 2785. Sort Vowels in a String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sort-vowels-in-a-string/)


## 📝 Problem Description

Given a **0-indexed** string `s`, **permute** `s` to get a new string `t` such that:

	- All consonants remain in their original places. More formally, if there is an index `i` with `0 <= i < s.length` such that `s[i]` is a consonant, then `t[i] = s[i]`.

	- The vowels must be sorted in the **nondecreasing** order of their **ASCII** values. More formally, for pairs of indices `i`, `j` with `0 <= i < j < s.length` such that `s[i]` and `s[j]` are vowels, then `t[i]` must not have a higher ASCII value than `t[j]`.

Return *the resulting string*.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

 

Example 1:**

```

**Input:** s = "lEetcOde"
**Output:** "lEOtcede"
**Explanation:** 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.

```

Example 2:**

```

**Input:** s = "lYmpH"
**Output:** "lYmpH"
**Explanation:** There are no vowels in s (all characters in s are consonants), so we return "lYmpH".

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists only of letters of the English alphabet in **uppercase and lowercase**.

## 🧠 Solution Explanation

**Intuition**
The solution involves separating vowels and consonants in the input string, sorting the vowels based on their ASCII values, and then reconstructing the string with vowels in their sorted positions. This approach ensures that vowels are in nondecreasing order of their ASCII values while consonants remain in their original positions.

**Approach**
1. Create a dictionary `vow_map` to store the frequency of each vowel in the string.
2. Create a list `vow_indexes` to store the indices of vowels in the string.
3. Iterate through the string, and for each character:
   - If it's a vowel, increment its frequency in `vow_map` and append its index to `vow_indexes`.
   - If it's a consonant, add it to the result string `res` at its original index.
4. Iterate through the sorted vowels (in ASCII order), and for each vowel:
   - Append it to the result string `res` at the index corresponding to its position in `vow_indexes`.
5. Return the resulting string `res` by joining its characters.

**Time Complexity**
O(n + m), where n is the length of the input string and m is the number of unique vowels. The first loop iterates through the string once, and the second loop iterates through the sorted vowels once. The time complexity is dominated by the string iteration.

**Space Complexity**
O(n + m), where n is the length of the input string and m is the number of unique vowels. The solution uses additional space to store the result string, `vow_map`, and `vow_indexes`.

**Key Insight**
The key insight is to separate vowels and consonants, sort the vowels, and then reconstruct the string with vowels in their sorted positions. This approach ensures that vowels are in nondecreasing order of their ASCII values while consonants remain in their original positions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 63 ms (Beats 95.81%) |
| 💾 Memory | 23.2 MB (Beats 15.3%) |
| 📅 Solved | 2025-09-11 |
| 💻 Language | Python |