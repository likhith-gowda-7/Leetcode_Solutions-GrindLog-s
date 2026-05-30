# 180. Consecutive Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/consecutive-numbers/)


## 📝 Problem Description

Table: `Logs`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.

```

 

Find all numbers that appear at least three times consecutively.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
**Output:** 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
**Explanation:** 1 is the only number that appears consecutively for at least three times.

```

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 499 ms (Beats 98.04%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-27 |
| 💻 Language | MySQL |