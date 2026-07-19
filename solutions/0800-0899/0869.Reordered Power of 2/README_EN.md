---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0869.Reordered%20Power%20of%202/README_EN.md
tags:
    - Hash Table
    - Math
    - Counting
    - Enumeration
    - Sorting
---

<!-- problem:start -->

# [869. Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code>. We reorder the digits in any order (including the original order) such that the leading digit is not zero.</p>

<p>Return <code>true</code> <em>if and only if we can do this so that the resulting number is a power of two</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration

We can enumerate all powers of 2 in the range $[1, 10^9]$ and check if their digit composition is the same as the given number.

Define a function $f(x)$ that represents the digit composition of number $x$. We can convert the number $x$ into an array of length 10, or a string sorted by digit size.

First, we calculate the digit composition of the given number $n$ as $\text{target} = f(n)$. Then, we enumerate $i$ starting from 1, shifting $i$ left by one bit each time (equivalent to multiplying by 2), until $i$ exceeds $10^9$. For each $i$, we calculate its digit composition and compare it with $\text{target}$. If they are the same, we return $\text{true}$; if the enumeration ends without finding the same digit composition, we return $\text{false}$.

Time complexity $O(\log^2 M)$, space complexity $O(\log M)$. Where $M$ is the upper limit of the input range ${10}^9$ for this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def f(x: int) -> List[int]:
            cnt = [0] * 10
            while x:
                x, v = divmod(x, 10)
                cnt[v] += 1
            return cnt

        target = f(n)
        i = 1
        while i <= 10**9:
            if f(i) == target:
                return True
            i <<= 1
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
