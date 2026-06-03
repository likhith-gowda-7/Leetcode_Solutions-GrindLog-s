> 📌 **Cross-listed:** Primary location is [Array/2778-Sum-of-Squares-of-Special-Elements](../../Array/2778-Sum-of-Squares-of-Special-Elements). This problem also appears under: **Array**, **Enumeration**

# 2778. Sum of Squares of Special Elements 


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-of-squares-of-special-elements/)


## 📝 Problem Description

You are given a **1-indexed** integer array `nums` of length `n`.

An element `nums[i]` of `nums` is called **special** if `i` divides `n`, i.e. `n % i == 0`.

Return *the **sum of the squares** of all **special** elements of *`nums`.

 

Example 1:**

```

**Input:** nums = [1,2,3,4]
**Output:** 21
**Explanation:** There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  

```

Example 2:**

```

**Input:** nums = [2,7,1,19,18,3]
**Output:** 63
**Explanation:** There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63. 

```

 

**Constraints:**

	- `1 <= nums.length == n <= 50`

	- `1 <= nums[i] <= 50`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the sum of squares of special elements in a given array. An element is special if its index divides the length of the array. We can achieve this by iterating through the array and checking each index to see if it's a special element.

**Approach**
1. Initialize a variable `res` to store the sum of squares of special elements.
2. Iterate through the array using a for loop, with the loop variable `i` representing the index of the current element.
3. For each index `i`, check if `i+1` divides the length of the array `n` by using the modulo operator (`len(nums)%(i+1)==0`). If it does, the element at index `i` is special.
4. If the element is special, calculate its square by multiplying it with itself (`nums[i]*nums[i]`) and add it to the result `res`.
5. After iterating through the entire array, return the result `res`.

**Time Complexity**
The time complexity of this solution is O(n), where n is the length of the array. This is because we're iterating through the array once, and the operations inside the loop (checking if the index is special and calculating the square) take constant time.

**Space Complexity**
The space complexity of this solution is O(1), which means the space used does not grow with the size of the input array. We're only using a constant amount of space to store the result `res`.

**Key Insight**
The key insight here is that we only need to check if the index `i` divides the length of the array `n`, which is a much simpler condition than checking if `i` is a special element. This allows us to avoid unnecessary calculations and make the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-09 |
| 💻 Language | Python |