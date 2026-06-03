# 2356. Number of Unique Subjects Taught by Each Teacher


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)


## 📝 Problem Description

Table: `Teacher`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.

```

 

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in **any order**.

The result format is shown in the following example.

 

Example 1:**

```

**Input:** 
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
**Output:**  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
**Explanation:** 
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.

```

## 🧠 Solution Explanation

**Intuition**
The solution works by grouping the teachers by their IDs and counting the number of unique subjects each teacher teaches. This approach is based on the idea that we can use the `GROUP BY` clause to aggregate the data by teacher ID and then use the `COUNT(DISTINCT)` function to count the number of unique subjects for each teacher.

**Approach**
1. The query starts by selecting the `teacher_id` column, which will be used to group the data.
2. The `COUNT(DISTINCT subject_id)` function is used to count the number of unique subjects for each teacher.
3. The `GROUP BY` clause is used to group the data by `teacher_id`, ensuring that the count is performed for each teacher separately.
4. The result is a table with two columns: `teacher_id` and `cnt`, where `cnt` represents the number of unique subjects taught by each teacher.

**Time Complexity**
O(n), where n is the number of rows in the `Teacher` table. This is because the query needs to scan each row in the table to perform the grouping and counting.

**Space Complexity**
O(n), where n is the number of rows in the `Teacher` table. This is because the query needs to store the intermediate results of the grouping and counting in memory.

**Key Insight**
The key insight here is that we can use the `GROUP BY` clause to aggregate the data by teacher ID, which allows us to count the number of unique subjects for each teacher efficiently. This approach is a common technique in SQL for solving problems that involve grouping and counting data.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 468 ms (Beats 97.66%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-25 |
| 💻 Language | MySQL |