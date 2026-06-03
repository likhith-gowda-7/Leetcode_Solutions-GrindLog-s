# 2877. Create a DataFrame from List


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-pythondata-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/create-a-dataframe-from-list/)


## 📝 Problem Description

Write a solution to **create** a DataFrame from a 2D list called `student_data`. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, `student_id` and `age`, and be in the same order as the original 2D list.

The result format is in the following example.

 

Example 1:**

```

**Input:
**student_data:**
**`[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]`
**Output:**
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
**Explanation:**
A DataFrame was created on top of student_data, with two columns named `student_id` and `age`.

```

## 🧠 Solution Explanation

### **Intuition**
This problem asks us to create a pandas DataFrame from a 2D list where each inner list represents a row. It tests basic pandas DataFrame construction.

### **Approach**
1. Import the pandas library
2. Use `pd.DataFrame()` constructor with the input 2D list
3. Specify the column names as the second argument
4. Return the resulting DataFrame

### **Time Complexity**
**O(n × m)** — Where n is the number of rows and m is the number of columns, as pandas needs to process each element.

### **Space Complexity**
**O(n × m)** — The DataFrame stores all elements from the input list.

### **Key Insight**
The pandas DataFrame constructor directly accepts a 2D list as input, making this a straightforward one-liner. The key is knowing the constructor's signature: `pd.DataFrame(data, columns)`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 234 ms (Beats 93.16%) |
| 💾 Memory | 65.5 MB (Beats 97.05%) |
| 📅 Solved | 2024-12-06 |
| 💻 Language | pythondata |