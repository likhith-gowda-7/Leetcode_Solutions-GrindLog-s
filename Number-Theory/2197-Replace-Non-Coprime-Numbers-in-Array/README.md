> 📌 **Cross-listed:** Primary location is [Array/2197-Replace-Non-Coprime-Numbers-in-Array](../../Array/2197-Replace-Non-Coprime-Numbers-in-Array). This problem also appears under: **Array**, **Math**, **Stack**, **Number Theory**

# 2197. Replace Non-Coprime Numbers in Array


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Number Theory](https://img.shields.io/badge/Number%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)


## 📝 Problem Description

You are given an array of integers `nums`. Perform the following steps:

	- Find **any** two **adjacent** numbers in `nums` that are **non-coprime**.

	- If no such numbers are found, **stop** the process.

	- Otherwise, delete the two numbers and **replace** them with their **LCM (Least Common Multiple)**.

	- **Repeat** this process as long as you keep finding two adjacent non-coprime numbers.

Return *the **final** modified array.* It can be shown that replacing adjacent non-coprime numbers in **any** arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are **less than or equal** to `10^8`.

Two values `x` and `y` are **non-coprime** if `GCD(x, y) > 1` where `GCD(x, y)` is the **Greatest Common Divisor** of `x` and `y`.

 

Example 1:**

```

**Input:** nums = [6,4,3,2,7,6,2]
**Output:** [12,7,6]
**Explanation:** 
- (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [**12**,3,2,7,6,2].
- (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [**12**,2,7,6,2].
- (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [**12**,7,6,2].
- (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,**6**].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [12,7,6].
Note that there are other ways to obtain the same resultant array.

```

Example 2:**

```

**Input:** nums = [2,2,1,1,3,3,3]
**Output:** [2,1,1,3]
**Explanation:** 
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,**3**,3].
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,**3**].
- (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [**2**,1,1,3].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [2,1,1,3].
Note that there are other ways to obtain the same resultant array.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- The test cases are generated such that the values in the final array are **less than or equal** to `10^8`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to keep track of the LCM of adjacent non-coprime numbers. It iterates through the input array, and whenever it finds two adjacent non-coprime numbers, it replaces them with their LCM and pushes the new LCM onto the stack.

**Approach**
1. Initialize an empty stack.
2. Iterate through the input array `nums`.
3. For each number `n`, calculate its LCM with the top element of the stack (if the stack is not empty).
4. If the GCD of the top stack element and `n` is greater than 1, it means they are non-coprime. Pop the top stack element, calculate the LCM of the popped element and `n`, and update `n` to this LCM.
5. Repeat step 4 until the stack is empty or the GCD of the top stack element and `n` is 1.
6. Push the updated `n` onto the stack.
7. After iterating through the entire array, return the stack as the final modified array.

**Time Complexity**
O(N * log(M)), where N is the length of the input array and M is the maximum value in the array. This is because we perform a GCD calculation for each pair of adjacent numbers, and GCD calculation has a time complexity of O(log(M)).

**Space Complexity**
O(N), where N is the length of the input array. This is because we use a stack to store the LCM of adjacent non-coprime numbers, and in the worst case, the stack size can grow up to the length of the input array.

**Key Insight**
The key insight here is to use a stack to keep track of the LCM of adjacent non-coprime numbers. By doing so, we can efficiently calculate the LCM of adjacent numbers and replace them with their LCM, resulting in a time complexity of O(N * log(M)).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 115 ms (Beats 78.07%) |
| 💾 Memory | 31.4 MB (Beats 98.25%) |
| 📅 Solved | 2025-09-16 |
| 💻 Language | Python |