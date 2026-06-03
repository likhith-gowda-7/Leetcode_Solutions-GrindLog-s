# 1189. Maximum Number of Balloons


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)


## 📝 Problem Description

Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

 

Example 1:**

**![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG)**

```

**Input:** text = "nlaebolko"
**Output:** 1

```

Example 2:**

**![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG)**

```

**Input:** text = "loonbalxballpoon"
**Output:** 2

```

Example 3:**

```

**Input:** text = "leetcode"
**Output:** 0

```

 

**Constraints:**

	- `1 <= text.length <= 10^4`

	- `text` consists of lower case English letters only.

 

**Note:** This question is the same as [ 2287: Rearrange Characters to Make Target String.](https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/)

## 🧠 Solution Explanation

**Intuition**
The solution works by counting the occurrences of each character in the string `text` and comparing it with the count of the same character in the word "balloon". The maximum number of instances that can be formed is the minimum of these counts divided by the count of the character in "balloon".

**Approach**
1. Check if the character 'b' is present in the string `text`. If not, return 0 as no instances can be formed.
2. Count the occurrences of each character in the string `text` using a `Counter` object `c1`.
3. Count the occurrences of each character in the word "balloon" using a `Counter` object `c2`.
4. Initialize a variable `res` to positive infinity.
5. Iterate over each character in the word "balloon". For each character, update `res` to be the minimum of its current value and the count of the character in `c1` divided by the count of the character in `c2`.

**Time Complexity**
O(n + m), where n is the length of the string `text` and m is the length of the word "balloon". This is because we are iterating over the string `text` once to count the occurrences of each character and iterating over the word "balloon" once to compare the counts.

**Space Complexity**
O(n + m), where n is the length of the string `text` and m is the length of the word "balloon". This is because we are storing the counts of each character in the string `text` and the word "balloon" in two separate `Counter` objects.

**Key Insight**
The key insight is to realize that the maximum number of instances that can be formed is the minimum of the counts of each character in the string `text` divided by the count of the same character in the word "balloon". This is because we can form at most one instance of "balloon" for each occurrence of each character in the string `text`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-01-17 |
| 💻 Language | Python |