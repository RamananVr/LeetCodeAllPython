---
comments: true
difficulty: Medium
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [159. Longest Substring with At Most Two Distinct Characters 🔒](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, return <em>the length of the longest </em><span data-keyword="substring-nonempty"><em>substring</em></span><em> that contains at most <strong>two distinct characters</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;eceba&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring is &quot;ece&quot; which its length is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ccaabbb&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The substring is &quot;aabbb&quot; which its length is 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Longest substring with at most two distinct characters. $n\le 10^5$, so enumerating endpoints is $O(n^2)$. The distinct count grows with the right end and shrinks with the left. Extend right while counting; when there are more than two kinds, move left. Update the answer on a valid window.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        cnt = Counter()
        ans = j = 0
        for i, c in enumerate(s):
            cnt[c] += 1
            while len(cnt) > 2:
                cnt[s[j]] -= 1
                if cnt[s[j]] == 0:
                    cnt.pop(s[j])
                j += 1
            ans = max(ans, i - j + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
