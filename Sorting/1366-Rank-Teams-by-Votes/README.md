> 📌 **Cross-listed:** Primary location is [Array/1366-Rank-Teams-by-Votes](../../Array/1366-Rank-Teams-by-Votes). This problem also appears under: **Array**, **Hash Table**, **String**, **Sorting**, **Counting**

# 1366. Rank Teams by Votes


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rank-teams-by-votes/)


## 📝 Problem Description

In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

You are given an array of strings `votes` which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return *a string of all teams **sorted** by the ranking system*.

 

Example 1:**

```

**Input:** votes = ["ABC","ACB","ABC","ACB","ACB"]
**Output:** "ACB"
**Explanation:** 
Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.

```

Example 2:**

```

**Input:** votes = ["WXYZ","XYZW"]
**Output:** "XWYZ"
**Explanation:**
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position. 

```

Example 3:**

```

**Input:** votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
**Output:** "ZMNAGUEDSJYLBOPHRQICWFXTVK"
**Explanation:** Only one voter, so their votes are used for the ranking.

```

 

**Constraints:**

	- `1 <= votes.length <= 1000`

	- `1 <= votes[i].length <= 26`

	- `votes[i].length == votes[j].length` for `0 <= i, j < votes.length`.

	- `votes[i][j]` is an English **uppercase** letter.

	- All characters of `votes[i]` are unique.

	- All the characters that occur in `votes[0]` **also occur** in `votes[j]` where `1 <= j < votes.length`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash map to count the occurrences of each team at each position in the votes. Then, it sorts the teams based on their counts and team letters. This approach works because the ranking system is based on the number of votes for each position, and if there's a tie, it considers the next position until the tie is resolved.

**Approach**
1. Check if there's only one vote, in which case return the team.
2. Initialize a hash map `h1` with default values of 0 for each team at each position.
3. Iterate over each vote and update the count of each team at each position in the hash map.
4. Sort the teams based on their counts and team letters using the `sorted` function with a custom key function.
5. Join the sorted teams into a string using the `join` function.

**Time Complexity**
O(n*m*log(m)), where n is the number of votes and m is the number of teams. The time complexity comes from iterating over the votes (n*m) and sorting the teams (m*log(m)).

**Space Complexity**
O(m), where m is the number of teams. The space complexity comes from storing the counts of each team at each position in the hash map.

**Key Insight**
The key insight is to use a hash map to count the occurrences of each team at each position, which allows us to efficiently sort the teams based on their counts and team letters. This approach is more efficient than iterating over the votes multiple times to count the occurrences of each team.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 13 ms (Beats 83.28%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-02-15 |
| 💻 Language | Python |