---
comments: true
difficulty: Medium
rating: 1646
source: Biweekly Contest 20 Q3
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>&nbsp;consisting only of characters <em>a</em>, <em>b</em> and <em>c</em>.</p>

<p>Return the number of substrings containing <b>at least</b>&nbsp;one occurrence of all these characters <em>a</em>, <em>b</em> and <em>c</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabc&quot;
<strong>Output:</strong> 10
<strong>Explanation:</strong> The substrings containing&nbsp;at least&nbsp;one occurrence of the characters&nbsp;<em>a</em>,&nbsp;<em>b</em>&nbsp;and&nbsp;<em>c are &quot;</em>abc<em>&quot;, &quot;</em>abca<em>&quot;, &quot;</em>abcab<em>&quot;, &quot;</em>abcabc<em>&quot;, &quot;</em>bca<em>&quot;, &quot;</em>bcab<em>&quot;, &quot;</em>bcabc<em>&quot;, &quot;</em>cab<em>&quot;, &quot;</em>cabc<em>&quot; </em>and<em> &quot;</em>abc<em>&quot; </em>(<strong>again</strong>)<em>. </em>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaacb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substrings containing&nbsp;at least&nbsp;one occurrence of the characters&nbsp;<em>a</em>,&nbsp;<em>b</em>&nbsp;and&nbsp;<em>c are &quot;</em>aaacb<em>&quot;, &quot;</em>aacb<em>&quot; </em>and<em> &quot;</em>acb<em>&quot;.</em><em> </em>
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 5 x 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;only consists of <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code> or <code>&#39;c&#39;</code> characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Single Pass

<!-- thinking:start -->

> **Thinking**
>
> Count substrings that contain $a$, $b$, and $c$. $n \le 5 \times 10^4$ rules out both endpoints. With right end $i$, every left end at most the earliest of the three last-seen positions is valid. Tracking those three indices, we add $\min(d[a],d[b],d[c])+1$ at each $i$.

<!-- thinking:end -->

We use an array $d$ of length $3$ to record the most recent occurrence of the three characters, initially all set to $-1$.

We traverse the string $s$. For the current position $i$, we first update $d[s[i]]=i$, then the number of valid strings is $\min(d[0], d[1], d[2]) + 1$, which is accumulated to the answer.

The time complexity is $O(n)$, where $n$ is the length of the string $s$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {"a": -1, "b": -1, "c": -1}
        ans = 0
        for i, c in enumerate(s):
            d[c] = i
            ans += min(d["a"], d["b"], d["c"]) + 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Sliding Window

<!-- thinking:start -->

> **Thinking**
>
> The first method uses last-seen indices. A counting window works as well: after extending $r$, shrink $l$ while all three letters remain, then add the current $l$ as the number of valid left ends. Both are linear; the window never stores last positions.

<!-- thinking:end -->

We can solve this using a sliding window. Maintain a window $[l, r]$ and an array $\textit{cnt}$ recording the frequency of each character in the window.

Traverse the string and keep moving the right boundary $r$ to include $s[r]$. If the window contains at least one $a$, $b$, and $c$, keep moving the left boundary $l$ to the right until the window no longer contains all three characters.

At this point, all substrings ending at $r$ that contain $a$, $b$, and $c$ can start at indices $0, 1, \ldots, l - 1$, giving $l$ valid substrings in total. Add this count to the answer.

The time complexity is $O(n)$, where $n$ is the length of the string $s$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = l = 0
        cnt = Counter()
        for r, c in enumerate(s):
            cnt[c] += 1
            while cnt['a'] and cnt['b'] and cnt['c']:
                cnt[s[l]] -= 1
                l += 1
            ans += l
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
