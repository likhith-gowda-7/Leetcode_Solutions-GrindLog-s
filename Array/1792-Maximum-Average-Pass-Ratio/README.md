# 1792. Maximum Average Pass Ratio


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-average-pass-ratio/)


## 📝 Problem Description

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `classes`, where `classes[i] = [pass_i, total_i]`. You know beforehand that in the `i^th` class, there are `total_i` total students, but only `pass_i` number of students will pass the exam.

You are also given an integer `extraStudents`. There are another `extraStudents` brilliant students that are **guaranteed** to pass the exam of any class they are assigned to. You want to assign each of the `extraStudents` students to a class in a way that **maximizes** the **average** pass ratio across **all** the classes.

The **pass ratio** of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The **average pass ratio** is the sum of pass ratios of all the classes divided by the number of the classes.

Return *the **maximum** possible average pass ratio after assigning the *`extraStudents`* students. *Answers within `10^-5` of the actual answer will be accepted.

 

Example 1:**

```

**Input:** classes = [[1,2],[3,5],[2,2]], `extraStudents` = 2
**Output:** 0.78333
**Explanation:** You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

```

Example 2:**

```

**Input:** classes = [[2,4],[3,9],[4,5],[2,10]], `extraStudents` = 4
**Output:** 0.53485

```

 

**Constraints:**

	- `1 <= classes.length <= 10^5`

	- `classes[i].length == 2`

	- `1 <= pass_i <= total_i <= 10^5`

	- `1 <= extraStudents <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach with a priority queue (max-heap) to maximize the average pass ratio. It iteratively assigns the extra brilliant students to the class with the highest gain in pass ratio, calculated by the difference in pass ratio before and after adding one student.

**Approach**
1. Initialize a max-heap `heap` to store classes with their gain in pass ratio.
2. For each class, calculate the gain in pass ratio by adding one student and push it into the heap.
3. While there are still extra brilliant students, pop the class with the highest gain from the heap, add one student to it, and push it back into the heap.
4. After all extra students are assigned, calculate the average pass ratio by summing the pass ratio of each class and dividing by the total number of classes.

**Time Complexity**
O(n log n) due to the heap operations (push, pop, and heapify). The heap size is initially n (number of classes), and each operation takes O(log n) time.

**Space Complexity**
O(n) for storing the classes in the heap.

**Key Insight**
The key insight is that by maximizing the gain in pass ratio for each class, we effectively maximize the overall average pass ratio. This is because the gain in pass ratio is a measure of how much the pass ratio increases when adding one student to a class, and by choosing the class with the highest gain, we ensure that we are making the most efficient use of the extra brilliant students.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1128 ms (Beats 51.87%) |
| 💾 Memory | 54.9 MB (Beats 100%) |
| 📅 Solved | 2025-09-01 |
| 💻 Language | Python |