---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2485.Find%20the%20Pivot%20Integer/README_EN.md
rating: 1207
source: Weekly Contest 321 Q1
tags:
    - Math
    - Prefix Sum
---

<!-- problem:start -->

# [2485. Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer)

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, find the <strong>pivot integer</strong> <code>x</code> such that:</p>

<ul>
	<li>The sum of all elements between <code>1</code> and <code>x</code> inclusively equals the sum of all elements between <code>x</code> and <code>n</code> inclusively.</li>
</ul>

<p>Return <em>the pivot integer </em><code>x</code>. If no such integer exists, return <code>-1</code>. It is guaranteed that there will be at most one pivot index for the given input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 is the pivot integer since: 1 = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proved that no such integer exist.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration

We can directly enumerate $x$ in the range of $[1,..n]$, and check whether the following equation holds. If it holds, then $x$ is the pivot integer, and we can directly return $x$.

$$
(1 + x) \times x = (x + n) \times (n - x + 1)
$$

The time complexity is $O(n)$, where $n$ is the given positive integer $n$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(1, n + 1):
            if (1 + x) * x == (x + n) * (n - x + 1):
                return x
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Mathematics

We can transform the above equation to get:

$$
n \times (n + 1) = 2 \times x^2
$$

That is:

$$
x = \sqrt{\frac{n \times (n + 1)}{2}}
$$

If $x$ is an integer, then $x$ is the pivot integer, otherwise there is no pivot integer.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        y = n * (n + 1) // 2
        x = int(sqrt(y))
        return x if x * x == y else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
