---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0254.Factor%20Combinations/README_EN.md
tags:
    - Backtracking
---

<!-- problem:start -->

# [254. Factor Combinations 🔒](https://leetcode.com/problems/factor-combinations)

## Description

<!-- description:start -->

<p>Numbers can be regarded as the product of their factors.</p>

<ul>
	<li>For example, <code>8 = 2 x 2 x 2 = 2 x 4</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>all possible combinations of its factors</em>. You may return the answer in <strong>any order</strong>.</p>

<p><strong>Note</strong> that the factors should be in the range <code>[2, n - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> [[2,6],[3,4],[2,2,3]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 37
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, i):
            if t:
                ans.append(t + [n])
            j = i
            while j * j <= n:
                if n % j == 0:
                    t.append(j)
                    dfs(n // j, j)
                    t.pop()
                j += 1

        t = []
        ans = []
        dfs(n, 2)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
