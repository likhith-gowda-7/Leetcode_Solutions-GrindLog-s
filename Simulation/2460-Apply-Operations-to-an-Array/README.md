> 📌 **Cross-listed:** Primary location is [Array/2460-Apply-Operations-to-an-Array](../../Array/2460-Apply-Operations-to-an-Array). This problem also appears under: **Array**, **Two Pointers**, **Simulation**

# 2460. Apply Operations to an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/apply-operations-to-an-array/)


## 📝 Problem Description

You are given a **0-indexed** array `nums` of size `n` consisting of **non-negative** integers.

You need to apply `n - 1` operations to this array where, in the `i^th` operation (**0-indexed**), you will apply the following on the `i^th` element of `nums`:

	- If `nums[i] == nums[i + 1]`, then multiply `nums[i]` by `2` and set `nums[i + 1]` to `0`. Otherwise, you skip this operation.

After performing **all** the operations, **shift** all the `0`'s to the **end** of the array.

	- For example, the array `[1,0,2,0,0,1]` after shifting all its `0`'s to the end, is `[1,2,1,0,0,0]`.

Return *the resulting array*.

**Note** that the operations are applied **sequentially**, not all at once.

 

Example 1:**

```

**Input:** nums = [1,2,2,1,1,0]
**Output:** [1,4,2,0,0,0]
**Explanation:** We do the following operations:
- i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
- i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,**4**,**0**,1,1,0].
- i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
- i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,**2**,**0**,0].
- i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,**0**,**0**].
After that, we shift the 0's to the end, which gives the array [1,4,2,0,0,0].

```

Example 2:**

```

**Input:** nums = [0,1]
**Output:** [1,0]
**Explanation:** No operation can be applied, we just shift the 0 to the end.

```

 

**Constraints:**

	- `2 <= nums.length <= 2000`

	- `0 <= nums[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution involves two main steps: first, we apply the operations to the array by multiplying adjacent equal elements and shifting zeros to the end, and second, we shift all zeros to the end of the array. This approach works because we can iterate through the array once to apply the operations and then another pass to shift the zeros.

**Approach**
1. Iterate through the array from the first element to the second last element (`range(len(nums)-1)`).
2. For each pair of adjacent elements, check if they are equal.
3. If they are equal, multiply the first element by 2 and set the second element to 0.
4. Initialize a pointer `l` to 0, which will keep track of the position where the next non-zero element should be placed.
5. Iterate through the array again and for each non-zero element, place it at the current position `l` and increment `l`.
6. Fill the remaining positions with zeros.
7. Return the modified array.

**Time Complexity**
The time complexity of this solution is O(n), where n is the size of the array. This is because we make two passes through the array: one to apply the operations and another to shift the zeros.

**Space Complexity**
The space complexity of this solution is O(1), excluding the space needed for the output array. This is because we only use a constant amount of space to store the pointer `l` and the temporary variables.

**Key Insight**
The key insight here is that we can apply the operations and shift the zeros in two separate passes, which simplifies the solution and reduces the time complexity. By using a pointer to keep track of the position where the next non-zero element should be placed, we can efficiently shift the zeros to the end of the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-03-01 |
| 💻 Language | Python |