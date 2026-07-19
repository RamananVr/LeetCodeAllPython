---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0481.Magical%20String/README_EN.md
tags:
    - Two Pointers
    - String
---

<!-- problem:start -->

# [481. Magical String](https://leetcode.com/problems/magical-string)

## Description

<!-- description:start -->

<p>A magical string <code>s</code> consists of only <code>&#39;1&#39;</code> and <code>&#39;2&#39;</code> and obeys the following rule:</p>

<ul>
	<li>Concatenating the sequence of lengths of its consecutive groups of identical characters <code>&#39;1&#39;</code> and <code>&#39;2&#39;</code> generates the string <code>s</code> itself.</li>
</ul>

<p>The first few elements of <code>s</code> is <code>s = &quot;1221121221221121122&hellip;&hellip;&quot;</code>. If we group the consecutive <code>1</code>&#39;s and <code>2</code>&#39;s in <code>s</code>, it will be <code>&quot;1 22 11 2 1 22 1 22 11 2 11 22 ......&quot;</code> and counting the occurrences of <code>1</code>&#39;s or <code>2</code>&#39;s in each group yields the sequence&nbsp;<code>&quot;1 2 2 1 1 2 1 2 2 1 2 2 ......&quot;</code>.</p>

<p>You can see that concatenating the occurrence sequence gives us&nbsp;<code>s</code> itself.</p>

<p>Given an integer <code>n</code>, return the number of <code>1</code>&#39;s in the first <code>n</code> number in the magical string <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first 6 elements of magical string s is &quot;122112&quot; and it contains three 1&#39;s, so return 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulate the Construction Process

According to the problem, we know that each group of numbers in the string $s$ can be obtained from the digits of the string $s$ itself.

The first two groups of numbers in string $s$ are $1$ and $22$, which are obtained from the first and second digits of string $s$, respectively. Moreover, the first group of numbers contains only $1$, the second group contains only $2$, the third group contains only $1$, and so on.

Since the first two groups of numbers are known, we initialize string $s$ as $122$, and then start constructing from the third group. The third group of numbers is obtained from the third digit of string $s$ (index $i=2$), so at this point, we point the pointer $i$ to the third digit $2$ of string $s$.

```
1 2 2
    ^
    i
```

The digit pointed by pointer $i$ is $2$, indicating that the third group of numbers will appear twice. Since the previous group of numbers is $2$, and the numbers alternate between groups, the third group of numbers is two $1$s, i.e., $11$. After construction, the pointer $i$ moves to the next position, pointing to the fourth digit $1$ of string $s$.

```
1 2 2 1 1
      ^
      i
```

At this point, the digit pointed by pointer $i$ is $1$, indicating that the fourth group of numbers will appear once. Since the previous group of numbers is $1$, and the numbers alternate between groups, the fourth group of numbers is one $2$, i.e., $2$. After construction, the pointer $i$ moves to the next position, pointing to the fifth digit $1$ of string $s$.

```
1 2 2 1 1 2
        ^
        i
```

Following this rule, we simulate the construction process sequentially until the length of string $s$ is greater than or equal to $n$.

The time complexity is $O(n)$, and the space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            pre = s[-1]
            cur = 3 - pre
            s += [cur] * s[i]
            i += 1
        return s[:n].count(1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
