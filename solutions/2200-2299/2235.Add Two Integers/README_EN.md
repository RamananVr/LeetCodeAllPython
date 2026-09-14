---
comments: true
difficulty: Easy
tags:
    - Math
---

<!-- problem:start -->

# [2235. Add Two Integers](https://leetcode.com/problems/add-two-integers)

## Description

<!-- description:start -->

Given two integers <code>num1</code> and <code>num2</code>, return <em>the <strong>sum</strong> of the two integers</em>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 12, num2 = 5
<strong>Output:</strong> 17
<strong>Explanation:</strong> num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = -10, num2 = 4
<strong>Output:</strong> -6
<strong>Explanation:</strong> num1 + num2 = -6, so -6 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100 &lt;= num1, num2 &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Add two integers in $[-100,100]$. The language's addition operator already does this in constant time; no carry handling is required.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 uses the addition operator. Without it we simulate grade-school addition on bits: xor is the sum without carry, and the carry is the bitwise and shifted left, repeated until the carry vanishes.
>
> Python integers are unbounded, so we mask to $32$ bits with $0\texttt{xFFFFFFFF}$. A set sign bit is converted back to a negative Python int via two's complement.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        num1, num2 = num1 & 0xFFFFFFFF, num2 & 0xFFFFFFFF
        while num2:
            carry = ((num1 & num2) << 1) & 0xFFFFFFFF
            num1, num2 = num1 ^ num2, carry
        return num1 if num1 < 0x80000000 else ~(num1 ^ 0xFFFFFFFF)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
