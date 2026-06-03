# 133. Clone Graph


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/clone-graph/)


## 📝 Problem Description

Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph)** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```

class Node {
    public int val;
    public List<Node> neighbors;
}

```

 

**Test case format:**

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

**An adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)
```

**Input:** adjList = [[2,4],[1,3],[2,4],[1,3]]
**Output:** [[2,4],[1,3],[2,4],[1,3]]
**Explanation:** There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/07/graph.png)
```

**Input:** adjList = [[]]
**Output:** [[]]
**Explanation:** Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

```

Example 3:**

```

**Input:** adjList = []
**Output:** []
**Explanation:** This an empty graph, it does not have any nodes.

```

 

**Constraints:**

	- The number of nodes in the graph is in the range `[0, 100]`.

	- `1 <= Node.val <= 100`

	- `Node.val` is unique for each node.

	- There are no repeated edges and no self-loops in the graph.

	- The Graph is connected and all nodes can be visited starting from the given node.

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of a hash map and a stack to perform a depth-first search (DFS) traversal of the graph. By mapping each original node to its deep copy, we can efficiently construct the cloned graph.

**Approach**
1. Initialize a hash map `clone_map` to store the mapping between original nodes and their deep copies.
2. If the input node is `None`, return `None` immediately.
3. Create a deep copy of the input node and store it in `clone_map`.
4. Initialize a stack with the input node.
5. While the stack is not empty, pop a node `v` from the stack.
6. For each neighbor `n` of `v`, if `n` is not in `clone_map`, create a new deep copy of `n` and store it in `clone_map`.
7. Add `n` to the stack.
8. Add the deep copy of `n` to the neighbors of the deep copy of `v`.
9. Return the deep copy of the input node.

**Time Complexity**
O(N + M), where N is the number of nodes and M is the number of edges. We visit each node and edge once during the DFS traversal.

**Space Complexity**
O(N + M), where N is the number of nodes and M is the number of edges. We store the mapping between original nodes and their deep copies in the hash map, and we use a stack to store nodes during the DFS traversal.

**Key Insight**
The key insight is to use a hash map to efficiently store and retrieve the mapping between original nodes and their deep copies. This allows us to avoid visiting the same node multiple times during the DFS traversal, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 48 ms (Beats 70.25%) |
| 💾 Memory | 19.8 MB (Beats 18.37%) |
| 📅 Solved | 2026-01-08 |
| 💻 Language | Python |