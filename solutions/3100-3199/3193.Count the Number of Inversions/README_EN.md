---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3193.Count%20the%20Number%20of%20Inversions/README_EN.md
rating: 2266
source: Biweekly Contest 133 Q4
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3193. Count the Number of Inversions](https://leetcode.com/problems/count-the-number-of-inversions)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code> and a 2D array <code>requirements</code>, where <code>requirements[i] = [end<sub>i</sub>, cnt<sub>i</sub>]</code> represents the end index and the <strong>inversion</strong> count of each requirement.</p>

<p>A pair of indices <code>(i, j)</code> from an integer array <code>nums</code> is called an <strong>inversion</strong> if:</p>

<ul>
	<li><code>i &lt; j</code> and <code>nums[i] &gt; nums[j]</code></li>
</ul>

<p>Return the number of <span data-keyword="permutation">permutations</span> <code>perm</code> of <code>[0, 1, 2, ..., n - 1]</code> such that for <strong>all</strong> <code>requirements[i]</code>, <code>perm[0..end<sub>i</sub>]</code> has exactly <code>cnt<sub>i</sub></code> inversions.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, requirements = [[2,2],[0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The two permutations are:</p>

<ul>
	<li><code>[2, 0, 1]</code>

    <ul>
    	<li>Prefix <code>[2, 0, 1]</code> has inversions <code>(0, 1)</code> and <code>(0, 2)</code>.</li>
    	<li>Prefix <code>[2]</code> has 0 inversions.</li>
    </ul>
    </li>
    <li><code>[1, 2, 0]</code>
    <ul>
    	<li>Prefix <code>[1, 2, 0]</code> has inversions <code>(0, 2)</code> and <code>(1, 2)</code>.</li>
    	<li>Prefix <code>[1]</code> has 0 inversions.</li>
    </ul>
    </li>

</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, requirements = [[2,2],[1,1],[0,0]]</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>The only satisfying permutation is <code>[2, 0, 1]</code>:</p>

<ul>
	<li>Prefix <code>[2, 0, 1]</code> has inversions <code>(0, 1)</code> and <code>(0, 2)</code>.</li>
	<li>Prefix <code>[2, 0]</code> has an inversion <code>(0, 1)</code>.</li>
	<li>Prefix <code>[2]</code> has 0 inversions.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, requirements = [[0,0],[1,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only satisfying permutation is <code>[0, 1]</code>:</p>

<ul>
	<li>Prefix <code>[0]</code> has 0 inversions.</li>
	<li>Prefix <code>[0, 1]</code> has no inversions.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 300</code></li>
	<li><code>1 &lt;= requirements.length &lt;= n</code></li>
	<li><code>requirements[i] = [end<sub>i</sub>, cnt<sub>i</sub>]</code></li>
	<li><code>0 &lt;= end<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>0 &lt;= cnt<sub>i</sub> &lt;= 400</code></li>
	<li>The input is generated such that there is at least one <code>i</code> such that <code>end<sub>i</sub> == n - 1</code>.</li>
	<li>The input is generated such that all <code>end<sub>i</sub></code> are unique.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the number of permutations of $[0..i]$ with $j$ inversions. Consider the relationship between the number $a_i$ at index $i$ and the previous $i$ numbers. If $a_i$ is smaller than $k$ of the previous numbers, then each of these $k$ numbers forms an inversion pair with $a_i$, contributing to $k$ inversions. Therefore, we can derive the state transition equation:

$$
f[i][j] = \sum_{k=0}^{\min(i, j)} f[i-1][j-k]
$$

Since the problem requires the number of inversions in $[0..\textit{end}_i]$ to be $\textit{cnt}_i$, when we calculate for $i = \textit{end}_i$, we only need to compute $f[i][\textit{cnt}_i]$. The rest of $f[i][..]$ will be $0$.

The time complexity is $O(n \times m \times \min(n, m))$, and the space complexity is $O(n \times m)$. Here, $m$ is the maximum number of inversions, and in this problem, $m \le 400$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        req = [-1] * n
        for end, cnt in requirements:
            req[end] = cnt
        if req[0] > 0:
            return 0
        req[0] = 0
        mod = 10**9 + 7
        m = max(req)
        f = [[0] * (m + 1) for _ in range(n)]
        f[0][0] = 1
        for i in range(1, n):
            l, r = 0, m
            if req[i] >= 0:
                l = r = req[i]
            for j in range(l, r + 1):
                for k in range(min(i, j) + 1):
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
        return f[n - 1][req[n - 1]]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
