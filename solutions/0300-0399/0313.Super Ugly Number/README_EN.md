---
comments: true
difficulty: Medium
tags:
    - Array
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [313. Super Ugly Number](https://leetcode.com/problems/super-ugly-number)

## Description

<!-- description:start -->

<p>A <strong>super ugly number</strong> is a positive integer whose prime factors are in the array <code>primes</code>.</p>

<p>Given an integer <code>n</code> and an array of integers <code>primes</code>, return <em>the</em> <code>n<sup>th</sup></code> <em><strong>super ugly number</strong></em>.</p>

<p>The <code>n<sup>th</sup></code> <strong>super ugly number</strong> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 12, primes = [2,7,13,19]
<strong>Output:</strong> 32
<strong>Explanation:</strong> [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, primes = [2,3,5]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= primes.length &lt;= 100</code></li>
	<li><code>2 &lt;= primes[i] &lt;= 1000</code></li>
	<li><code>primes[i]</code> is <strong>guaranteed</strong> to be a prime number.</li>
	<li>All the values of <code>primes</code> are <strong>unique</strong> and sorted in <strong>ascending order</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Min Heap)

<!-- thinking:start -->

> **Thinking**
>
> A super ugly number uses only the given primes. Trial-dividing every integer is too slow for large $n$.
>
> Start from $1$, pop the heap minimum $x$, and push $x\times p$ when it does not overflow. If $x$ is divisible by the current prime, skip later primes (Euler-sieve style). The $n$-th pop is the answer.

<!-- thinking:end -->

We use a priority queue (min heap) to maintain all possible super ugly numbers, initially putting $1$ into the queue.

Each time we take the smallest super ugly number $x$ from the queue, multiply $x$ by each number in the array `primes`, and put the product into the queue. Repeat the above operation $n$ times to get the $n$th super ugly number.

Since the problem guarantees that the $n$th super ugly number is within the range of a 32-bit signed integer, before we put the product into the queue, we can first check whether the product exceeds $2^{31} - 1$. If it does, there is no need to put the product into the queue. In addition, the Euler sieve can be used for optimization.

The time complexity is $O(n \times m \times \log (n \times m))$, and the space complexity is $O(n \times m)$. Where $m$ and $n$ are the length of the array `primes` and the given integer $n$ respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        x = 0
        mx = (1 << 31) - 1
        for _ in range(n):
            x = heappop(q)
            for k in primes:
                if x <= mx // k:
                    heappush(q, k * x)
                if x % k == 0:
                    break
        return x
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming + Multi-pointer Heap

<!-- thinking:start -->

> **Thinking**
>
> Method 1 fans each ugly number across every prime and the heap grows large. Keep one pointer per prime: the heap top is the next candidate; after writing it, push that prime's next multiple. The heap stays $O(m)$ and the time is $O(n\log m)$.

<!-- thinking:end -->

Store the first $n$ super ugly numbers in $ugly[1..n]$, and keep a min-heap. Each heap entry belongs to one prime $p$ and records the next candidate $p \times ugly[\textit{index}]$.

Initialize $ugly[1] = 1$ and push $(p, p, 2)$ for every prime. Repeatedly pop the heap minimum into $ugly$, then advance that prime's pointer and push it back. Each prime keeps a single pointer, so we do not expand every generated ugly number against the whole prime list.

The time complexity is $O(n \times \log m)$, and the space complexity is $O(n + m)$, where $m$ is the length of $\textit{primes}$.

<!-- solution:end -->

<!-- problem:end -->
