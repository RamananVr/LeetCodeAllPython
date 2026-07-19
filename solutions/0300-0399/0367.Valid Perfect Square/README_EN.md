---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0367.Valid%20Perfect%20Square/README_EN.md
tags:
    - Math
    - Binary Search
---

<!-- problem:start -->

# [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square)

## Description

<!-- description:start -->

<p>Given a positive integer num, return <code>true</code> <em>if</em> <code>num</code> <em>is a perfect square or</em> <code>false</code> <em>otherwise</em>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer. In other words, it is the product of some integer with itself.</p>

<p>You must not use any built-in library function, such as <code>sqrt</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 16
<strong>Output:</strong> true
<strong>Explanation:</strong> We return true because 4 * 4 = 16 and 4 is an integer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

We can use binary search to solve this problem. Define the left boundary $l = 1$ and the right boundary $r = num$ of the binary search, then find the smallest integer $x$ that satisfies $x^2 \geq num$ in the range $[l, r]$. Finally, if $x^2 = num$, then $num$ is a perfect square.

The time complexity is $O(\log n)$, where $n$ is the given number. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = bisect_left(range(1, num + 1), num, key=lambda x: x * x) + 1
        return l * l == num
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Mathematics

Since $1 + 3 + 5 + \cdots + (2n - 1) = n^2$, we can gradually subtract $1, 3, 5, \cdots$ from $num$. If $num$ finally equals $0$, then $num$ is a perfect square.

The time complexity is $O(\sqrt n)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
