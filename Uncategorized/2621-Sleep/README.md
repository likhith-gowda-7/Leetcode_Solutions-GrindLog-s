# 2621. Sleep


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-JavaScript-blue)


🔗 [View on LeetCode](https://leetcode.com/problems/sleep/)


## 📝 Problem Description

Given a positive integer `millis`, write an asynchronous function that sleeps for `millis` milliseconds. It can resolve any value.

**Note** that *minor* deviation from `millis` in the actual sleep duration is acceptable.

 

Example 1:**

```

**Input:** millis = 100
**Output:** 100
**Explanation:** It should return a promise that resolves after 100ms.
let t = Date.now();
sleep(100).then(() => {
  console.log(Date.now() - t); // 100
});

```

Example 2:**

```

**Input:** millis = 200
**Output:** 200
**Explanation:** It should return a promise that resolves after 200ms.

```

 

**Constraints:**

	- `1 <= millis <= 1000`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 57 ms (Beats 5.16%) |
| 💾 Memory | 49 MB (Beats 100%) |
| 📅 Solved | 2024-09-30 |
| 💻 Language | JavaScript |