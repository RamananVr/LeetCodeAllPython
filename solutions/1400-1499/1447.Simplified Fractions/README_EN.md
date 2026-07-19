---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1447.Simplified%20Fractions/README_EN.md
rating: 1268
source: Biweekly Contest 26 Q2
tags:
    - Math
    - String
    - Number Theory
---

<!-- problem:start -->

# [1447. Simplified Fractions](https://leetcode.com/problems/simplified-fractions)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <em>a list of all <strong>simplified</strong> fractions between </em><code>0</code><em> and </em><code>1</code><em> (exclusive) such that the denominator is less-than-or-equal-to </em><code>n</code>. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [&quot;1/2&quot;]
<strong>Explanation:</strong> &quot;1/2&quot; is the only unique fraction with a denominator less-than-or-equal-to 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [&quot;1/2&quot;,&quot;1/3&quot;,&quot;2/3&quot;]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> [&quot;1/2&quot;,&quot;1/3&quot;,&quot;1/4&quot;,&quot;2/3&quot;,&quot;3/4&quot;]
<strong>Explanation:</strong> &quot;2/4&quot; is not a simplified fraction because it can be simplified to &quot;1/2&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [
            f'{i}/{j}'
            for i in range(1, n)
            for j in range(i + 1, n + 1)
            if gcd(i, j) == 1
        ]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
