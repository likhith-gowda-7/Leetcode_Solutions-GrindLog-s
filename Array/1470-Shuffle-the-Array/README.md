# 1470. Shuffle the Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shuffle-the-array/)


## 📝 Problem Description

Given the array `nums` consisting of `2n` elements in the form `[x_1,x_2,...,x_n,y_1,y_2,...,y_n]`.



*Return the array in the form* `[x_1,y_1,x_2,y_2,...,x_n,y_n]`.



 


Example 1:**



```

**Input:** nums = [2,5,1,3,4,7], n = 3
**Output:** [2,3,5,4,1,7] 
**Explanation:** Since x_1=2, x_2=5, x_3=1, y_1=3, y_2=4, y_3=7 then the answer is [2,3,5,4,1,7].

```


Example 2:**



```

**Input:** nums = [1,2,3,4,4,3,2,1], n = 4
**Output:** [1,4,2,3,3,2,4,1]

```


Example 3:**



```

**Input:** nums = [1,1,2,2], n = 2
**Output:** [1,2,1,2]

```


 


**Constraints:**




	- `1 <= n <= 500`

	- `nums.length == 2n`

	- `1 <= nums[i] <= 10^3`

## 🧠 Solution Explanation

**Intuition**
The problem requires rearranging the input array `nums` consisting of `2n` elements into a new array where elements from the first `n` elements are interleaved with elements from the second `n` elements. This can be achieved by iterating over the input array and placing elements at specific indices in the result array.

**Approach**
1. Initialize an empty result array `res` with the same length as the input array `nums`.
2. Initialize an index `idx` to 0, which will be used to keep track of the current element in the input array.
3. Iterate over the input array in steps of 2, starting from index 0. For each pair of elements, place the first element at the current index `i` in the result array and increment `idx` by 1.
4. Iterate over the input array in steps of 2, starting from index 1. For each pair of elements, place the second element at the current index `j` in the result array and increment `idx` by 1.

**Time Complexity**
O(n) - The algorithm iterates over the input array twice, each time in steps of 2, resulting in a total of n iterations.

**Space Complexity**
O(n) - The algorithm creates a new result array of the same length as the input array, which requires additional space proportional to the size of the input array.

**Key Insight**
The key insight is to recognize that the input array can be divided into two interleaved subarrays, and by iterating over the array in steps of 2, we can efficiently construct the desired output array. This approach takes advantage of the fact that the input array has a fixed length of 2n, allowing us to use a simple iterative solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 54 ms (Beats 95.71%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-11-13 |
| 💻 Language | Python |