---
comments: true
difficulty: Medium
tags:
    - Bit Manipulation
    - Array
    - Dynamic Programming
    - Backtracking
    - Bitmask
---

<!-- problem:start -->

# [526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement)

## Description

<!-- description:start -->

<p>Suppose you have <code>n</code> integers labeled <code>1</code> through <code>n</code>. A permutation of those <code>n</code> integers <code>perm</code> (<strong>1-indexed</strong>) is considered a <strong>beautiful arrangement</strong> if for every <code>i</code> (<code>1 &lt;= i &lt;= n</code>), <strong>either</strong> of the following is true:</p>

<ul>
	<li><code>perm[i]</code> is divisible by <code>i</code>.</li>
	<li><code>i</code> is divisible by <code>perm[i]</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>the <strong>number</strong> of the <strong>beautiful arrangements</strong> that you can construct</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<b>Explanation:</b> 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Backtracking

<!-- thinking:start -->

> **Thinking**
>
> Count permutations where value $j$ at position $i$ divides or is divided by $i$. Full $15!$ search is impossible, but few values fit each position.
>
> Precompute the legal values per position, then backtrack by position while marking used numbers. Reaching $n+1$ counts one arrangement. The divisibility lists keep the search inside the feasible set.

<!-- thinking:end -->

Assign unused numbers to each position when the divisibility condition holds.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(i):
            nonlocal ans, n
            if i == n + 1:
                ans += 1
                return
            for j in match[i]:
                if not vis[j]:
                    vis[j] = True
                    dfs(i + 1)
                    vis[j] = False

        ans = 0
        vis = [False] * (n + 1)
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j % i == 0 or i % j == 0:
                    match[i].append(j)

        dfs(1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: State Compression DP

<!-- thinking:start -->

> **Thinking**
>
> Backtracking still expands a permutation tree and repeats the same unused-set at the same position. With $n \le 15$ the used set fits in $2^n$ bits.
>
> $f[i]$ is the number of ways to reach used-set $i$. The pop-count is the next position; try each unused $j$ that divides that position. $f[0]=1$ and the full mask is the answer. Each subset is filled once.

<!-- thinking:end -->

$f[i]$ is the number of ways to form the chosen-number mask $i$.

<!-- solution:end -->

<!-- problem:end -->
