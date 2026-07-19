---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1735.Count%20Ways%20to%20Make%20Array%20With%20Product/README_EN.md
rating: 2499
source: Biweekly Contest 44 Q4
tags:
    - Array
    - Math
    - Dynamic Programming
    - Combinatorics
    - Number Theory
---

<!-- problem:start -->

# [1735. Count Ways to Make Array With Product](https://leetcode.com/problems/count-ways-to-make-array-with-product)

## Description

<!-- description:start -->

<p>You are given a 2D integer array, <code>queries</code>. For each <code>queries[i]</code>, where <code>queries[i] = [n<sub>i</sub>, k<sub>i</sub>]</code>, find the number of different ways you can place positive integers into an array of size <code>n<sub>i</sub></code> such that the product of the integers is <code>k<sub>i</sub></code>. As the number of ways may be too large, the answer to the <code>i<sup>th</sup></code> query is the number of ways <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>Return <em>an integer array </em><code>answer</code><em> where </em><code>answer.length == queries.length</code><em>, and </em><code>answer[i]</code><em> is the answer to the </em><code>i<sup>th</sup></code><em> query.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> queries = [[2,6],[5,1],[73,660]]
<strong>Output:</strong> [4,1,50734910]
<strong>Explanation:</strong>&nbsp;Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 10<sup>9</sup> + 7 = 50734910.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
<strong>Output:</strong> [1,2,3,10,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup> </code></li>
	<li><code>1 &lt;= n<sub>i</sub>, k<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prime Factorization + Combinatorial Mathematics

We can perform prime factorization on $k$, i.e., $k = p_1^{x_1} \times p_2^{x_2} \times \cdots \times p_m^{x_m}$, where $p_i$ is a prime number, and $x_i$ is the exponent of $p_i$. The problem is equivalent to: placing $x_1$ $p_1$s, $x_2$ $p_2$s, $\cdots$, $x_m$ $p_m$s into $n$ positions respectively, where a single position can be empty. The question is how many schemes are there.

According to combinatorial mathematics, there are two cases when we put $x$ balls into $n$ boxes:

If the box cannot be empty, the number of schemes is $C_{x-1}^{n-1}$. This is using the partition method, i.e., there are a total of $x$ balls, and we insert $n-1$ partitions at $x-1$ positions, thereby dividing the $x$ balls into $n$ groups.

If the box can be empty, we can add $n$ virtual balls, and then use the partition method, i.e., there are a total of $x+n$ balls, and we insert $n-1$ partitions at $x+n-1$ positions, thereby dividing the actual $x$ balls into $n$ groups and allowing the box to be empty. Therefore, the number of schemes is $C_{x+n-1}^{n-1}$.

Therefore, for each query $queries[i]$, we can first perform prime factorization on $k$ to get the exponents $x_1, x_2, \cdots, x_m$, then calculate $C_{x_1+n-1}^{n-1}, C_{x_2+n-1}^{n-1}, \cdots, C_{x_m+n-1}^{n-1}$, and finally multiply all the scheme numbers.

So, the problem is transformed into how to quickly calculate $C_m^n$. According to the formula $C_m^n = \frac{m!}{n!(m-n)!}$, we can pre-process $m!$, and then use the inverse element to quickly calculate $C_m^n$.

The time complexity is $O(K \times \log \log K + N + m \times \log K)$, and the space complexity is $O(N)$.

<!-- tabs:start -->

#### Python3

```python
N = 10020
MOD = 10**9 + 7
f = [1] * N
g = [1] * N
p = defaultdict(list)
for i in range(1, N):
    f[i] = f[i - 1] * i % MOD
    g[i] = pow(f[i], MOD - 2, MOD)
    x = i
    j = 2
    while j <= x // j:
        if x % j == 0:
            cnt = 0
            while x % j == 0:
                cnt += 1
                x //= j
            p[i].append(cnt)
        j += 1
    if x > 1:
        p[i].append(1)

def comb(n, k):
    return f[n] * g[k] * g[n - k] % MOD

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        ans = []
        for n, k in queries:
            t = 1
            for x in p[k]:
                t = t * comb(x + n - 1, n - 1) % MOD
            ans.append(t)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
