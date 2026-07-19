---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3770.Largest%20Prime%20from%20Consecutive%20Prime%20Sum/README_EN.md
rating: 1546
source: Weekly Contest 479 Q2
tags:
    - Array
    - Math
    - Number Theory
---

<!-- problem:start -->

# [3770. Largest Prime from Consecutive Prime Sum](https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code>.</p>

<p>Return the <strong>largest <span data-keyword="prime-number">prime number</span></strong> less than or equal to <code>n</code> that can be expressed as the <strong>sum</strong> of one or more <strong>consecutive prime numbers</strong> starting from 2. If no such number exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 20</span></p>

<p><strong>Output:</strong> <span class="example-io">17</span></p>

<p><strong>Explanation:</strong></p>

<p>The prime numbers less than or equal to <code>n = 20</code> which are consecutive prime sums are:</p>

<ul>
	<li>
	<p><code>2 = 2</code></p>
	</li>
	<li>
	<p><code>5 = 2 + 3</code></p>
	</li>
	<li>
	<p><code>17 = 2 + 3 + 5 + 7</code></p>
	</li>
</ul>

<p>The largest is 17, so it is the answer.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The only consecutive prime sum less than or equal to 2 is 2 itself.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Binary Search

We can preprocess a list of all prime numbers less than or equal to $5 \times 10^5$, then calculate the consecutive prime sums starting from 2, and store those sums that are prime numbers in an array $s$.

For each query, we simply need to use binary search in array $s$ to find the maximum value less than or equal to $n$.

In terms of time complexity, preprocessing the primes takes $O(M \log \log M)$ time, and each query takes $O(\log k)$ time, where $M$ is the upper limit of preprocessing, and $k$ is the length of array $s$. In this problem, $k \leq 40$.

<!-- tabs:start -->

#### Python3

```python
mx = 500000
is_prime = [True] * (mx + 1)
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, mx + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, mx + 1, i):
            is_prime[j] = False
s = [0]
t = 0
for x in primes:
    t += x
    if t > mx:
        break
    if is_prime[t]:
        s.append(t)

class Solution:
    def largestPrime(self, n: int) -> int:
        i = bisect_right(s, n) - 1
        return s[i]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
