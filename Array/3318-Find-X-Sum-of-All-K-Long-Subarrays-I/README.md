# 3318. Find X-Sum of All K-Long Subarrays I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)


## 📝 Problem Description

You are given an array `nums` of `n` integers and two integers `k` and `x`.

The **x-sum** of an array is calculated by the following procedure:

	- Count the occurrences of all elements in the array.

	- Keep only the occurrences of the top `x` most frequent elements. If two elements have the same number of occurrences, the element with the **bigger** value is considered more frequent.

	- Calculate the sum of the resulting array.

**Note** that if an array has less than `x` distinct elements, its **x-sum** is the sum of the array.

Return an integer array `answer` of length `n - k + 1` where `answer[i]` is the **x-sum** of the subarray `nums[i..i + k - 1]`.

 

Example 1:**

**Input:** nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

**Output:** [6,10,12]

**Explanation:**

	- For subarray `[1, 1, 2, 2, 3, 4]`, only elements 1 and 2 will be kept in the resulting array. Hence, `answer[0] = 1 + 1 + 2 + 2`.

	- For subarray `[1, 2, 2, 3, 4, 2]`, only elements 2 and 4 will be kept in the resulting array. Hence, `answer[1] = 2 + 2 + 2 + 4`. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.

	- For subarray `[2, 2, 3, 4, 2, 3]`, only elements 2 and 3 are kept in the resulting array. Hence, `answer[2] = 2 + 2 + 2 + 3 + 3`.

Example 2:**

**Input:** nums = [3,8,7,8,7,5], k = 2, x = 2

**Output:** [11,15,15,15,12]

**Explanation:**

Since `k == x`, `answer[i]` is equal to the sum of the subarray `nums[i..i + k - 1]`.

 

**Constraints:**

	- `1 <= n == nums.length <= 50`

	- `1 <= nums[i] <= 50`

	- `1 <= x <= k <= nums.length`

## 🧠 Solution Explanation

**Intuition**
This solution uses a combination of a frequency array and a priority queue to efficiently calculate the x-sum of subarrays. The key insight is to maintain a sliding window of size k and update the frequency array and priority queue accordingly.

**Approach**
1. Initialize a frequency array `freq` to store the count and value of each element in the array.
2. Create a priority queue `heap` to store the top x most frequent elements.
3. Iterate through the array, updating the frequency array and priority queue for each subarray of size k.
4. For each subarray, pop elements from the priority queue until it has less than x elements or the count of the top element is 0.
5. Calculate the x-sum by multiplying the count of each element by its value and summing the results.
6. Append the x-sum to the result array.
7. Repeat steps 3-6 until the end of the array is reached.

**Time Complexity**
O(n log x), where n is the length of the array and x is the number of top frequent elements. The priority queue operations (insert, delete, and extract_min) take O(log x) time, and we perform these operations n times.

**Space Complexity**
O(n + x), where n is the length of the array and x is the number of top frequent elements. We store the frequency array and priority queue, which take O(n + x) space.

**Key Insight**
The key insight is to use a priority queue to efficiently maintain the top x most frequent elements, allowing us to calculate the x-sum of subarrays in O(n log x) time. This approach avoids the need to sort the entire array or use a complex data structure, making it efficient and scalable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 94.59%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-11-04 |
| 💻 Language | Python |