# 610. Triangle Judgement


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/triangle-judgement/)


## 📝 Problem Description

Table: `Triangle`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

```

 

Report for every three line segments whether they can form a triangle.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
**Output:** 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

```

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 276 ms (Beats 86.75%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-27 |
| 💻 Language | MySQL |