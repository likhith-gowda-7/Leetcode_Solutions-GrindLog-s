# 596. Classes With at Least 5 Students


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/classes-with-at-least-5-students/)


## 📝 Problem Description

Table: `Courses`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.

```

 

Write a solution to find all the classes that have **at least five students**.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
**Output:** 
+---------+
| class   |
+---------+
| Math    |
+---------+
**Explanation:** 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.

```

## 🧠 Solution Explanation

**Intuition**
This solution works by grouping the classes together and counting the number of students in each class. It then filters out the classes with less than 5 students, returning only the classes with at least 5 students.

**Approach**
1. The `GROUP BY` clause groups the rows in the `Courses` table by the `class` column.
2. The `COUNT(student)` function counts the number of rows in each group, effectively counting the number of students in each class.
3. The `HAVING` clause filters the results to only include classes with a count of 5 or more students.

**Time Complexity**
O(n), where n is the number of rows in the `Courses` table. This is because the solution needs to iterate over each row once to perform the grouping and counting.

**Space Complexity**
O(n), where n is the number of unique classes in the `Courses` table. This is because the solution needs to store the intermediate results of the grouping and counting in memory.

**Key Insight**
The key insight here is that the `HAVING` clause allows us to filter the results after grouping, which is essential for solving this problem efficiently. By grouping the classes together and then filtering out the classes with less than 5 students, we can avoid having to iterate over each row multiple times, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 305 ms (Beats 93.21%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-26 |
| 💻 Language | MySQL |