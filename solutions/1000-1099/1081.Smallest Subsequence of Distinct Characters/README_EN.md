---
comments: true
difficulty: Medium
rating: 2184
source: Weekly Contest 140 Q4
tags:
    - Stack
    - Greedy
    - String
    - Monotonic Stack
---

<!-- problem:start -->

# [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the </em><span data-keyword="lexicographically-smaller-string"><em>lexicographically smallest</em></span> <span data-keyword="subsequence-string"><em>subsequence</em></span><em> of</em> <code>s</code> <em>that contains all the distinct characters of</em> <code>s</code> <em>exactly once</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bcabc&quot;
<strong>Output:</strong> &quot;abc&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbacdcbc&quot;
<strong>Output:</strong> &quot;acdb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Note:</strong> This question is the same as 316: <a href="https://leetcode.com/problems/remove-duplicate-letters/" target="_blank">https://leetcode.com/problems/remove-duplicate-letters/</a>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> We need each distinct letter once, in the smallest subsequence that preserves order. $n\le 1000$ fits a monotonic stack: a larger top that still appears later can be popped.
>
> Record the last index of every letter. Skip a letter already on the stack; otherwise pop tops that are greater and still occur later, then push.
>
> A set tracks membership. The stack order is the answer.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stk = []
        vis = set()
        for i, c in enumerate(s):
            if c in vis:
                continue
            while stk and stk[-1] > c and last[stk[-1]] > i:
                vis.remove(stk.pop())
            stk.append(c)
            vis.add(c)
        return "".join(stk)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 uses a hash set for membership. Twenty-six letters fit in a bit mask, flipped when a letter is pushed or popped.
>
> Last-occurrence indices and the monotonic pops stay the same.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
