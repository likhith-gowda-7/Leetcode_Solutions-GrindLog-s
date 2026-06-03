# 1877. Minimize Maximum Pair Sum in Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)


## 📝 Problem Description

The **pair sum** of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is the largest **pair sum** in a list of pairs.




	- For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the **maximum pair sum** would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.



Given an array `nums` of **even** length `n`, pair up the elements of `nums` into `n / 2` pairs such that:




	- Each element of `nums` is in **exactly one** pair, and

	- The **maximum pair sum **is **minimized**.



Return *the minimized **maximum pair sum** after optimally pairing up the elements*.



 


Example 1:**



```

**Input:** nums = [3,5,2,3]
**Output:** 7
**Explanation:** The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

```


Example 2:**



```

**Input:** nums = [3,5,4,2,4,6]
**Output:** 8
**Explanation:** The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.

```


 


**Constraints:**




	- `n == nums.length`

	- `2 <= n <= 10^5`

	- `n` is **even**.

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by pairing up the smallest and largest numbers in the array, then the second smallest and second largest, and so on. This approach ensures that the maximum pair sum is minimized because we are always pairing up the smallest and largest numbers available.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Initialize two pointers, `l` and `r`, to the start and end of the sorted array, respectively.
3. Initialize a variable `maxi` to store the maximum pair sum found so far.
4. While `l` is less than `r`, calculate the pair sum of the elements at indices `l` and `r`.
5. If the pair sum is greater than the current `maxi`, update `maxi` to the new pair sum.
6. Move the pointers `l` and `r` towards the center of the array by incrementing `l` and decrementing `r`.
7. Repeat steps 4-6 until `l` is no longer less than `r`.
8. Return the final `maxi` value, which represents the minimized maximum pair sum.

**Time Complexity**
O(n log n) due to the sorting step, where n is the length of the input array. The while loop runs in O(n/2) time, but this is dominated by the sorting step.

**Space Complexity**
O(1) (excluding the space required for the input array), since we only use a constant amount of extra space to store the pointers and the `maxi` value.

**Key Insight**
The key insight is that by pairing up the smallest and largest numbers, we are effectively "averaging out" the maximum pair sum. This is because the smallest number is always paired with the largest number, which minimizes the maximum pair sum. This approach is a classic example of the "greedy algorithm" paradigm, where we make locally optimal choices to achieve a global optimum.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 856 ms (Beats 48.36%) |
| 💾 Memory | 33.5 MB (Beats 51.85%) |
| 📅 Solved | 2026-01-24 |
| 💻 Language | Python |