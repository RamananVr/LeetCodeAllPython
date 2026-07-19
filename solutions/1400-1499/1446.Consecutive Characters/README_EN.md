---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1446.Consecutive%20Characters/README_EN.md
rating: 1165
source: Biweekly Contest 26 Q1
tags:
    - String
---

<!-- problem:start -->

# [1446. Consecutive Characters](https://leetcode.com/problems/consecutive-characters)

## Description

<!-- description:start -->

<p>The <strong>power</strong> of the string is the maximum length of a non-empty substring that contains only one unique character.</p>

<p>Given a string <code>s</code>, return <em>the <strong>power</strong> of</em> <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The substring &quot;ee&quot; is of length 2 with the character &#39;e&#39; only.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbcccddddeeeeedcba&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The substring &quot;eeeee&quot; is of length 5 with the character &#39;e&#39; only.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Traversal and Counting

We define a variable $\textit{t}$ to represent the length of the current consecutive characters, initially $\textit{t}=1$.

Next, we traverse the string $s$ starting from the second character. If the current character is the same as the previous character, then $\textit{t} = \textit{t} + 1$, and update the answer $\textit{ans} = \max(\textit{ans}, \textit{t})$; otherwise, set $\textit{t} = 1$.

Finally, return the answer $\textit{ans}$.

The time complexity is $O(n)$, where $n$ is the length of the string $s$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxPower(self, s: str) -> int:
        ans = t = 1
        for a, b in pairwise(s):
            if a == b:
                t += 1
                ans = max(ans, t)
            else:
                t = 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
