> 📌 **Cross-listed:** Primary location is [Array/0658-Find-K-Closest-Elements](../../Array/0658-Find-K-Closest-Elements). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Sliding Window**, **Sorting**, **Heap (Priority Queue)**

# 658. Find K Closest Elements


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-k-closest-elements/)


## 📝 Problem Description

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

	- `|a - x| < |b - x|`, or

	- `|a - x| == |b - x|` and `a < b`

 

Example 1:**

**Input:** arr = [1,2,3,4,5], k = 4, x = 3

**Output:** [1,2,3,4]

Example 2:**

**Input:** arr = [1,1,2,3,4,5], k = 4, x = -1

**Output:** [1,1,2,3]

 

**Constraints:**

	- `1 <= k <= arr.length`

	- `1 <= arr.length <= 10^4`

	- `arr` is sorted in **ascending** order.

	- `-10^4 <= arr[i], x <= 10^4`

## 🧠 Solution Explanation

**Intuition**
This solution uses a priority queue (implemented with a heap) to efficiently find the k closest elements to x in the sorted array. The key insight is to use the negative absolute difference between each element and x as the priority, which allows us to easily pop the smallest elements from the heap.

**Approach**
1. Initialize an empty heap and a result list.
2. Iterate through the sorted array, calculating the negative absolute difference between each element and x.
3. If the heap is not full (i.e., its size is less than k), push the element and its difference onto the heap.
4. If the heap is full, check if the smallest element in the heap (i.e., the one with the smallest difference) is smaller than the current element's difference. If so, pop the smallest element from the heap and push the current element onto the heap.
5. After iterating through the entire array, pop all elements from the heap and add them to the result list.
6. Finally, sort the result list in ascending order and return it.

**Time Complexity**
O(n log k), where n is the length of the array. This is because each insertion and deletion operation on the heap takes O(log k) time, and we perform these operations n times.

**Space Complexity**
O(k), as we need to store at most k elements in the heap.

**Key Insight**
The key insight is to use the negative absolute difference between each element and x as the priority, which allows us to easily pop the smallest elements from the heap. This approach takes advantage of the heap data structure's ability to efficiently maintain the smallest element at the top.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 51 ms (Beats 18.82%) |
| 💾 Memory | 19.6 MB (Beats 100%) |
| 📅 Solved | 2025-07-07 |
| 💻 Language | Python |