# 944. Delete Columns to Make Sorted


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted/)


## 📝 Problem Description

You are given an array of `n` strings `strs`, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

	- For example, `strs = ["abc", "bce", "cae"]` can be arranged as follows:

```

abc
bce
cae

```

You want to **delete** the columns that are **not sorted lexicographically**. In the above example (**0-indexed**), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted, while column 1 (`'b'`, `'c'`, `'a'`) is not, so you would delete column 1.

Return *the number of columns that you will delete*.

 

Example 1:**

```

**Input:** strs = ["cba","daf","ghi"]
**Output:** 1
**Explanation:** The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

```

Example 2:**

```

**Input:** strs = ["a","b"]
**Output:** 0
**Explanation:** The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.

```

Example 3:**

```

**Input:** strs = ["zyx","wvu","tsr"]
**Output:** 3
**Explanation:** The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.

```

 

**Constraints:**

	- `n == strs.length`

	- `1 <= n <= 100`

	- `1 <= strs[i].length <= 1000`

	- `strs[i]` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over the columns of the grid, checking if each column is sorted lexicographically. If a column is not sorted, it increments the count of columns to be deleted.

**Approach**
1. Use the `zip(*strs)` function to transpose the grid, resulting in an iterator over the columns.
2. Iterate over each column `s` in the iterator.
3. Check if the column `s` is sorted by comparing it to its sorted version using `sorted(s)`. If the sorted version is not equal to the original column, it means the column is not sorted.
4. If the column is not sorted, increment the count of columns to be deleted.
5. Return the count of columns to be deleted.

**Time Complexity**
O(n*m*log(m)), where n is the number of strings and m is the length of each string. This is because for each column, we are sorting the characters, which takes O(m*log(m)) time. We do this for each of the n columns, resulting in a total time complexity of O(n*m*log(m)).

**Space Complexity**
O(m), where m is the length of each string. This is because we are storing the characters of each column in the `s` variable, which takes O(m) space.

**Key Insight**
The key insight is that we can check if a column is sorted by comparing it to its sorted version. This is a common technique in competitive programming, where we can often solve problems by transforming the input data in a way that makes it easier to analyze. In this case, sorting the column makes it easy to check if it is sorted lexicographically.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 25 ms (Beats 98.79%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-12-20 |
| 💻 Language | Python |