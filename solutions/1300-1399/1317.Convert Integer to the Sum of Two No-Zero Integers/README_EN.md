---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1317.Convert%20Integer%20to%20the%20Sum%20of%20Two%20No-Zero%20Integers/README_EN.md
rating: 1277
source: Weekly Contest 171 Q1
tags:
    - Math
---

<!-- problem:start -->

# [1317. Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers)

## Description

<!-- description:start -->

<p><strong>No-Zero integer</strong> is a positive integer that <strong>does not contain any <code>0</code></strong> in its decimal representation.</p>

<p>Given an integer <code>n</code>, return <em>a list of two integers</em> <code>[a, b]</code> <em>where</em>:</p>

<ul>
	<li><code>a</code> and <code>b</code> are <strong>No-Zero integers</strong>.</li>
	<li><code>a + b = n</code></li>
</ul>

<p>The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [1,1]
<strong>Explanation:</strong> Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> [2,9]
<strong>Explanation:</strong> Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Direct Enumeration

Starting from $1$, we enumerate $a$, then $b = n - a$. For each $a$ and $b$, we convert them to strings and concatenate them, then check if they contain the character '0'. If they do not contain '0', we have found the answer and return $[a, b]$.

The time complexity is $O(n \times \log n)$, where $n$ is the integer given in the problem. The space complexity is $O(\log n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in count(1):
            b = n - a
            if "0" not in f"{a}{b}":
                return [a, b]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Direct Enumeration (Alternative Approach)

In Solution 1, we converted $a$ and $b$ into strings and concatenated them, then checked if they contained the character '0'. Here, we can use a function $f(x)$ to check whether $x$ contains the character '0', and then directly enumerate $a$, checking whether both $a$ and $b = n - a$ do not contain the character '0'. If they do not, we have found the answer and return $[a, b]$.

The time complexity is $O(n \times \log n)$, where $n$ is the integer given in the problem. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def f(x: int) -> bool:
            while x:
                if x % 10 == 0:
                    return False
                x //= 10
            return True

        for a in count(1):
            b = n - a
            if f(a) and f(b):
                return [a, b]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
