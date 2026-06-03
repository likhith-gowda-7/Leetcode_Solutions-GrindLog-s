# 1907. Count Salary Categories


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-MySQL-blue) ![Database](https://img.shields.io/badge/Database-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-salary-categories/)


## 📝 Problem Description

Table: `Accounts`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.

```

 

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

	- `"Low Salary"`: All the salaries **strictly less** than `$20000`.

	- `"Average Salary"`: All the salaries in the **inclusive** range `[$20000, $50000]`.

	- `"High Salary"`: All the salaries **strictly greater** than `$50000`.

The result table **must** contain all three categories. If there are no accounts in a category, return `0`.

Return the result table in **any order**.

The result format is in the following example.

 

Example 1:**

```

**Input:** 
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
**Output:** 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
**Explanation:** 
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.

```

## 🧠 Solution Explanation

**Intuition**
The solution uses the `UNION` operator to combine three separate queries, each counting the number of accounts in a specific salary category. This approach works because the `UNION` operator allows us to combine the results of multiple queries into a single result set.

**Approach**
1. The first query counts the number of accounts with an income strictly less than $20,000, categorizing them as "Low Salary".
2. The second query counts the number of accounts with an income between $20,000 and $50,000 (inclusive), categorizing them as "Average Salary".
3. The third query counts the number of accounts with an income strictly greater than $50,000, categorizing them as "High Salary".
4. The `UNION` operator combines the results of these three queries into a single result set, with each query's result set having two columns: "category" and "accounts_count".

**Time Complexity**
O(n) - The `UNION` operator processes each row in the `Accounts` table once, resulting in a linear time complexity.

**Space Complexity**
O(n) - The `UNION` operator requires additional memory to store the combined result set, which can grow up to the size of the `Accounts` table.

**Key Insight**
The key insight here is that the `UNION` operator allows us to combine multiple queries into a single result set, making it easy to count the number of accounts in each salary category. This approach is efficient because it only requires a single pass through the `Accounts` table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1475 ms (Beats 78.58%) |
| 💾 Memory | 0B (Beats 100%) |
| 📅 Solved | 2026-01-31 |
| 💻 Language | MySQL |