---
comments: true
difficulty: Easy
tags:
    - Bit Manipulation
    - Backtracking
---

<!-- problem:start -->

# [401. Binary Watch](https://leetcode.com/problems/binary-watch)

## Description

<!-- description:start -->

<p>A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent&nbsp;the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.</p>

<ul>
	<li>For example, the below binary watch reads <code>&quot;4:51&quot;</code>.</li>
</ul>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0401.Binary%20Watch/images/binarywatch.jpg" style="width: 500px; height: 500px;" /></p>

<p>Given an integer <code>turnedOn</code> which represents the number of LEDs that are currently on (ignoring the PM), return <em>all possible times the watch could represent</em>. You may return the answer in <strong>any order</strong>.</p>

<p>The hour must not contain a leading zero.</p>

<ul>
	<li>For example, <code>&quot;01:00&quot;</code> is not valid. It should be <code>&quot;1:00&quot;</code>.</li>
</ul>

<p>The minute must&nbsp;consist of two digits and may contain a leading zero.</p>

<ul>
	<li>For example, <code>&quot;10:2&quot;</code> is not valid. It should be <code>&quot;10:02&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> turnedOn = 1
<strong>Output:</strong> ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> turnedOn = 9
<strong>Output:</strong> []
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= turnedOn &lt;= 10</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumerate Combinations

<!-- thinking:start -->

> **Thinking**
>
> Hours lie in $[0,12)$ and minutes in $[0,60)$, so only $720$ readings exist. The number of lit LEDs is the total number of $1$-bits, so we enumerate each pair $(i,j)$ and count bits.
>
> The search space is constant. Enumerating valid clock readings and matching $\textit{turnedOn}$ is shorter than choosing LED subsets and then checking that the time is legal.

<!-- thinking:end -->

The problem can be converted to finding all possible combinations of $i \in [0, 12)$ and $j \in [0, 60)$.

A valid combination must satisfy the condition that the number of 1s in the binary representation of $i$ plus the number of 1s in the binary representation of $j$ equals $\textit{turnedOn}$.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [
            '{:d}:{:02d}'.format(i, j)
            for i in range(12)
            for j in range(60)
            if (bin(i) + bin(j)).count('1') == turnedOn
        ]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Binary Enumeration

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 enumerates legal hours and minutes. The ten LEDs are also a mask in $[0,2^{10})$: the high $4$ bits are the hour and the low $6$ bits the minute. Keep those with $h<12$, $m<60$, and popcount equal to $\textit{turnedOn}$.
>
> A single loop mirrors the hardware layout; the asymptotic cost stays $O(1)$.

<!-- thinking:end -->

We can use $10$ binary bits to represent the watch, where the first $4$ bits represent hours and the last $6$ bits represent minutes. Enumerate each number in $[0, 2^{10})$, check if the number of 1s in its binary representation equals $\textit{turnedOn}$, and if so, convert it to time format and add it to the answer.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(1 << 10):
            h, m = i >> 6, i & 0b111111
            if h < 12 and m < 60 and i.bit_count() == turnedOn:
                ans.append('{:d}:{:02d}'.format(h, m))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
