> 📌 **Cross-listed:** Primary location is [Array/3312-Sorted-GCD-Pair-Queries](../../Array/3312-Sorted-GCD-Pair-Queries). This problem also appears under: **Array**, **Hash Table**, **Math**, **Binary Search**, **Combinatorics**, **Counting**, **Number Theory**, **Prefix Sum**

# 3312. Sorted GCD Pair Queries


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sorted-gcd-pair-queries/)


## 📝 Problem Description

You are given an integer array `nums` of length `n` and an integer array `queries`.

Let `gcdPairs` denote an array obtained by calculating the GCD of all possible pairs `(nums[i], nums[j])`, where `0 <= i < j < n`, and then sorting these values in **ascending** order.

For each query `queries[i]`, you need to find the element at index `queries[i]` in `gcdPairs`.

Return an integer array `answer`, where `answer[i]` is the value at `gcdPairs[queries[i]]` for each query.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

 

Example 1:**

**Input:** nums = [2,3,4], queries = [0,2,2]

**Output:** [1,2,2]

**Explanation:**

`gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1]`.

After sorting in ascending order, `gcdPairs = [1, 1, 2]`.

So, the answer is `[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]`.

Example 2:**

**Input:** nums = [4,4,2,1], queries = [5,3,1,0]

**Output:** [4,2,1,1]

**Explanation:**

`gcdPairs` sorted in ascending order is `[1, 1, 1, 2, 2, 4]`.

Example 3:**

**Input:** nums = [2,2], queries = [0,0]

**Output:** [2,2]

**Explanation:**

`gcdPairs = [2]`.

 

**Constraints:**

	- `2 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 5 * 10^4`

	- `1 <= queries.length <= 10^5`

	- `0 <= queries[i] < n * (n - 1) / 2`

## 🧠 Solution Explanation

**Intuition**
This solution works by precomputing the frequency of each number in the input array `nums` and then using this frequency information to calculate the number of pairs whose GCD is exactly `g` for each `g` from `1` to `maxVal`. The solution then uses this information to build a prefix sum array `prefix` that stores the number of pairs with GCD less than or equal to `g`. Finally, the solution uses binary search to find the first `g` whose prefix sum is greater than the query value `q`.

**Approach**
1. Calculate the frequency of each number in the input array `nums` and store it in the `freq` array.
2. For each `g` from `1` to `maxVal`, calculate the number of numbers that are divisible by `g` and store it in the `divCnt` array.
3. For each `g` from `maxVal` to `1`, calculate the number of pairs whose GCD is exactly `g` and store it in the `exact` array. This is done by choosing any two numbers divisible by `g` and then removing pairs whose GCD is a larger multiple of `g`.
4. Build a prefix sum array `prefix` that stores the number of pairs with GCD less than or equal to `g`.
5. For each query `q`, use binary search to find the first `g` whose prefix sum is greater than `q` and append this value to the `ans` array.

**Time Complexity**
The time complexity of this solution is O(n + maxVal log maxVal), where n is the length of the input array `nums`. This is because we need to iterate over the input array `nums` to calculate the frequency of each number, and then we need to iterate over the range from `1` to `maxVal` to calculate the number of pairs whose GCD is exactly `g`. The binary search operation takes O(log maxVal) time.

**Space Complexity**
The space complexity of this solution is O(maxVal), where maxVal is the maximum value in the input array `nums`. This is because we need to store the frequency of each number, the number of numbers that are divisible by each `g`, and the prefix sum array.

**Key Insight**
The key insight behind this solution is that we can use the frequency information of each number to calculate the number of pairs whose GCD is exactly `g`. This is done by choosing any two numbers divisible by `g` and then removing pairs whose GCD is a larger multiple of `g`. This approach allows us to efficiently calculate the number of pairs whose GCD is exactly `g` for each `g` from `1` to `maxVal`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 545 ms (Beats 47.5%) |
| 💾 Memory | 39.8 MB (Beats 67.5%) |
| 📅 Solved | 2026-07-17 |
| 💻 Language | Python |