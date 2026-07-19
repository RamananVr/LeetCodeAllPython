---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3881.Direction%20Assignments%20with%20Exactly%20K%20Visible%20People/README_EN.md
rating: 1760
source: Biweekly Contest 179 Q2
tags:
    - Math
    - Combinatorics
---

<!-- problem:start -->

# [3881. Direction Assignments with Exactly K Visible People](https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people)

## Description

<!-- description:start -->

<p>You are given three integers <code>n</code>, <code>pos</code>, and <code>k</code>.</p>

<p>There are <code>n</code> people standing in a line indexed from 0 to <code>n - 1</code>. Each person <strong>independently</strong> chooses a direction:</p>

<ul>
	<li><code>&#39;L&#39;</code>: <strong>visible</strong> only to people on their <strong>right</strong></li>
	<li><code>&#39;R&#39;</code>: <strong>visible</strong> only to people on their <strong>left</strong></li>
</ul>
A person at index <code>pos</code> sees others as follows:

<ul>
	<li>A person <code>i &lt; pos</code> is visible if and only if they choose <code>&#39;L&#39;</code>.</li>
	<li>A person <code>i &gt; pos</code> is visible if and only if they choose <code>&#39;R&#39;</code>.</li>
</ul>

<p>Return the number of possible direction assignments such that the person at index <code>pos</code> sees <strong>exactly</strong> <code>k</code> people.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, pos = 1, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>Index 0 is to the left of <code>pos = 1</code>, and index 2 is to the right of <code>pos = 1</code>.</li>
	<li>To see <code>k = 0</code> people, index 0 must choose <code>&#39;R&#39;</code> and index 2 must choose <code>&#39;L&#39;</code>, keeping both invisible.</li>
	<li>The person at index 1 can choose <code>&#39;L&#39;</code> or <code>&#39;R&#39;</code> since it does not affect the count. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, pos = 2, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Index 0 and index 1 are left of <code>pos = 2</code>, and there is no index to the right.</li>
	<li>To see <code>k = 1</code> person, exactly one of index 0 or index 1 must choose <code>&#39;L&#39;</code>, and the other must choose <code>&#39;R&#39;</code>.</li>
	<li>There are 2 ways to choose which index is visible from the left.</li>
	<li>The person at index 2 can choose <code>&#39;L&#39;</code> or <code>&#39;R&#39;</code> since it does not affect the count. Thus, the answer is <code>2 + 2 = 4</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1, pos = 0, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There are no indices to the left or right of <code>pos = 0</code>.</li>
	<li>To see <code>k = 0</code> people, no additional condition is required.</li>
	<li>The person at index 0 can choose <code>&#39;L&#39;</code> or <code>&#39;R&#39;</code>. Thus, the answer is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= pos, k &lt;= n - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Combinatorics + Enumeration

There are $\textit{pos}$ people to the left of position $\textit{pos}$, and $n - \textit{pos} - 1$ people to the right.

We enumerate the number of visible people on the left, $a$, so the number of visible people on the right is $b = k - a$. If both $a$ and $b$ are valid, the answer increases by $2 \cdot \binom{\textit{pos}}{a} \cdot \binom{n - \textit{pos} - 1}{b}$. The factor of $2$ comes from the fact that the person at index $\textit{pos}$ can face either 'L' or 'R'.

For the binomial coefficient $\binom{n}{k}$, we can precompute factorials and modular inverses for fast calculation.

The time complexity is $O(n)$, where $n$ is the input integer $n$. The space complexity is $O(n)$ for storing factorials and modular inverses.

<!-- tabs:start -->

#### Python3

```python
N = 100001
MOD = 10**9 + 7
f = [1] * N
g = [1] * N
for i in range(1, N):
    f[i] = f[i - 1] * i % MOD
    g[i] = pow(f[i], MOD - 2, MOD)

def comb(n, k):
    return f[n] * g[k] * g[n - k] % MOD

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        l, r = pos, n - pos - 1
        ans = 0
        for a in range(min(k, l) + 1):
            b = k - a
            if b <= r:
                ans += 2 * comb(l, a) * comb(r, b)
                ans %= MOD
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
