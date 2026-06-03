> 📌 **Cross-listed:** Primary location is [Depth-First Search/0210-Course-Schedule-II](../../Depth-First-Search/0210-Course-Schedule-II). This problem also appears under: **Depth-First Search**, **Breadth-First Search**, **Graph Theory**, **Topological Sort**

# 210. Course Schedule II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Topological Sort](https://img.shields.io/badge/Topological%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/course-schedule-ii/)


## 📝 Problem Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

	- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

 

Example 1:**

```

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** [0,1]
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

```

Example 2:**

```

**Input:** numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
**Output:** [0,2,1,3]
**Explanation:** There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

```

Example 3:**

```

**Input:** numCourses = 1, prerequisites = []
**Output:** [0]

```

 

**Constraints:**

	- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`

	- `prerequisites[i].length == 2`

	- `0 <= a_i, b_i < numCourses`

	- `a_i != b_i`

	- All the pairs `[a_i, b_i]` are **distinct**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a topological sort to find the ordering of courses. The idea is to visit each course in a way that ensures we complete all prerequisites before taking a course. This is possible if and only if the graph of courses and prerequisites is a directed acyclic graph (DAG), which is the case here.

**Approach**
1. Create an adjacency list representation of the graph using the prerequisites.
2. Initialize a state array to keep track of the state of each course (unvisited, visiting, visited).
3. Define a depth-first search (DFS) function that takes a course node as input.
4. In the DFS function:
   - If the course is being visited (state[node] == 1), it means we have a cycle, so return False.
   - If the course has been visited (state[node] == 2), it means we can continue, so return True.
   - Mark the course as visiting (state[node] = 1) and recursively visit all its prerequisites.
   - If any prerequisite has a cycle, return False.
   - Otherwise, mark the course as visited (state[node] = 2) and add it to the order list.
5. Iterate over all courses and call the DFS function for each unvisited course.
6. If any course has a cycle, return an empty list. Otherwise, return the order list.

**Time Complexity**
O(n + m), where n is the number of courses and m is the number of prerequisites. We visit each course and prerequisite once.

**Space Complexity**
O(n + m), where n is the number of courses and m is the number of prerequisites. We store the adjacency list and the state array.

**Key Insight**
The key insight is to use a topological sort to find the ordering of courses. By visiting each course in a way that ensures we complete all prerequisites before taking a course, we can find a valid ordering if and only if the graph is a DAG. The DFS function is used to detect cycles and ensure that we visit each course in a valid order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 75%) |
| 💾 Memory | 19.4 MB (Beats 99.99%) |
| 📅 Solved | 2025-08-26 |
| 💻 Language | Python |