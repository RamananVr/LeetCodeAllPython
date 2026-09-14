---
comments: true
difficulty: Medium
tags:
    - Greedy
    - Math
---

<!-- problem:start -->

# [670. Maximum Swap](https://leetcode.com/problems/maximum-swap)

## Description

<!-- description:start -->

<p>You are given an integer <code>num</code>. You can swap two digits at most once to get the maximum valued number.</p>

<p>Return <em>the maximum valued number you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 2736
<strong>Output:</strong> 7236
<strong>Explanation:</strong> Swap the number 2 and the number 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 9973
<strong>Output:</strong> 9973
<strong>Explanation:</strong> No swap.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy Algorithm

<!-- thinking:start -->

> **Thinking**
>
> Swap at most two digits to maximize the number. Trying every pair is unnecessary.
>
> From the right, record the index of the largest digit to the right (inclusive). From the left, swap at the first $s[i]<s[d[i]]$. That raises the highest possible place.

<!-- thinking:end -->

First, we convert the number into a string $s$. Then, we traverse the string $s$ from right to left, using an array or hash table $d$ to record the position of the maximum number to the right of each number (it can be the position of the number itself).

Next, we traverse $d$ from left to right. If $s[i] < s[d[i]]$, we swap them and exit the traversal process.

Finally, we convert the string $s$ back into a number, which is the answer.

The time complexity is $O(\log M)$, and the space complexity is $O(\log M)$. Here, $M$ is the range of the number $num$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        d = list(range(n))
        for i in range(n - 2, -1, -1):
            if s[i] <= s[d[i + 1]]:
                d[i] = d[i + 1]
        for i, j in enumerate(d):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
                break
        return int(''.join(s))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Space Optimized Greedy

<!-- thinking:start -->

> **Thinking**
>
> Method 1 stores a right-max index array. One right-to-left scan can keep the best seen digit and the leftmost profitable swap, without the extra array.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
