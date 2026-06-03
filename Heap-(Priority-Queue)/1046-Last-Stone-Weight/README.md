> 📌 **Cross-listed:** Primary location is [Array/1046-Last-Stone-Weight](../../Array/1046-Last-Stone-Weight). This problem also appears under: **Array**, **Heap (Priority Queue)**

# 1046. Last Stone Weight


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/last-stone-weight/)


## 📝 Problem Description

You are given an array of integers `stones` where `stones[i]` is the weight of the `i^th` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

	- If `x == y`, both stones are destroyed, and

	- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return *the weight of the last remaining stone*. If there are no stones left, return `0`.

 

Example 1:**

```

**Input:** stones = [2,7,4,1,8,1]
**Output:** 1
**Explanation:** 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

```

Example 2:**

```

**Input:** stones = [1]
**Output:** 1

```

 

**Constraints:**

	- `1 <= stones.length <= 30`

	- `1 <= stones[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The key insight here is to use a priority queue (heap) to efficiently find and remove the heaviest stones. By negating the weights, we can use the built-in min-heap functionality of Python's `heapq` module to simulate a max-heap.

**Approach**
1. Negate all stone weights to simulate a max-heap using Python's `heapq` module.
2. Heapify the list of stones to create a valid max-heap.
3. While there are more than one stone left:
   1. Pop the two heaviest stones from the heap.
   2. Calculate the difference in weights between the two stones.
   3. If the difference is non-zero, push the result back into the heap.
4. Return the weight of the last remaining stone, or 0 if the heap is empty.

**Time Complexity**
O(n log n) due to the heapify operation and the repeated heap operations (heappop and heappush). The heap operations themselves take O(log n) time, and we perform them n times in the worst case.

**Space Complexity**
O(n) for storing the stones in the heap.

**Key Insight**
The key to this solution is the clever use of a min-heap to simulate a max-heap, allowing us to efficiently find and remove the heaviest stones. By negating the weights, we can take advantage of the built-in min-heap functionality of Python's `heapq` module, making the solution much more efficient than a naive approach.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-11-22 |
| 💻 Language | Python |