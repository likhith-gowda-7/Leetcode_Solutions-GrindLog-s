# 619. Biggest Single Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/biggest-single-number/)


## 📝 Problem Description

Table: `MyNumbers`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.

```

 

A **single number** is a number that appeared only once in the `MyNumbers` table.

Find the largest **single number**. If there is no **single number**, report `null`.

The result format is in the following example.

 
 

Example 1:**

```

**Input:** 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
**Output:** 
+-----+
| num |
+-----+
| 6   |
+-----+
**Explanation:** The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.

```

Example 2:**

```

**Input:** 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
**Output:** 
+------+
| num  |
+------+
| null |
+------+
**Explanation:** There are no single numbers in the input table so we return null.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a subquery to find single numbers (numbers that appear only once) in the table, and then selects the maximum of these single numbers. This approach works because it first identifies the single numbers and then finds the largest among them.

**Approach**
1. The subquery groups the numbers in the `MyNumbers` table by their values and counts the occurrences of each number using `count(*) as n`.
2. The `having n=1` clause filters the results to include only numbers that appear once.
3. The outer query selects the maximum number from the results of the subquery.

**Time Complexity**
O(n log n) due to the sorting operation implicitly performed by the `max` function, where n is the number of unique numbers in the table.

**Space Complexity**
O(n) for storing the intermediate results of the subquery, where n is the number of rows in the `MyNumbers` table.

**Key Insight**
The key insight is to use a subquery to identify single numbers and then select the maximum among them, which allows us to avoid iterating through the entire table multiple times. This approach takes advantage of the fact that we only need to find the maximum single number, not all single numbers.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 410 ms (Beats 83.8%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-25 |
| 💻 Language | MySQL |