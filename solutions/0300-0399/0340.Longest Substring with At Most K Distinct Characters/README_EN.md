---
comments: true
difficulty: Medium
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [340. Longest Substring with At Most K Distinct Characters 🔒](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the length of the longest </em><span data-keyword="substring-nonempty"><em>substring</em></span><em> of</em> <code>s</code> <em>that contains at most</em> <code>k</code> <em><strong>distinct</strong> characters</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;eceba&quot;, k = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring is &quot;ece&quot; with length 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The substring is &quot;aa&quot; with length 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 50</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sliding Window + Hash Table

<!-- thinking:start -->

> **Thinking**
>
> Longest substring with at most $k$ distinct characters. Checking every pair of ends is $O(n^2)$. Distinctness grows with the right end and shrinks when the left advances, so a sliding window works.
>
> Admit the right character; while the map has more than $k$ keys, drop the left. The window is always the longest legal suffix of the prefix, and the length is $n-l$.

<!-- thinking:end -->

We can use the idea of a sliding window, with a hash table $\textit{cnt}$ to record the occurrence count of each character within the window, and $\textit{l}$ to denote the left boundary of the window.

Iterate through the string, adding the character at the right boundary to the hash table each time. If the number of distinct characters in the hash table exceeds $k$, remove the character at the left boundary from the hash table, then update the left boundary $\textit{l}$.

Finally, return the length of the string minus the length of the left boundary.

The time complexity is $O(n)$, and the space complexity is $O(k)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        cnt = Counter()
        for c in s:
            cnt[c] += 1
            if len(cnt) > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
        return len(s) - l
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
