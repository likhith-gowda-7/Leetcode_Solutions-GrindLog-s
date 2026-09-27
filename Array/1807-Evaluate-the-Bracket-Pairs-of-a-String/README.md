# 1807. Evaluate the Bracket Pairs of a String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/)


## 📝 Problem Description

You are given a string `s` that contains some bracket pairs, with each pair containing a **non-empty** key.

	- For example, in the string `"(name)is(age)yearsold"`, there are **two** bracket pairs that contain the keys `"name"` and `"age"`.

You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each `knowledge[i] = [key_i, value_i]` indicates that key `key_i` has a value of `value_i`.

You are tasked to evaluate **all** of the bracket pairs. When you evaluate a bracket pair that contains some key `key_i`, you will:

	- Replace `key_i` and the bracket pair with the key's corresponding `value_i`.

	- If you do not know the value of the key, you will replace `key_i` and the bracket pair with a question mark `"?"` (without the quotation marks).

Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return *the resulting string after evaluating **all** of the bracket pairs.*

 

Example 1:**

```

**Input:** s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
**Output:** "bobistwoyearsold"
**Explanation:**
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

```

Example 2:**

```

**Input:** s = "hi(name)", knowledge = [["a","b"]]
**Output:** "hi?"
**Explanation:** As you do not know the value of the key "name", replace "(name)" with "?".

```

Example 3:**

```

**Input:** s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
**Output:** "yesyesyesaaa"
**Explanation:** The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `0 <= knowledge.length <= 10^5`

	- `knowledge[i].length == 2`

	- `1 <= key_i.length, value_i.length <= 10`

	- `s` consists of lowercase English letters and round brackets `'('` and `')'`.

	- Every open bracket `'('` in `s` will have a corresponding close bracket `')'`.

	- The key in each bracket pair of `s` will be non-empty.

	- There will not be any nested bracket pairs in `s`.

	- `key_i` and `value_i` consist of lowercase English letters.

	- Each `key_i` in `knowledge` is unique.

## 🧠 Solution Explanation

**Intuition**  
Treat the string as a stream of characters. Whenever we see an opening parenthesis we start collecting the key; when we hit the closing parenthesis we look up the key in a dictionary and output the corresponding value or “?”. Outside parentheses we copy characters unchanged.  

**Approach**  
1. Build a hash map `h1` from each `key → value` in `knowledge`.  
2. Scan `s` character by character.  
3. Maintain a flag `found` that is `True` while inside a parenthesis and an empty string `curr` to accumulate the key.  
4. On `'('` set `found = True`.  
5. On `')'` (when `found` is `True`) append `h1[curr]` if the key exists; otherwise append `"?"`. Reset `curr` and `found`.  
6. For any other character:  
   * If `found` is `True`, add it to `curr`.  
   * If `found` is `False`, append it directly to the result string.  
7. Return the built result.  

**Time Complexity**  
O(|s| + |knowledge|).  
Building the map takes O(|knowledge|).  
Scanning the string is a single pass over |s|.  

**Space Complexity**  
O(|knowledge| + |s|).  
The map stores all key–value pairs.  
The result string can grow up to the length of `s` (worst‑case all characters are kept).  

**Key Insight**  
A simple flag (`found`) combined with a running key buffer (`curr`) lets us process the string in one pass, replacing bracketed keys on the fly without extra parsing or recursion.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 48 ms (Beats 64.18%) |
| 💾 Memory | 52 MB (Beats 13.43%) |
| 📅 Solved | 2026-09-26 |
| 💻 Language | Python |