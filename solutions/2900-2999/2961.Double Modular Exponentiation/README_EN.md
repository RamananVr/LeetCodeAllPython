---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2961.Double%20Modular%20Exponentiation/README_EN.md
rating: 1450
source: Weekly Contest 375 Q2
tags:
    - Array
    - Math
    - Simulation
---

<!-- problem:start -->

# [2961. Double Modular Exponentiation](https://leetcode.com/problems/double-modular-exponentiation)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> 2D array <code>variables</code> where <code>variables[i] = [a<sub>i</sub>, b<sub>i</sub>, c<sub>i,</sub> m<sub>i</sub>]</code>, and an integer <code>target</code>.</p>

<p>An index <code>i</code> is <strong>good</strong> if the following formula holds:</p>

<ul>
	<li><code>0 &lt;= i &lt; variables.length</code></li>
	<li><code>((a<sub>i</sub><sup>b<sub>i</sub></sup> % 10)<sup>c<sub>i</sub></sup>) % m<sub>i</sub> == target</code></li>
</ul>

<p>Return <em>an array consisting of <strong>good</strong> indices in <strong>any order</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
<strong>Output:</strong> [0,2]
<strong>Explanation:</strong> For each index i in the variables array:
1) For the index 0, variables[0] = [2,3,3,10], (2<sup>3</sup> % 10)<sup>3</sup> % 10 = 2.
2) For the index 1, variables[1] = [3,3,3,1], (3<sup>3</sup> % 10)<sup>3</sup> % 1 = 0.
3) For the index 2, variables[2] = [6,1,1,4], (6<sup>1</sup> % 10)<sup>1</sup> % 4 = 2.
Therefore we return [0,2] as the answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> variables = [[39,3,1000,1000]], target = 17
<strong>Output:</strong> []
<strong>Explanation:</strong> For each index i in the variables array:
1) For the index 0, variables[0] = [39,3,1000,1000], (39<sup>3</sup> % 10)<sup>1000</sup> % 1000 = 1.
Therefore we return [] as the answer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= variables.length &lt;= 100</code></li>
	<li><code>variables[i] == [a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, m<sub>i</sub>]</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, m<sub>i</sub> &lt;= 10<sup>3</sup></code></li>
	<li><code><font face="monospace">0 &lt;= target &lt;= 10<sup>3</sup></font></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation + Fast Power

We can directly simulate according to the problem description. For the power operation modulo, we can use the fast power method to speed up the calculation.

The time complexity is $O(n \times \log M)$, where $n$ is the length of the array $variables$; and $M$ is the maximum value in $b_i$ and $c_i$, in this problem $M \le 10^3$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [
            i
            for i, (a, b, c, m) in enumerate(variables)
            if pow(pow(a, b, 10), c, m) == target
        ]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
