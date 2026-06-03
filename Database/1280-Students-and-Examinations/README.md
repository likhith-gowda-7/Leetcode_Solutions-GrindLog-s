# 1280. Students and Examinations


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/students-and-examinations/)


## 📝 Problem Description

Table: `Students`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.

```

 

Table: `Subjects`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.

```

 

Table: `Examinations`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

```

 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by `student_id` and `subject_name`.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
**Output:** 
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
**Explanation:** 
The result table should contain all students and all subjects.
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
Alex did not attend any exams.
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of joins and aggregation to generate a report showing each student's ID, name, and the number of exams they attended for each subject. The key insight is that we need to count the number of exams each student attended for each subject, which requires joining the three tables and grouping the results.

**Approach**
1. Perform a cross join between the `Students` and `Subjects` tables to generate a Cartesian product of all possible student-subject combinations.
2. Left join the `Examinations` table with the result of the cross join to filter out students who did not attend any exams in a particular subject.
3. Group the results by student ID, name, and subject name to count the number of exams each student attended for each subject.
4. Order the results by student ID and name for easier reading.

**Time Complexity**
O(n*m), where n is the number of students and m is the number of subjects. This is because we perform a cross join between the `Students` and `Subjects` tables, which results in n*m rows. The subsequent left join and grouping operations do not change the number of rows, so the time complexity remains O(n*m).

**Space Complexity**
O(n*m), as we need to store the intermediate results of the cross join and left join operations. The final grouping and ordering operations do not affect the space complexity.

**Key Insight**
The key insight is that we can use a cross join to generate all possible student-subject combinations, and then filter out the students who did not attend any exams in a particular subject using a left join. This approach allows us to count the number of exams each student attended for each subject efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 931 ms (Beats 87.24%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-19 |
| 💻 Language | MySQL |