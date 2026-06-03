> 📌 **Cross-listed:** Primary location is [Array/0347-Top-K-Frequent-Elements](../../Array/0347-Top-K-Frequent-Elements). This problem also appears under: **Array**, **Hash Table**, **Divide and Conquer**, **Sorting**, **Heap (Priority Queue)**, **Bucket Sort**, **Counting**, **Quickselect**

# 347. Top K Frequent Elements


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

 

Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

	- `k` is in the range `[1, the number of unique elements in the array]`.

	- It is **guaranteed** that the answer is **unique**.

 

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## 🧠 Solution Explanation

### Intuition
The solution works by first counting the frequency of each element in the array using a hash table, and then grouping the elements by their frequency. This approach allows us to efficiently find the top k frequent elements by iterating over the frequency groups in descending order. The key idea is to use the frequency as an index to store the corresponding elements, enabling us to quickly retrieve the top k elements.

### Approach
1. Count the frequency of each element in the array using a hash table (`h1=Counter(nums)`).
2. Create an array of lists (`freq_arr`) where each index represents a frequency, and store the corresponding elements in each list.
3. Initialize an empty result list (`res`) and a counter (`length`) to keep track of the number of elements added to the result.
4. Iterate over the frequency groups in descending order, and for each non-empty group, pop an element and add it to the result list until the desired number of elements (`k`) is reached.

### Time Complexity
The time complexity is O(n), where n is the number of elements in the array. This is because we perform a constant amount of work for each element in the array, including counting its frequency and adding it to the result list.

### Space Complexity
The space complexity is O(n), where n is the number of elements in the array. This is because in the worst case, we need to store all elements in the hash table and the frequency array.

### Key Insight
The key insight is to use the frequency as an index to store the corresponding elements, allowing us to efficiently find the top k frequent elements by iterating over the frequency groups in descending order. This approach enables us to achieve a time complexity better than O(n log n), as required by the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2 ms (Beats 91.39%) |
| 💾 Memory | 21 MB (Beats 100%) |
| 📅 Solved | 2025-07-06 |
| 💻 Language | Python |