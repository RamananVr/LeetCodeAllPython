---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2067.Number%20of%20Equal%20Count%20Substrings/README_EN.md
tags:
    - Hash Table
    - String
    - Counting
    - Sliding Window
---

<!-- problem:start -->

# [2067. Number of Equal Count Substrings 🔒](https://leetcode.com/problems/number-of-equal-count-substrings)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> string <code>s</code> consisting of only lowercase English letters, and an integer <code>count</code>. A <strong>substring</strong> of <code>s</code> is said to be an <strong>equal count substring</strong> if, for each <strong>unique</strong> letter in the substring, it appears exactly <code>count</code> times in the substring.</p>

<p>Return <em>the number of <strong>equal count substrings</strong> in </em><code>s</code>.</p>

<p>A <strong>substring</strong> is a contiguous non-empty sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabcbbcc&quot;, count = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The substring that starts at index 0 and ends at index 2 is &quot;aaa&quot;.
The letter &#39;a&#39; in the substring appears exactly 3 times.
The substring that starts at index 3 and ends at index 8 is &quot;bcbbcc&quot;.
The letters &#39;b&#39; and &#39;c&#39; in the substring appear exactly 3 times.
The substring that starts at index 0 and ends at index 8 is &quot;aaabcbbcc&quot;.
The letters &#39;a&#39;, &#39;b&#39;, and &#39;c&#39; in the substring appear exactly 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, count = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, count = 5
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= count &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Sliding Window

We can enumerate the number of types of letters in the substring within the range of $[1..26]$, then the length of the substring is $i \times count$.

Next, we take the current substring length as the size of the window, count the number of types of letters in the window size that are equal to $count$, and record it in $t$. If $i = t$ at this time, it means that the number of letters in the current window are all $count$, then we can increment the answer by one.

The time complexity is $O(n \times C)$, and the space complexity is $O(C)$. Where $n$ is the length of the string $s$, and $C$ is the number of types of letters, in this problem $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        ans = 0
        for i in range(1, 27):
            k = i * count
            if k > len(s):
                break
            cnt = Counter()
            t = 0
            for j, c in enumerate(s):
                cnt[c] += 1
                t += cnt[c] == count
                t -= cnt[c] == count + 1
                if j >= k:
                    cnt[s[j - k]] -= 1
                    t += cnt[s[j - k]] == count
                    t -= cnt[s[j - k]] == count - 1
                ans += i == t
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
