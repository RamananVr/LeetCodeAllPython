---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0233.Number%20of%20Digit%20One/README_EN.md
tags:
    - Recursion
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, count <em>the total number of digit </em><code>1</code><em> appearing in all non-negative integers less than or equal to</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Digit DP

This problem essentially asks for the number of times the digit $1$ appears in the given range $[l, ..r]$. The count is related to the number of digits and the value of each digit. We can use the concept of Digit DP to solve this problem. In Digit DP, the size of the number has little impact on the complexity.

For the range $[l, ..r]$ problem, we generally convert it to the problem of $[1, ..r]$ and then subtract the result of $[1, ..l - 1]$, i.e.:

$$
ans = \sum_{i=1}^{r} ans_i -  \sum_{i=1}^{l-1} ans_i
$$

However, for this problem, we only need to find the value for the range $[1, ..r]$.

Here, we use memoized search to implement Digit DP. We search from the starting point downwards, and at the lowest level, we get the number of solutions. We then return the answers layer by layer upwards, and finally get the final answer from the starting point of the search.

The basic steps are as follows:

First, we convert the number $n$ to a string $s$. Then we design a function $\textit{dfs}(i, \textit{cnt}, \textit{limit})$, where:

- The digit $i$ represents the current position being searched, starting from the highest digit, i.e., $i = 0$ represents the highest digit.
- The digit $\textit{cnt}$ represents the current count of the digit $1$ in the number.
- The boolean $\textit{limit}$ indicates whether the current number is restricted by the upper bound.

The function executes as follows:

If $i$ exceeds the length of the number $n$, it means the search is over, directly return $cnt$. If $\textit{limit}$ is true, $up$ is the $i$-th digit of the current number. Otherwise, $up = 9$. Next, we iterate $j$ from $0$ to $up$. For each $j$:

- If $j$ equals $1$, we increment $cnt$ by one.
- Recursively call $\textit{dfs}(i + 1, \textit{cnt}, \textit{limit} \land j = up)$.

The answer is $\textit{dfs}(0, 0, \text{True})$.

The time complexity is $O(m^2 \times D)$, and the space complexity is $O(m^2)$. Here, $m$ is the length of the number $n$, and $D = 10$.

Similar Problems:

Here is the translation of the similar problems into English:

- [357. Count Numbers with Unique Digits](https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0357.Count%20Numbers%20with%20Unique%20Digits/README_EN.md)
- [600. Non-negative Integers without Consecutive Ones](https://github.com/doocs/leetcode/blob/main/solution/0600-0699/0600.Non-negative%20Integers%20without%20Consecutive%20Ones/README_EN.md)
- [788. Rotated Digits](https://github.com/doocs/leetcode/blob/main/solution/0700-0799/0788.Rotated%20Digits/README_EN.md)
- [902. Numbers At Most N Given Digit Set](https://github.com/doocs/leetcode/blob/main/solution/0900-0999/0902.Numbers%20At%20Most%20N%20Given%20Digit%20Set/README_EN.md)
- [1012. Numbers with Repeated Digits](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1012.Numbers%20With%20Repeated%20Digits/README_EN.md)
- [2376. Count Special Integers](https://github.com/doocs/leetcode/blob/main/solution/2300-2399/2376.Count%20Special%20Integers/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        @cache
        def dfs(i: int, cnt: int, limit: bool) -> int:
            if i >= len(s):
                return cnt
            up = int(s[i]) if limit else 9
            ans = 0
            for j in range(up + 1):
                ans += dfs(i + 1, cnt + (j == 1), limit and j == up)
            return ans

        s = str(n)
        return dfs(0, 0, True)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
