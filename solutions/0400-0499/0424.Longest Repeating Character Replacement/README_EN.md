---
comments: true
difficulty: Medium
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most <code>k</code> times.</p>

<p>Return <em>the length of the longest substring containing the same letter you can get after performing the above operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ABAB&quot;, k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the two &#39;A&#39;s with two &#39;B&#39;s or vice versa.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;AABABBA&quot;, k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the one &#39;A&#39; in the middle with &#39;B&#39; and form &quot;AABBBBA&quot;.
The substring &quot;BBBB&quot; has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only uppercase English letters.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

<!-- thinking:start -->

> **Thinking**
>
> A window can be made uniform with at most $k$ changes iff its length minus the majority count is at most $k$. Trying every pair of ends is $O(n^2)$.
>
> Expand the right end while tracking the maximum frequency $\textit{mx}$. When $r-l+1-\textit{mx}>k$, shift the left end by one. The longest legal window has length $n-l$.
>
> There is no need to decrease $\textit{mx}$ on a left move: we only want the maximum length, and an overestimate of $\textit{mx}$ only makes the test stricter.

<!-- thinking:end -->

We use a hash table `cnt` to count the occurrence of each character in the string, and two pointers `l` and `r` to maintain a sliding window, such that the size of the window minus the count of the most frequent character does not exceed $k$.

We iterate through the string, updating the right boundary `r` of the window each time, updating the count of characters within the window, and updating the maximum count `mx` of the characters that have appeared. When the size of the window minus `mx` is greater than $k$, we need to shrink the left boundary `l` of the window, updating the count of characters within the window, until the size of the window minus `mx` is no longer greater than $k$.

Finally, the answer is $n - l$, where $n$ is the length of the string.

The time complexity is $O(n)$, and the space complexity is $O(|\Sigma|)$. Where $n$ is the length of the string, and $|\Sigma|$ is the size of the character set. In this problem, the character set is uppercase English letters, so $|\Sigma| = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        l = mx = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            mx = max(mx, cnt[c])
            if r - l + 1 - mx > k:
                cnt[s[l]] -= 1
                l += 1
        return len(s) - l
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
