---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0076.Minimum%20Window%20Substring/README_EN.md
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)

## Description

<!-- description:start -->

<p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return <em>the <strong>minimum window</strong></em> <span data-keyword="substring-nonempty"><strong><em>substring</em></strong></span><em> of </em><code>s</code><em> such that every character in </em><code>t</code><em> (<strong>including duplicates</strong>) is included in the window</em>. If there is no such substring, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>The testcases will be generated such that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ADOBECODEBANC&quot;, t = &quot;ABC&quot;
<strong>Output:</strong> &quot;BANC&quot;
<strong>Explanation:</strong> The minimum window substring &quot;BANC&quot; includes &#39;A&#39;, &#39;B&#39;, and &#39;C&#39; from string t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;a&quot;
<strong>Output:</strong> &quot;a&quot;
<strong>Explanation:</strong> The entire string s is the minimum window.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;aa&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> Both &#39;a&#39;s from t must be included in the window.
Since the largest window of s only has one &#39;a&#39;, return empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>n == t.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> time?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Two Pointers

We use a hash table or array $\textit{need}$ to count the occurrences of each character in string $t$, and another hash table or array $\textit{window}$ to count the occurrences of each character in the sliding window. Additionally, we define two pointers $l$ and $r$ to point to the left and right boundaries of the window, a variable $\textit{cnt}$ to represent how many characters from $t$ are already included in the window, and variables $k$ and $\textit{mi}$ to represent the starting position and length of the minimum window substring.

We traverse the string $s$ from left to right. For the current character $s[r]$:

- We add it to the window, i.e., $\textit{window}[s[r]] = \textit{window}[s[r]] + 1$. If $\textit{need}[s[r]] \geq \textit{window}[s[r]]$, it means $s[r]$ is a "necessary character", and we increment $\textit{cnt}$ by one.
- If $\textit{cnt}$ equals the length of $t$, it means the window already contains all characters from $t$, and we can try to update the starting position and length of the minimum window substring. If $r - l + 1 < \textit{mi}$, it means the current window represents a shorter substring, so we update $\textit{mi} = r - l + 1$ and $k = l$.
- Then, we try to move the left boundary $l$. If $\textit{need}[s[l]] \geq \textit{window}[s[l]]$, it means $s[l]$ is a "necessary character", and moving the left boundary will remove $s[l]$ from the window. Therefore, we need to decrement $\textit{cnt}$ by one, update $\textit{window}[s[l]] = \textit{window}[s[l]] - 1$, and move $l$ one position to the right.
- If $\textit{cnt}$ is not equal to the length of $t$, it means the window does not yet contain all characters from $t$, so we do not need to move the left boundary. Instead, we move $r$ one position to the right and continue traversing.

After the traversal, if no minimum window substring is found, return an empty string. Otherwise, return $s[k:k+\textit{mi}]$.

The time complexity is $O(m + n)$, and the space complexity is $O(|\Sigma|)$. Here, $m$ and $n$ are the lengths of strings $s$ and $t$, respectively; and $|\Sigma|$ is the size of the character set, which is $128$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        cnt = l = 0
        k, mi = -1, inf
        for r, c in enumerate(s):
            window[c] += 1
            if need[c] >= window[c]:
                cnt += 1
            while cnt == len(t):
                if r - l + 1 < mi:
                    mi = r - l + 1
                    k = l
                if need[s[l]] >= window[s[l]]:
                    cnt -= 1
                window[s[l]] -= 1
                l += 1
        return "" if k < 0 else s[k : k + mi]

```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
