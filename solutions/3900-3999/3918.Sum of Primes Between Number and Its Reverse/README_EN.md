---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3900-3999/3918.Sum%20of%20Primes%20Between%20Number%20and%20Its%20Reverse/README_EN.md
rating: 1301
source: Weekly Contest 500 Q2
tags:
    - Math
    - Number Theory
---

<!-- problem:start -->

# [3918. Sum of Primes Between Number and Its Reverse](https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code>.</p>

<p>Let <code>r</code> be the integer formed by reversing the digits of <code>n</code>.</p>

<p>Return the <strong>sum</strong> of all <span data-keyword="prime-number">prime numbers</span> between <code>min(n, r)</code> and <code>max(n, r)</code>, inclusive.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 13</span></p>

<p><strong>Output:</strong> <span class="example-io">132</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The reverse of 13 is 31. Thus, the range is <code>[13, 31]</code>.</li>
	<li>The prime numbers in this range are 13, 17, 19, 23, 29, and 31.</li>
	<li>The sum of these prime numbers is <code>13 + 17 + 19 + 23 + 29 + 31 = 132</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">17</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The reverse of 10 is 1. Thus, the range is <code>[1, 10]</code>.</li>
	<li>The prime numbers in this range are 2, 3, 5, and 7.</li>
	<li>The sum of these prime numbers is <code>2 + 3 + 5 + 7 = 17</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 8</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The reverse of 8 is 8. Thus, the range is <code>[8, 8]</code>.</li>
	<li>There are no prime numbers in this range, so the sum is 0.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Precompute Primes

We note that the reversed number $r$ of $n$ will not exceed 1000, so we can precompute all prime numbers up to 1000.

Next, we compute $low = \min(n, r)$ and $high = \max(n, r)$, then iterate through all integers in the range $[low, high]$. If an integer is prime, we add it to the answer.

The time complexity is $O(n)$, and the space complexity is $O(M)$, where $M$ is the upper bound used for prime precomputation, which is 1000 here.

<!-- tabs:start -->

#### Python3

```python
limit = 1000
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        low = min(n, r)
        high = max(n, r)
        return sum(x for x in range(low, high + 1) if is_prime[x])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
