# 373. Find K Pairs with Smallest Sums


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)


## 📝 Problem Description

You are given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order** and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return *the* `k` *pairs* `(u_1, v_1), (u_2, v_2), ..., (u_k, v_k)` *with the smallest sums*.

 

Example 1:**

```

**Input:** nums1 = [1,7,11], nums2 = [2,4,6], k = 3
**Output:** [[1,2],[1,4],[1,6]]
**Explanation:** The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

```

Example 2:**

```

**Input:** nums1 = [1,1,2], nums2 = [1,2,3], k = 2
**Output:** [[1,1],[1,1]]
**Explanation:** The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 10^5`

	- `-10^9 <= nums1[i], nums2[i] <= 10^9`

	- `nums1` and `nums2` both are sorted in **non-decreasing order**.

	- `1 <= k <= 10^4`

	- `k <= nums1.length * nums2.length`

## 🧠 Solution Explanation

## Intuition
This solution works by utilizing a min-heap to store pairs of elements from the two input arrays, where the heap is ordered by the sum of the pair elements. The heap allows us to efficiently extract the pair with the smallest sum at each step. By maintaining a set of visited pairs, we avoid duplicates and ensure that we return the k pairs with the smallest sums.

## Approach
1. Initialize a min-heap with the first pair of elements from the two input arrays.
2. While the heap is not empty and we have not yet found k pairs, extract the pair with the smallest sum from the heap.
3. Add the extracted pair to the result list and mark it as visited.
4. Push the next possible pairs (i.e., the pair with the next element from the first array and the current element from the second array, and the pair with the current element from the first array and the next element from the second array) into the heap.
5. Repeat steps 2-4 until we have found k pairs or the heap is empty.

## Time Complexity
The time complexity is O(k * log(min(n, m))), where n and m are the lengths of the two input arrays. This is because we perform a heap operation (either push or pop) for each of the k pairs, and each heap operation takes O(log(min(n, m))) time.

## Space Complexity
The space complexity is O(k + min(n, m)), where n and m are the lengths of the two input arrays. This is because we store the k pairs in the result list and at most min(n, m) pairs in the heap at any given time.

## Key Insight
The key insight behind this solution is the use of a min-heap to efficiently find the pair with the smallest sum at each step, allowing us to avoid comparing all possible pairs and reducing the time complexity. By maintaining a set of visited pairs, we also avoid duplicates and ensure that we return the correct k pairs.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 120 ms (Beats 19.12%) |
| 💾 Memory | 34.8 MB (Beats 100%) |
| 📅 Solved | 2025-12-02 |
| 💻 Language | Python |