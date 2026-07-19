---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3750.Minimum%20Number%20of%20Flips%20to%20Reverse%20Binary%20String/README_EN.md
rating: 1288
source: Biweekly Contest 170 Q1
tags:
    - Bit Manipulation
    - Math
    - Two Pointers
    - String
---

<!-- problem:start -->

# [3750. Minimum Number of Flips to Reverse Binary String](https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string)

## Description

<!-- description:start -->

<p>You are given a <strong>positive</strong> integer <code>n</code>.</p>

<p>Let <code>s</code> be the <strong>binary representation</strong> of <code>n</code> without leading zeros.</p>

<p>The <strong>reverse</strong> of a binary string <code>s</code> is obtained by writing the characters of <code>s</code> in the opposite order.</p>

<p>You may flip any bit in <code>s</code> (change <code>0 &rarr; 1</code> or <code>1 &rarr; 0</code>). Each flip affects <strong>exactly</strong> one bit.</p>

<p>Return the <strong>minimum</strong> number of flips required to make <code>s</code> equal to the reverse of its original form.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 7 is <code>&quot;111&quot;</code>. Its reverse is also <code>&quot;111&quot;</code>, which is the same. Hence, no flips are needed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 10 is <code>&quot;1010&quot;</code>. Its reverse is <code>&quot;0101&quot;</code>. All four bits must be flipped to make them equal. Thus, the minimum number of flips required is 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We first convert the integer $n$ into a binary string $s$. Then we use two pointers to traverse from both ends of the string towards the center, counting the number of positions where the characters differ, denoted as $cnt$. Since each flip can only affect one bit, the total number of flips is $cnt \times 2$.

The time complexity is $O(\log n)$ and the space complexity is $O(\log n)$, where $n$ is the input integer.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        m = len(s)
        return sum(s[i] != s[m - i - 1] for i in range(m // 2)) * 2
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
