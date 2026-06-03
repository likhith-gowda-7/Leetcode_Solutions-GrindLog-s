> 📌 **Cross-listed:** Primary location is [Depth-First Search/0207-Course-Schedule](../../Depth-First-Search/0207-Course-Schedule). This problem also appears under: **Depth-First Search**, **Breadth-First Search**, **Graph Theory**, **Topological Sort**

# 207. Course Schedule


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Topological Sort](https://img.shields.io/badge/Topological%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/course-schedule/)


## 📝 Problem Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

	- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

 

Example 1:**

```

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** true
**Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

```

Example 2:**

```

**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]
**Output:** false
**Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

```

 

**Constraints:**

	- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= 5000`

	- `prerequisites[i].length == 2`

	- `0 <= a_i, b_i < numCourses`

	- All the pairs prerequisites[i] are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to detect cycles in the graph of courses. If a cycle is found, it means that there's a course that cannot be taken, and the function returns `False`. If no cycles are found, it means that all courses can be taken, and the function returns `True`.

**Approach**
1. Create an adjacency list representation of the graph using the `prerequisites` array.
2. Initialize a `states` array to keep track of the state of each course (unvisited, visiting, or visited).
3. Define a `dfs` function to perform the depth-first search. The function takes a node (course) as input and returns `True` if the course can be taken and `False` otherwise.
4. In the `dfs` function, check if the node is being visited (cycle detected) or has already been visited (course can be taken). If not, mark the node as visiting and recursively call the `dfs` function on its prerequisites.
5. If all courses have been checked and no cycles are found, return `True`.

**Time Complexity**
O(n + m), where n is the number of courses and m is the number of prerequisites. This is because each course and prerequisite is visited at most once.

**Space Complexity**
O(n), where n is the number of courses. This is because we need to store the state of each course in the `states` array.

**Key Insight**
The key insight is that a cycle in the graph of courses indicates that there's a course that cannot be taken, and therefore, all courses cannot be taken. By using DFS to detect cycles, we can efficiently determine whether it's possible to finish all courses.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 87.39%) |
| 💾 Memory | 19.3 MB (Beats 100%) |
| 📅 Solved | 2025-08-10 |
| 💻 Language | Python |