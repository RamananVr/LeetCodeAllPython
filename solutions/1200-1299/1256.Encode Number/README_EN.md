---
comments: true
difficulty: Medium
rating: 1561
source: Biweekly Contest 13 Q1
tags:
    - Bit Manipulation
    - Math
    - String
---

<!-- problem:start -->

# [1256. Encode Number 🔒](https://leetcode.com/problems/encode-number)

## Description

<!-- description:start -->

<p>Given a non-negative integer <code>num</code>, Return its <em>encoding</em> string.</p>

<p>The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:</p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1256.Encode%20Number/images/encode_number.png" style="width: 164px; height: 360px;" /></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 23
<strong>Output:</strong> &quot;1000&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 107
<strong>Output:</strong> &quot;101100&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10^9</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bit Manipulation

<!-- thinking:start -->

> **Thinking**
>
> The table is $0,1,00,01,\ldots$, i.e. all binary strings in order. The bits of $num+1$ without the leading $1$ are exactly the $num$-th such string. $num$ reaches $10^9$, so we cannot list them; one bit trick suffices.

<!-- thinking:end -->

We add one to $num$, then convert it to a binary string and remove the highest bit $1$.

The time complexity is $O(\log n)$, and the space complexity is $O(\log n)$. Where $n$ is the size of $num$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
