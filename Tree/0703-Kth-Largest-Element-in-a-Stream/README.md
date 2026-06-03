# 703. Kth Largest Element in a Stream


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Tree](https://img.shields.io/badge/Tree-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Binary Search Tree](https://img.shields.io/badge/Binary%20Search%20Tree-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/)


## 📝 Problem Description

You are part of a university admissions office and need to keep track of the `kth` highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer `k`, maintains a stream of test scores and continuously returns the `k`th highest test score **after** a new score has been submitted. More specifically, we are looking for the `k`th highest score in the sorted list of all scores.

Implement the `KthLargest` class:

	- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of test scores `nums`.

	- `int add(int val)` Adds a new test score `val` to the stream and returns the element representing the `k^th` largest element in the pool of test scores so far.

 

Example 1:**

**Input:**

["KthLargest", "add", "add", "add", "add", "add"]

[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

**Output:** [null, 4, 5, 5, 8, 8]

**Explanation:**

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);

kthLargest.add(3); // return 4

kthLargest.add(5); // return 5

kthLargest.add(10); // return 5

kthLargest.add(9); // return 8

kthLargest.add(4); // return 8

Example 2:**

**Input:**

["KthLargest", "add", "add", "add", "add"]

[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

**Output:** [null, 7, 7, 7, 8]

**Explanation:**

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);

kthLargest.add(2); // return 7

kthLargest.add(10); // return 7

kthLargest.add(9); // return 7

kthLargest.add(9); // return 8

 

**Constraints:**

	- `0 <= nums.length <= 10^4`

	- `1 <= k <= nums.length + 1`

	- `-10^4 <= nums[i] <= 10^4`

	- `-10^4 <= val <= 10^4`

	- At most `10^4` calls will be made to `add`.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a min-heap to efficiently maintain the kth largest element in the stream of test scores. By storing the k largest elements in the heap, we can quickly determine the kth largest score after adding a new score.

**Approach**
1. Initialize the min-heap with the given stream of test scores `nums`.
2. If the length of the heap exceeds `k`, remove the smallest element (the root of the heap) until the heap contains `k` elements.
3. When adding a new score `val`, check if the heap has less than `k` elements. If so, push `val` onto the heap.
4. If the heap has `k` elements and `val` is greater than the smallest element in the heap (the root), replace the smallest element with `val` using `heapq.heappushpop`.

**Time Complexity**
O(k + log(k)) for the initialization step, where k is the number of elements in the heap. For the `add` method, the time complexity is O(log(k)) because we perform a single heap operation (either push or push-pop).

**Space Complexity**
O(k) for storing the k largest elements in the heap.

**Key Insight**
The key to this solution is using a min-heap to efficiently maintain the k largest elements. By storing the k largest elements in the heap, we can quickly determine the kth largest score after adding a new score. This approach allows us to achieve a time complexity of O(log(k)) for the `add` method.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 96.58%) |
| 💾 Memory | 23.9 MB (Beats 99.99%) |
| 📅 Solved | 2025-07-05 |
| 💻 Language | Python |