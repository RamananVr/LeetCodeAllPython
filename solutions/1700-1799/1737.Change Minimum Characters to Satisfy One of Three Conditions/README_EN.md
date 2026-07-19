---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1737.Change%20Minimum%20Characters%20to%20Satisfy%20One%20of%20Three%20Conditions/README_EN.md
rating: 1952
source: Weekly Contest 225 Q2
tags:
    - Hash Table
    - String
    - Counting
    - Prefix Sum
---

<!-- problem:start -->

# [1737. Change Minimum Characters to Satisfy One of Three Conditions](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions)

## Description

<!-- description:start -->

<p>You are given two strings <code>a</code> and <code>b</code> that consist of lowercase letters. In one operation, you can change any character in <code>a</code> or <code>b</code> to <strong>any lowercase letter</strong>.</p>

<p>Your goal is to satisfy <strong>one</strong> of the following three conditions:</p>

<ul>
	<li><strong>Every</strong> letter in <code>a</code> is <strong>strictly less</strong> than <strong>every</strong> letter in <code>b</code> in the alphabet.</li>
	<li><strong>Every</strong> letter in <code>b</code> is <strong>strictly less</strong> than <strong>every</strong> letter in <code>a</code> in the alphabet.</li>
	<li><strong>Both</strong> <code>a</code> and <code>b</code> consist of <strong>only one</strong> distinct letter.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations needed to achieve your goal.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = &quot;aba&quot;, b = &quot;caa&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Consider the best way to make each condition true:
1) Change b to &quot;ccc&quot; in 2 operations, then every letter in a is less than every letter in b.
2) Change a to &quot;bbb&quot; and b to &quot;aaa&quot; in 3 operations, then every letter in b is less than every letter in a.
3) Change a to &quot;aaa&quot; and b to &quot;aaa&quot; in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = &quot;dabadd&quot;, b = &quot;cda&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The best way is to make condition 1 true by changing b to &quot;eee&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>5</sup></code></li>
	<li><code>a</code> and <code>b</code> consist only of lowercase letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Enumeration

First, we count the number of occurrences of each letter in strings $a$ and $b$, denoted as $cnt_1$ and $cnt_2$.

Then, we consider condition $3$, i.e., every letter in $a$ and $b$ is the same. We just need to enumerate the final letter $c$, and then count the number of letters in $a$ and $b$ that are not $c$. This is the number of characters that need to be changed.

Next, we consider conditions $1$ and $2$, i.e., every letter in $a$ is less than every letter in $b$, or every letter in $b$ is less than every letter in $a$. For condition $1$, we make all characters in string $a$ less than character $c$, and all characters in string $b$ not less than $c$. We enumerate $c$ to find the smallest answer. Condition $2$ is similar.

The final answer is the minimum of the above three cases.

The time complexity is $O(m + n + C^2)$, where $m$ and $n$ are the lengths of strings $a$ and $b$ respectively, and $C$ is the size of the character set. In this problem, $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        def f(cnt1, cnt2):
            for i in range(1, 26):
                t = sum(cnt1[i:]) + sum(cnt2[:i])
                nonlocal ans
                ans = min(ans, t)

        m, n = len(a), len(b)
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for c in a:
            cnt1[ord(c) - ord('a')] += 1
        for c in b:
            cnt2[ord(c) - ord('a')] += 1
        ans = m + n
        for c1, c2 in zip(cnt1, cnt2):
            ans = min(ans, m + n - c1 - c2)
        f(cnt1, cnt2)
        f(cnt2, cnt1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
