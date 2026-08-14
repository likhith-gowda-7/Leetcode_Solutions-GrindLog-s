> 📌 **Cross-listed:** Primary location is [Hash Table/3090-Maximum-Length-Substring-With-Two-Occurrences](../../Hash-Table/3090-Maximum-Length-Substring-With-Two-Occurrences). This problem also appears under: **Hash Table**, **String**, **Sliding Window**

# 3090. Maximum Length Substring With Two Occurrences


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)


## 📝 Problem Description

Given a string `s`, return the **maximum** length of a substring such that it contains *at most two occurrences* of each character.
 

Example 1:**

**Input:** s = "bcbbbcba"

**Output:** 4

**Explanation:**

The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbbbcba"`.

Example 2:**

**Input:** s = "aaaa"

**Output:** 2

**Explanation:**

The following substring has a length of 2 and contains at most two occurrences of each character: `"aaaa"`.

 

**Constraints:**

	- `2 <= s.length <= 100`

	- `s` consists only of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**  
We slide a window over the string while keeping a count of each character inside it. As soon as any character appears three times, the window is too long and we shrink it from the left until that character’s count drops back to two. The longest window we see is the answer.

**Approach**  
1. Create a hash map `freq` to store counts of characters in the current window.  
2. Initialize pointers `l = 0` (left) and `r` will iterate over the string.  
3. For each `r`:  
   - Increment `freq[s[r]]` and the current window length `sub_len`.  
   - While `freq[s[r]] > 2` (the new character has appeared three times):  
     * Decrease `freq[s[l]]` and `sub_len`.  
     * Move `l` one step right.  
   - Update `res` with the maximum of itself and `sub_len`.  
4. Return `res`.

**Time Complexity**  
Each character enters and leaves the window at most once, so the loop runs in **O(n)** time, where *n* is the length of `s`.

**Space Complexity**  
The frequency map holds at most 26 entries (lowercase letters), giving **O(1)** auxiliary space.

**Key Insight**  
The sliding‑window technique guarantees that the window always satisfies the “at most two of each character” rule; when a violation occurs, shrinking from the left restores the condition, ensuring we explore all valid substrings efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 21.08%) |
| 📅 Solved | 2026-08-14 |
| 💻 Language | Python |