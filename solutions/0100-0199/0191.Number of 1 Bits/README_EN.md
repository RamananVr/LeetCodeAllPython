---
comments: true
difficulty: Easy
tags:
    - Bit Manipulation
    - Divide and Conquer
---

<!-- problem:start -->

# [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits)

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, write a function that returns the number of <span data-keyword="set-bit">set bits</span> in its binary representation (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 11</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The input binary string <strong>1011</strong> has a total of three set bits.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 128</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The input binary string <strong>10000000</strong> has a total of one set bit.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2147483645</span></p>

<p><strong>Output:</strong> <span class="example-io">30</span></p>

<p><strong>Explanation:</strong></p>

<p>The input binary string <strong>1111111111111111111111111111101</strong> has a total of thirty set bits.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If this function is called many times, how would you optimize it?

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Count set bits. Checking every bit always looks at $32$ positions. $n\mathbin{\&}(n-1)$ clears the lowest $1$, so the loop runs once per set bit.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 uses $n\mathbin{\&}(n-1)$. $\textit{lowbit}=n\mathbin{\&}-n$ isolates the lowest $1$; subtract and repeat. Same idea, the form used in Fenwick trees.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n -= n & -n
            ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
