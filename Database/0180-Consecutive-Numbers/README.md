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

## 🧠 Solution Explanation

**Intuition**
The solution uses a common technique in SQL: window functions. By using `lag` and `lead` functions, we can access the previous and next rows in the result set, allowing us to check if a number appears consecutively.

**Approach**
1. Create a temporary view `num_neighbours` that selects the `num` column from the `Logs` table, along with the previous (`back`) and next (`front`) numbers using `lag` and `lead` window functions.
2. Select the `num` column from `num_neighbours` where both `back` and `front` are equal to `num`, indicating consecutive numbers.
3. Use `distinct` to remove duplicates from the result.

**Time Complexity**
O(n), where n is the number of rows in the `Logs` table. This is because we're scanning the table once to create the temporary view, and then scanning it again to select the consecutive numbers.

**Space Complexity**
O(n), as we're creating a temporary view that stores the previous and next numbers for each row. However, this is a reasonable trade-off for the benefits of using window functions.

**Key Insight**
The key insight here is that by using `lag` and `lead` functions, we can effectively "look ahead" and "look behind" each row, allowing us to check for consecutive numbers without having to use self-joins or other more complex techniques. This makes the solution concise and efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 499 ms (Beats 98.34%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-27 |
| 💻 Language | MySQL |