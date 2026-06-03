# 295. Find Median from Data Stream


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)


## 📝 Problem Description

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

	- For example, for `arr = [2,3,4]`, the median is `3`.

	- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

	- `MedianFinder()` initializes the `MedianFinder` object.

	- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.

	- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

 

Example 1:**

```

**Input**
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
**Output**
[null, null, null, 1.5, null, 2.0]

**Explanation**
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

```

 

**Constraints:**

	- `-10^5 <= num <= 10^5`

	- There will be at least one element in the data structure before calling `findMedian`.

	- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

 

**Follow up:**

	- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

	- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## 🧠 Solution Explanation

**Intuition**
The solution uses two heaps, a max heap (`small`) and a min heap (`large`), to efficiently maintain the median of the data stream. The max heap stores the smaller half of the numbers, and the min heap stores the larger half. By balancing the sizes of the two heaps, the solution can find the median in constant time.

**Approach**

1. Initialize two heaps, `small` and `large`, to store the smaller and larger halves of the numbers, respectively.
2. In the `addNum` method, check if the sizes of the two heaps are equal. If they are, add the new number to the `small` heap and then move the maximum element from `small` to `large`.
3. If the sizes of the two heaps are not equal, add the new number to the `large` heap and then move the minimum element from `large` to `small`.
4. In the `findMedian` method, check if the sizes of the two heaps are equal. If they are, return the average of the maximum element in `small` and the minimum element in `large`.
5. If the sizes of the two heaps are not equal, return the minimum element in `large`.

**Time Complexity**
The time complexity of the solution is O(log n) for the `addNum` method and O(1) for the `findMedian` method. This is because the heaps are balanced, and the operations on the heaps take logarithmic time.

**Space Complexity**
The space complexity of the solution is O(n), where n is the number of elements in the data stream. This is because the solution uses two heaps to store the elements.

**Key Insight**
The key insight behind this solution is that by balancing the sizes of the two heaps, the solution can find the median in constant time. This is achieved by moving elements between the two heaps based on their sizes, which ensures that the heaps remain balanced.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 111 ms (Beats 99.21%) |
| 💾 Memory | 39.1 MB (Beats 99.99%) |
| 📅 Solved | 2025-07-13 |
| 💻 Language | Python |