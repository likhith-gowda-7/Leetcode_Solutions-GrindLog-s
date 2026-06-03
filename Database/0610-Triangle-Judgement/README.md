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

## 🧠 Solution Explanation

**Intuition**
The solution uses a simple SQL query to check if the given line segments can form a triangle. The key insight is that a triangle can be formed if the sum of the lengths of any two sides is greater than the length of the third side.

**Approach**
1. The query selects all columns (`*`) from the `Triangle` table.
2. It uses the `IF` function to check the condition for forming a triangle.
3. The condition is `(y+z)>x and (x+z)>y and (x+y)>z`, which checks if the sum of any two sides is greater than the third side.
4. If the condition is true, the `IF` function returns "Yes", otherwise it returns "No".
5. The result is assigned to a new column called `triangle`.

**Time Complexity**
O(n), where n is the number of rows in the `Triangle` table. This is because the query needs to check each row once.

**Space Complexity**
O(1), because the query only uses a constant amount of space to store the result, regardless of the size of the input table.

**Key Insight**
The key insight is that the triangle inequality theorem states that a triangle can be formed if the sum of the lengths of any two sides is greater than the length of the third side. This theorem is used to check if the given line segments can form a triangle.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 276 ms (Beats 88.26%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-27 |
| 💻 Language | MySQL |