---
comments: true
difficulty: Hard
rating: 2429
source: Weekly Contest 257 Q4
tags:
    - Union Find
    - Array
    - Math
    - Greatest Common Divisor
    - Number Theory
    - Sorting
    - Prime Factorization
    - Euclidean Algorithm
---

<!-- problem:start -->

# [1998. GCD Sort of an Array](https://leetcode.com/problems/gcd-sort-of-an-array)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>, and you can perform the following operation <strong>any</strong> number of times on <code>nums</code>:</p>

<ul>
	<li>Swap the positions of two elements <code>nums[i]</code> and <code>nums[j]</code> if <code>gcd(nums[i], nums[j]) &gt; 1</code> where <code>gcd(nums[i], nums[j])</code> is the <strong>greatest common divisor</strong> of <code>nums[i]</code> and <code>nums[j]</code>.</li>
</ul>

<p>Return <code>true</code> <em>if it is possible to sort </em><code>nums</code><em> in <strong>non-decreasing</strong> order using the above swap method, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,21,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can sort [7,21,3] by performing the following operations:
- Swap 7 and 21 because gcd(7,21) = 7. nums = [<u><strong>21</strong></u>,<u><strong>7</strong></u>,3]
- Swap 21 and 3 because gcd(21,3) = 3. nums = [<u><strong>3</strong></u>,7,<u><strong>21</strong></u>]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,2,6,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to sort the array because 5 cannot be swapped with any other element.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,5,9,3,15]
<strong>Output:</strong> true
We can sort [10,5,9,3,15] by performing the following operations:
- Swap 10 and 15 because gcd(10,15) = 5. nums = [<u><strong>15</strong></u>,5,9,3,<u><strong>10</strong></u>]
- Swap 15 and 3 because gcd(15,3) = 3. nums = [<u><strong>3</strong></u>,5,9,<u><strong>15</strong></u>,10]
- Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,<u><strong>10</strong></u>,<u><strong>15</strong></u>]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Two numbers may be swapped if their gcd exceeds $1$; we ask whether the array can become sorted. Numbers that share a prime factor lie in one swap component. Pairwise gcd is too slow for values up to $10^5$.
>
> Sieve each value's primes and union the value with those primes. After sorting, a mismatch whose two numbers are in different components cannot be swapped into place.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = 10**5 + 10
        p = list(range(n))
        f = defaultdict(list)
        mx = max(nums)
        for i in range(2, mx + 1):
            if f[i]:
                continue
            for j in range(i, mx + 1, i):
                f[j].append(i)

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i in nums:
            for j in f[i]:
                p[find(i)] = find(j)

        s = sorted(nums)
        for i, num in enumerate(nums):
            if s[i] != num and find(num) != find(s[i]):
                return False
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
