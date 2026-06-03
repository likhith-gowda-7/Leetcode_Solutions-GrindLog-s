# 2634. Filter Elements from Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/filter-elements-from-array/)


## 📝 Problem Description

Given an integer array `arr` and a filtering function `fn`, return a filtered array `filteredArr`.

The `fn` function takes one or two arguments:

	- `arr[i]` - number from the `arr`

	- `i` - index of `arr[i]`

`filteredArr` should only contain the elements from the `arr` for which the expression `fn(arr[i], i)` evaluates to a **truthy** value. A **truthy** value is a value where `Boolean(value)` returns `true`.

Please solve it without the built-in `Array.filter` method.

 

Example 1:**

```

**Input:** arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }
**Output:** [20,30]
**Explanation:**
const newArray = filter(arr, fn); // [20, 30]
The function filters out values that are not greater than 10
```

Example 2:**

```

**Input:** arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }
**Output:** [1]
**Explanation:**
fn can also accept the index of each element
In this case, the function removes elements not at index 0

```

Example 3:**

```

**Input:** arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 }
**Output:** [-2,0,1,2]
**Explanation:**
Falsey values such as 0 should be filtered out

```

 

**Constraints:**

	- `0 <= arr.length <= 1000`

	- `-10^9 <= arr[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating through the input array and applying the provided filtering function to each element. If the function returns a truthy value, the element is added to the filtered array. This approach leverages the fact that JavaScript's `Boolean` function treats certain values (like numbers, strings, and objects) as truthy or falsy based on their inherent properties.

**Approach**
1. Initialize an empty array `filteredArr` to store the filtered elements.
2. Iterate through the input array `arr` using a `for` loop, keeping track of the current index `i`.
3. For each element `arr[i]`, apply the filtering function `fn` by passing `arr[i]` and `i` as arguments.
4. If the filtering function returns a truthy value, add `arr[i]` to the `filteredArr`.
5. After iterating through the entire array, return the `filteredArr`.

**Time Complexity**
O(n), where n is the length of the input array `arr`. This is because we're making a single pass through the array, and the filtering function is evaluated once for each element.

**Space Complexity**
O(n), where n is the length of the input array `arr`. This is because in the worst case, we might need to store all elements of the input array in the `filteredArr`.

**Key Insight**
The key insight here is that we can leverage JavaScript's built-in behavior of treating certain values as truthy or falsy to simplify the filtering process. By using a simple `if` statement to check the return value of the filtering function, we can efficiently create a new array containing only the elements that pass the filter.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 53 ms (Beats 9.22%) |
| 💾 Memory | 49.2 MB (Beats 100%) |
| 📅 Solved | 2024-09-27 |
| 💻 Language | JavaScript |