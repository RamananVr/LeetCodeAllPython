---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1134.Armstrong%20Number/README_EN.md
rating: 1231
source: Biweekly Contest 5 Q2
tags:
    - Math
---

<!-- problem:start -->

# [1134. Armstrong Number 🔒](https://leetcode.com/problems/armstrong-number)

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <code>true</code> <em>if and only if it is an <strong>Armstrong number</strong></em>.</p>

<p>The <code>k</code>-digit number <code>n</code> is an Armstrong number if and only if the <code>k<sup>th</sup></code> power of each digit sums to <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 153
<strong>Output:</strong> true
<strong>Explanation:</strong> 153 is a 3-digit number, and 153 = 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 123
<strong>Output:</strong> false
<strong>Explanation:</strong> 123 is a 3-digit number, and 123 != 1<sup>3</sup> + 2<sup>3</sup> + 3<sup>3</sup> = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We can first calculate the number of digits $k$, then calculate the sum $s$ of the $k$th power of each digit, and finally check whether $s$ equals $n$.

The time complexity is $O(\log n)$, and the space complexity is $O(\log n)$. Here, $n$ is the given number.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        s, x = 0, n
        while x:
            s += (x % 10) ** k
            x //= 10
        return s == n
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
