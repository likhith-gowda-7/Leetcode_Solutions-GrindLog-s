> 📌 **Cross-listed:** Primary location is [Array/0721-Accounts-Merge](../../Array/0721-Accounts-Merge). This problem also appears under: **Array**, **Hash Table**, **String**, **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Sorting**

# 721. Accounts Merge


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/accounts-merge/)


## 📝 Problem Description

Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are **emails** representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in **any order**.

 

Example 1:**

```

**Input:** accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
**Output:** [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
**Explanation:**
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

```

Example 2:**

```

**Input:** accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
**Output:** [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

```

 

**Constraints:**

	- `1 <= accounts.length <= 1000`

	- `2 <= accounts[i].length <= 10`

	- `1 <= accounts[i][j].length <= 30`

	- `accounts[i][0]` consists of English letters.

	- `accounts[i][j] (for j > 0)` is a valid email.

## 🧠 Solution Explanation

**Intuition**
This solution uses a Union-Find data structure to group accounts with common emails together. By treating each account as a node in a graph and merging nodes with common emails, we can efficiently group accounts belonging to the same person.

**Approach**
1. Initialize a Union-Find data structure with `n` nodes, where `n` is the number of accounts. Each node represents an account, and the `parent` array stores the parent of each node.
2. Iterate through each account and its emails. For each email, check if it's already in the `details` dictionary. If it is, merge the current account with the account associated with the email using the `union` function.
3. After iterating through all accounts, iterate through the `parent` array and merge any nodes that have the same parent (i.e., belong to the same group).
4. Create a new list `user_accounts` to store the merged emails for each group. Iterate through the `user_accounts` dictionary and create a new list for each group, sorting the emails in each list.
5. Return the list of merged accounts, where each account is a list containing the name and sorted emails.

**Time Complexity**
O(n*m*log(n)), where n is the number of accounts and m is the average number of emails per account. The `union` function takes O(log(n)) time, and we perform it n*m times. The sorting operation takes O(m*log(m)) time, and we perform it n times.

**Space Complexity**
O(n+m), where n is the number of accounts and m is the total number of emails. We store the `parent` array, `size` array, `details` dictionary, and `user_accounts` dictionary, which take O(n+m) space.

**Key Insight**
The key insight is to use a Union-Find data structure to efficiently merge accounts with common emails. By treating each account as a node in a graph and merging nodes with common emails, we can group accounts belonging to the same person in O(n*m*log(n)) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 91.37%) |
| 💾 Memory | 20.6 MB (Beats 100%) |
| 📅 Solved | 2025-09-21 |
| 💻 Language | Python |