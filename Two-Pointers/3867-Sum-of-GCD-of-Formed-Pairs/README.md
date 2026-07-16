> 📌 **Cross-listed:** Primary location is [Array/3867-Sum-of-GCD-of-Formed-Pairs](../../Array/3867-Sum-of-GCD-of-Formed-Pairs). This problem also appears under: **Array**, **Math**, **Two Pointers**, **Sorting**, **Simulation**, **Number Theory**

# 3867. Sum of GCD of Formed Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/)


## 📝 Problem Description

You are given an integer array `nums` of length `n`.

Construct an array `prefixGcd` where for each index `i`:

	- Let `mx_i = max(nums[0], nums[1], ..., nums[i])`.

	- `prefixGcd[i] = gcd(nums[i], mx_i)`.

After constructing `prefixGcd`:

	- Sort `prefixGcd` in **non-decreasing** order.

	- Form pairs by taking the **smallest unpaired** element and the **largest unpaired** element.

	- Repeat this process until no more pairs can be formed.

	- For each formed pair, **compute** the `gcd` of the two elements.

	- If `n` is odd, the **middle** element in the `prefixGcd` array remains **unpaired** and should be ignored.

Return an integer denoting the **sum of the GCD** values of all formed pairs.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.
 

Example 1:**

**Input:** nums = [2,6,4]

**Output:** 2

**Explanation:**

Construct `prefixGcd`:

	
		
			`i`
			`nums[i]`
			`mx_i`
			`prefixGcd[i]`
		
	
	
		
			0
			2
			2
			2
		
		
			1
			6
			6
			6
		
		
			2
			4
			6
			2
		
	

`prefixGcd = [2, 6, 2]`. After sorting, it forms `[2, 2, 6]`.

Pair the smallest and largest elements: `gcd(2, 6) = 2`. The remaining middle element 2 is ignored. Thus, the sum is 2.

Example 2:**

**Input:** nums = [3,6,2,8]

**Output:** 5

**Explanation:**

Construct `prefixGcd`:

	
		
			`i`
			`nums[i]`
			`mx_i`
			`prefixGcd[i]`
		
	
	
		
			0
			3
			3
			3
		
		
			1
			6
			6
			6
		
		
			2
			2
			6
			2
		
		
			3
			8
			8
			8
		
	

`prefixGcd = [3, 6, 2, 8]`. After sorting, it forms `[2, 3, 6, 8]`.

Form pairs: `gcd(2, 8) = 2` and `gcd(3, 6) = 3`. Thus, the sum is `2 + 3 = 5`.

 

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^​​​​​​​9`

## 🧠 Solution Explanation

**Intuition**
The key insight here is to realize that the sum of the GCD values of all formed pairs can be computed by pairing the smallest unpaired element with the largest unpaired element in the sorted `prefixGcd` array. This is because the GCD of two numbers is maximized when one number is a multiple of the other.

**Approach**
1. Construct the `prefixGcd` array by iterating through the input array `nums` and computing the GCD of each element with the maximum element seen so far.
2. Sort the `prefixGcd` array in non-decreasing order.
3. Initialize two pointers, `left` and `right`, to the start and end of the sorted array, respectively.
4. While the two pointers haven't crossed each other, compute the GCD of the elements at the `left` and `right` indices and add it to the `gcd_sum`.
5. Move the `left` pointer to the right and the `right` pointer to the left.
6. If `n` is odd, ignore the middle element in the `prefixGcd` array.

**Time Complexity**
O(n log n) due to the sorting step, where n is the length of the input array `nums`.

**Space Complexity**
O(n) for storing the `prefixGcd` array, where n is the length of the input array `nums`.

**Key Insight**
The key insight here is that the GCD of two numbers is maximized when one number is a multiple of the other, which is why pairing the smallest unpaired element with the largest unpaired element in the sorted `prefixGcd` array gives the maximum possible GCD value.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 205 ms (Beats 57.49%) |
| 💾 Memory | 33.4 MB (Beats 91.62%) |
| 📅 Solved | 2026-07-16 |
| 💻 Language | Python |