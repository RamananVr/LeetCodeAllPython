---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1790.Check%20if%20One%20String%20Swap%20Can%20Make%20Strings%20Equal/README_EN.md
rating: 1300
source: Weekly Contest 232 Q1
tags:
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [1790. Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal)

## Description

<!-- description:start -->

<p>You are given two strings <code>s1</code> and <code>s2</code> of equal length. A <strong>string swap</strong> is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.</p>

<p>Return <code>true</code> <em>if it is possible to make both strings equal by performing <strong>at most one string swap </strong>on <strong>exactly one</strong> of the strings. </em>Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;bank&quot;, s2 = &quot;kanb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> For example, swap the first character with the last character of s2 to make &quot;bank&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;attack&quot;, s2 = &quot;defend&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make them equal with one string swap.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;kelb&quot;, s2 = &quot;kelb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The two strings are already equal, so no string swap operation is required.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>s1.length == s2.length</code></li>
	<li><code>s1</code> and <code>s2</code> consist of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We use a variable $cnt$ to record the number of characters at the same position in the two strings that are different. If the two strings meet the requirements of the problem, then $cnt$ must be $0$ or $2$. We also use two character variables $c1$ and $c2$ to record the characters that are different at the same position in the two strings.

While traversing the two strings simultaneously, for two characters $a$ and $b$ at the same position, if $a \ne b$, then $cnt$ is incremented by $1$. If at this time $cnt$ is greater than $2$, or $cnt$ is $2$ and $a \ne c2$ or $b \ne c1$, then we directly return `false`. Note to record $c1$ and $c2$.

At the end of the traversal, if $cnt \neq 1$, return `true`.

The time complexity is $O(n)$, where $n$ is the length of the string. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        c1 = c2 = None
        for a, b in zip(s1, s2):
            if a != b:
                cnt += 1
                if cnt > 2 or (cnt == 2 and (a != c2 or b != c1)):
                    return False
                c1, c2 = a, b
        return cnt != 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
