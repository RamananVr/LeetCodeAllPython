---
comments: true
difficulty: Medium
tags:
    - String
    - Dynamic Programming
    - Backtracking
    - Parentheses
---

<!-- problem:start -->

# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

## Description

<!-- description:start -->

<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS + Pruning

<!-- thinking:start -->

> **Thinking**
>
> The first idea is to enumerate every string of length $2n$ and keep the valid ones. $n \le 8$ gives $2^{16}$ candidates, so it would pass, but most prefixes are already illegal.
>
> The bottleneck is generate-then-check: once a prefix has more `)` than `(`, or either count exceeds $n$, no suffix can save it.
>
> A valid prefix only needs the two counts $l$ and $r$: keep $l \ge r$ and neither above $n$. When $l=r=n$, record the string.
>
> DFS therefore tries appending `(` or `)` and prunes on those three inequalities. The search tree is much smaller than full enumeration; extra space is just the current string, $O(n)$.

<!-- thinking:end -->

The range of $n$ in the problem is $[1, 8]$, so we can directly solve this problem through "brute force search + pruning".

We design a function $dfs(l, r, t)$, where $l$ and $r$ represent the number of left and right brackets respectively, and $t$ represents the current bracket sequence. Then we can get the following recursive structure:

- If $l \gt n$ or $r \gt n$ or $l \lt r$, then the current bracket combination $t$ is invalid, return directly;
- If $l = n$ and $r = n$, then the current bracket combination $t$ is valid, add it to the answer array `ans`, and return directly;
- We can choose to add a left bracket, and recursively execute `dfs(l + 1, r, t + "(")`;
- We can also choose to add a right bracket, and recursively execute `dfs(l, r + 1, t + ")")`.

The time complexity is $O(2^{n\times 2} \times n)$, and the space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l: int, r: int, t: str):
            if l > n or r > n or l < r:
                return
            if l == n and r == n:
                ans.append(t)
                return
            dfs(l + 1, r, t + "(")
            dfs(l, r + 1, t + ")")

        ans = []
        dfs(0, 0, "")
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
