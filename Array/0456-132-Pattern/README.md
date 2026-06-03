# 456. 132 Pattern


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/132-pattern/)


## 📝 Problem Description

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

Return `true`* if there is a **132 pattern** in *`nums`*, otherwise, return *`false`*.*

 

Example 1:**

```

**Input:** nums = [1,2,3,4]
**Output:** false
**Explanation:** There is no 132 pattern in the sequence.

```

Example 2:**

```

**Input:** nums = [3,1,4,2]
**Output:** true
**Explanation:** There is a 132 pattern in the sequence: [1, 4, 2].

```

Example 3:**

```

**Input:** nums = [-1,3,2,0]
**Output:** true
**Explanation:** There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 2 * 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack-based approach to find the 132 pattern in the given array. The key insight is to maintain a "mini" value, which represents the minimum value seen so far that is greater than the current element. This allows us to efficiently check for the 132 pattern.

**Approach**
1. Initialize an empty stack and set the "mini" value to negative infinity.
2. Iterate through the array in reverse order.
3. For each element, check if it's less than the current "mini" value. If so, return True, as we've found a 132 pattern.
4. While the stack is not empty and the top element of the stack is less than the current element, pop the stack and update the "mini" value to the popped element. This ensures that the "mini" value is always the minimum value seen so far that is greater than the current element.
5. Push the current element onto the stack.
6. If the iteration completes without finding a 132 pattern, return False.

**Time Complexity**
O(n), where n is the length of the array. This is because we're iterating through the array once in reverse order.

**Space Complexity**
O(n), where n is the length of the array. This is because in the worst case, we might need to push all elements onto the stack.

**Key Insight**
The key to this solution is maintaining the "mini" value, which allows us to efficiently check for the 132 pattern. By updating the "mini" value whenever we pop an element from the stack, we ensure that it always represents the minimum value seen so far that is greater than the current element. This insight enables us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 80.57%) |
| 💾 Memory | 35.5 MB (Beats 100%) |
| 📅 Solved | 2025-02-08 |
| 💻 Language | Python |