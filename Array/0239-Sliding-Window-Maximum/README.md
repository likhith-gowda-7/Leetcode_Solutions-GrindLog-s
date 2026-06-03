# 239. Sliding Window Maximum


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sliding-window-maximum/)


## 📝 Problem Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

 

Example 1:**

```

**Input:** nums = [1,3,-1,-3,5,3,6,7], k = 3
**Output:** [3,3,5,5,6,7]
**Explanation:** 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       **3**
 1 [3  -1  -3] 5  3  6  7       **3**
 1  3 [-1  -3  5] 3  6  7      ** 5**
 1  3  -1 [-3  5  3] 6  7       **5**
 1  3  -1  -3 [5  3  6] 7       **6**
 1  3  -1  -3  5 [3  6  7]      **7**

```

Example 2:**

```

**Input:** nums = [1], k = 1
**Output:** [1]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

	- `1 <= k <= nums.length`

## 🧠 Solution Explanation

## Intuition
The solution works by maintaining a deque to store the indices of the maximum elements within the current sliding window. This approach ensures that the maximum element is always at the front of the deque, allowing for efficient retrieval and removal of elements as the window moves. The deque is updated based on the comparison of the current element with the elements at the back of the deque.

## Approach
1. Initialize an empty deque `max_queue` to store the indices of the maximum elements and an empty list `res` to store the maximum sliding window values.
2. Iterate over the array using the right pointer `r`, and for each element, remove the elements from the back of the deque that are smaller than the current element.
3. Append the current element to the deque.
4. When the window size is reached (i.e., `r + 1 >= k`), append the maximum element (at the front of the deque) to the result list and remove it from the deque if it is the leftmost element of the window.
5. Move the left pointer `l` to the right to slide the window.

## Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because each element is pushed and popped from the deque at most once, resulting in a linear time complexity.

## Space Complexity
The space complexity is O(n), where n is the length of the input array. This is because in the worst case, the deque can store up to n elements (e.g., when the input array is sorted in descending order).

## Key Insight
The key insight is to use a deque to store the indices of the maximum elements within the current sliding window, allowing for efficient retrieval and removal of elements as the window moves. This approach enables the solution to maintain a time complexity of O(n) and a space complexity of O(n), making it efficient for large input arrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 137 ms (Beats 99.72%) |
| 💾 Memory | 32 MB (Beats 100%) |
| 📅 Solved | 2025-03-26 |
| 💻 Language | Python |