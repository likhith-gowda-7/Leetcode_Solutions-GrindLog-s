> 📌 **Cross-listed:** Primary location is [Array/0332-Reconstruct-Itinerary](../../Array/0332-Reconstruct-Itinerary). This problem also appears under: **Array**, **String**, **Depth-First Search**, **Graph Theory**, **Sorting**, **Heap (Priority Queue)**, **Eulerian Circuit**

# 332. Reconstruct Itinerary


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reconstruct-itinerary/)


## 📝 Problem Description

You are given a list of airline `tickets` where `tickets[i] = [from_i, to_i]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

	- For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg)
```

**Input:** tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
**Output:** ["JFK","MUC","LHR","SFO","SJC"]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg)
```

**Input:** tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
**Output:** ["JFK","ATL","JFK","SFO","ATL","SFO"]
**Explanation:** Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

```

 

**Constraints:**

	- `1 <= tickets.length <= 300`

	- `tickets[i].length == 2`

	- `from_i.length == 3`

	- `to_i.length == 3`

	- `from_i` and `to_i` consist of uppercase English letters.

	- `from_i != to_i`

## 🧠 Solution Explanation

## Intuition
The solution works by building a graph from the given tickets and then performing a depth-first search (DFS) to find the valid itinerary. The use of a heap to store the adjacent nodes ensures that the lexical order is maintained. By exploring the graph in a depth-first manner, we can reconstruct the itinerary in the correct order.

## Approach
1. Create an adjacency list representation of the graph using a dictionary and a heap to store the adjacent nodes.
2. Define a recursive DFS function that explores the graph, popping nodes from the heap and recursively calling itself until all nodes have been visited.
3. Once all nodes have been visited, append the current node to the result list and return.
4. Start the DFS from the node "JFK" and reverse the result list to obtain the correct order.

## Time Complexity
The time complexity is O(n log n) due to the heap operations, where n is the number of tickets. The while loop inside the DFS function runs in O(n) time, but the heap operations (heappush and heappop) take O(log n) time.

## Space Complexity
The space complexity is O(n) as we need to store the adjacency list and the result list, both of which can contain up to n nodes.

## Key Insight
The key insight is to use a heap to store the adjacent nodes, which ensures that the lexical order is maintained when there are multiple valid itineraries. This allows us to efficiently find the correct order of the itinerary by exploring the graph in a depth-first manner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.3 MB (Beats 100%) |
| 📅 Solved | 2025-10-03 |
| 💻 Language | Python |