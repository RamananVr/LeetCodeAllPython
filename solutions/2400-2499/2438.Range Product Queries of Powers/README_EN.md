---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2438.Range%20Product%20Queries%20of%20Powers/README_EN.md
rating: 1609
source: Biweekly Contest 89 Q2
tags:
    - Bit Manipulation
    - Array
    - Prefix Sum
---

<!-- problem:start -->

# [2438. Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers)

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, there exists a <strong>0-indexed</strong> array called <code>powers</code>, composed of the <strong>minimum</strong> number of powers of <code>2</code> that sum to <code>n</code>. The array is sorted in <strong>non-decreasing</strong> order, and there is <strong>only one</strong> way to form the array.</p>

<p>You are also given a <strong>0-indexed</strong> 2D integer array <code>queries</code>, where <code>queries[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>. Each <code>queries[i]</code> represents a query where you have to find the product of all <code>powers[j]</code> with <code>left<sub>i</sub> &lt;= j &lt;= right<sub>i</sub></code>.</p>

<p>Return<em> an array </em><code>answers</code><em>, equal in length to </em><code>queries</code><em>, where </em><code>answers[i]</code><em> is the answer to the </em><code>i<sup>th</sup></code><em> query</em>. Since the answer to the <code>i<sup>th</sup></code> query may be too large, each <code>answers[i]</code> should be returned <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 15, queries = [[0,1],[2,2],[0,3]]
<strong>Output:</strong> [2,4,64]
<strong>Explanation:</strong>
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 10<sup>9</sup> + 7 yields the same answer, so [2,4,64] is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, queries = [[0,0]]
<strong>Output:</strong> [2]
<strong>Explanation:</strong>
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 10<sup>9</sup> + 7 is the same, so [2] is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt; powers.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bit Manipulation + Simulation

We can use bit manipulation (lowbit) to obtain the $\textit{powers}$ array, and then use simulation to find the answer for each query.

First, for a given positive integer $n$, we can quickly obtain the value corresponding to the lowest bit $1$ in the binary representation through $n \& -n$, which is the minimum power of $2$ factor of the current number. By repeatedly performing this operation on $n$ and subtracting this value, we can sequentially obtain all the powers of $2$ corresponding to the set bits, forming the $\textit{powers}$ array. This array is in increasing order, and its length equals the number of $1$s in the binary representation of $n$.

Next, we need to process each query. For the current query $(l, r)$, we need to calculate

$$
\textit{answers}[i] = \prod_{j=l}^{r} \textit{powers}[j]
$$

where $\textit{answers}[i]$ is the answer to the $i$-th query. Since the query results can be very large, we need to take modulo $10^9 + 7$ for each answer.

The time complexity is $O(m \times \log n)$, where $m$ is the length of the array $\textit{queries}$. Ignoring the space consumption of the answer, the space complexity is $O(\log n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        while n:
            x = n & -n
            powers.append(x)
            n -= x
        mod = 10**9 + 7
        ans = []
        for l, r in queries:
            x = 1
            for i in range(l, r + 1):
                x = x * powers[i] % mod
            ans.append(x)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
