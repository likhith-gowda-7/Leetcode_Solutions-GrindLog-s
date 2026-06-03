# 955. Delete Columns to Make Sorted II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/)


## 📝 Problem Description

You are given an array of `n` strings `strs`, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have `strs = ["abcdef","uvwxyz"]` and deletion indices `{0, 2, 3}`, then the final array after deletions is `["bef", "vyz"]`.

Suppose we chose a set of deletion indices `answer` such that after deletions, the final array has its elements in **lexicographic** order (i.e., `strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]`). Return *the minimum possible value of* `answer.length`.

 

Example 1:**

```

**Input:** strs = ["ca","bb","ac"]
**Output:** 1
**Explanation:** 
After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.

```

Example 2:**

```

**Input:** strs = ["xc","yb","za"]
**Output:** 0
**Explanation:** 
strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)

```

Example 3:**

```

**Input:** strs = ["zyx","wvu","tsr"]
**Output:** 3
**Explanation:** We have to delete every column.

```

 

**Constraints:**

	- `n == strs.length`

	- `1 <= n <= 100`

	- `1 <= strs[i].length <= 100`

	- `strs[i]` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the minimum number of columns to delete from a set of strings so that the remaining strings are in lexicographic order. The key insight is that we can delete a column if and only if the characters in that column are not in lexicographic order. We can use a greedy approach to iterate through the columns and delete the ones that are not in order.

**Approach**
1. Initialize a boolean array `state` of size `rows` to keep track of whether each row is in lexicographic order with the previous row.
2. Iterate through each column `col` from left to right.
3. For each column, check if the characters in that column are in lexicographic order by iterating through the rows from 1 to `rows-1`.
4. If the characters are not in order, increment the `deleted` count and mark all subsequent rows as not in order.
5. If the characters are in order, mark all subsequent rows as in order.
6. After iterating through all columns, return the `deleted` count.

**Time Complexity**
O(n*m), where n is the number of rows and m is the number of columns. We iterate through each column and each row once.

**Space Complexity**
O(n), where n is the number of rows. We use a boolean array of size n to keep track of whether each row is in lexicographic order.

**Key Insight**
The key insight is that we can delete a column if and only if the characters in that column are not in lexicographic order. This allows us to use a greedy approach to iterate through the columns and delete the ones that are not in order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.5 MB (Beats 100%) |
| 📅 Solved | 2025-12-25 |
| 💻 Language | Python |