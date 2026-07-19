---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1900-1999/1915.Number%20of%20Wonderful%20Substrings/README_EN.md
rating: 2234
source: Weekly Contest 247 Q3
tags:
    - Bit Manipulation
    - Hash Table
    - String
    - Prefix Sum
---

<!-- problem:start -->

# [1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings)

## Description

<!-- description:start -->

<p>A <strong>wonderful</strong> string is a string where <strong>at most one</strong> letter appears an <strong>odd</strong> number of times.</p>

<ul>

    <li>For example, <code>&quot;ccjjc&quot;</code> and <code>&quot;abab&quot;</code> are wonderful, but <code>&quot;ab&quot;</code> is not.</li>

</ul>

<p>Given a string <code>word</code> that consists of the first ten lowercase English letters (<code>&#39;a&#39;</code> through <code>&#39;j&#39;</code>), return <em>the <strong>number of wonderful non-empty substrings</strong> in </em><code>word</code><em>. If the same substring appears multiple times in </em><code>word</code><em>, then count <strong>each occurrence</strong> separately.</em></p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>

<strong>Input:</strong> word = &quot;aba&quot;

<strong>Output:</strong> 4

<strong>Explanation:</strong> The four wonderful substrings are underlined below:

- &quot;<u><strong>a</strong></u>ba&quot; -&gt; &quot;a&quot;

- &quot;a<u><strong>b</strong></u>a&quot; -&gt; &quot;b&quot;

- &quot;ab<u><strong>a</strong></u>&quot; -&gt; &quot;a&quot;

- &quot;<u><strong>aba</strong></u>&quot; -&gt; &quot;aba&quot;

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>

<strong>Input:</strong> word = &quot;aabb&quot;

<strong>Output:</strong> 9

<strong>Explanation:</strong> The nine wonderful substrings are underlined below:

- &quot;<strong><u>a</u></strong>abb&quot; -&gt; &quot;a&quot;

- &quot;<u><strong>aa</strong></u>bb&quot; -&gt; &quot;aa&quot;

- &quot;<u><strong>aab</strong></u>b&quot; -&gt; &quot;aab&quot;

- &quot;<u><strong>aabb</strong></u>&quot; -&gt; &quot;aabb&quot;

- &quot;a<u><strong>a</strong></u>bb&quot; -&gt; &quot;a&quot;

- &quot;a<u><strong>abb</strong></u>&quot; -&gt; &quot;abb&quot;

- &quot;aa<u><strong>b</strong></u>b&quot; -&gt; &quot;b&quot;

- &quot;aa<u><strong>bb</strong></u>&quot; -&gt; &quot;bb&quot;

- &quot;aab<u><strong>b</strong></u>&quot; -&gt; &quot;b&quot;

</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>

<strong>Input:</strong> word = &quot;he&quot;

<strong>Output:</strong> 2

<strong>Explanation:</strong> The two wonderful substrings are underlined below:

- &quot;<b><u>h</u></b>e&quot; -&gt; &quot;h&quot;

- &quot;h<strong><u>e</u></strong>&quot; -&gt; &quot;e&quot;

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>

    <li><code>word</code> consists of lowercase English letters from <code>&#39;a&#39;</code>&nbsp;to <code>&#39;j&#39;</code>.</li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix XOR + Counting

Since the string contains only $10$ lowercase letters, we can use a $10$-bit integer to represent the parity of each letter count in the current prefix. The $i$-th bit is $1$ if the $i$-th letter appears an odd number of times, and $0$ if it appears an even number of times.

We iterate through each character in the string. Use a variable $st$ to maintain the current prefix XOR state, and an array $cnt$ to record how many times each prefix state has appeared. Initially, $st = 0$ and $cnt[0] = 1$.

For each character, update the prefix XOR state. If the current state has appeared $cnt[st]$ times, it means there are $cnt[st]$ substrings in which all letter counts are even, so we add $cnt[st]$ to the answer. In addition, for $0 \le i < 10$, toggling the $i$-th bit of $st$ (i.e., $st \oplus (1 << i)$) represents substrings where exactly one letter has an odd count, so we add $cnt[st \oplus (1 << i)]$ to the answer. Finally, increment the occurrence count of $st$ by $1$, and continue.

The time complexity is $O(n \times \Sigma)$, and the space complexity is $O(2^{\Sigma})$, where $\Sigma = 10$ and $n$ is the length of the string.

Similar problems:

- [1371. 每个元音包含偶数次的最长子字符串](https://github.com/doocs/leetcode/blob/main/solution/1300-1399/1371.Find%20the%20Longest%20Substring%20Containing%20Vowels%20in%20Even%20Counts/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = st = 0
        for c in word:
            st ^= 1 << (ord(c) - ord("a"))
            ans += cnt[st]
            ans += sum(cnt[st ^ (1 << i)] for i in range(10))
            cnt[st] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
