# 1146. Snapshot Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Design](https://img.shields.io/badge/Design-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/snapshot-array/)


## 📝 Problem Description

Implement a SnapshotArray that supports the following interface:

	- `SnapshotArray(int length)` initializes an array-like data structure with the given length. **Initially, each element equals 0**.

	- `void set(index, val)` sets the element at the given `index` to be equal to `val`.

	- `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.

	- `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

 

Example 1:**

```

**Input:** ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
**Output:** [null,null,0,null,5]
**Explanation: **
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

 

**Constraints:**

	- `1 <= length <= 5 * 10^4`

	- `0 <= index < length`

	- `0 <= val <= 10^9`

	- `0 <= snap_id < `(the total number of times we call `snap()`)

	- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 180 ms (Beats 52.76%) |
| 💾 Memory | 44.1 MB (Beats 99.8%) |
| 📅 Solved | 2025-02-28 |
| 💻 Language | Python |