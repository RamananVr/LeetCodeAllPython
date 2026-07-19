---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3517.Smallest%20Palindromic%20Rearrangement%20I/README_EN.md
rating: 1357
source: Weekly Contest 445 Q2
tags:
    - String
    - Counting Sort
    - Sorting
---

<!-- problem:start -->

# [3517. Smallest Palindromic Rearrangement I](https://leetcode.com/problems/smallest-palindromic-rearrangement-i)

## Description

<!-- description:start -->

<p>You are given a <strong><span data-keyword="palindrome-string">palindromic</span></strong> string <code>s</code>.</p>

<p>Return the <strong><span data-keyword="lexicographically-smaller-string">lexicographically smallest</span></strong> palindromic <span data-keyword="permutation-string">permutation</span> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;z&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;z&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>A string of only one character is already the lexicographically smallest palindrome.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;babab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;abbba&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Rearranging <code>&quot;babab&quot;</code> &rarr; <code>&quot;abbba&quot;</code> gives the smallest lexicographic palindrome.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;daccad&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;acddca&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Rearranging <code>&quot;daccad&quot;</code> &rarr; <code>&quot;acddca&quot;</code> gives the smallest lexicographic palindrome.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>s</code> is guaranteed to be palindromic.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We first count the occurrence of each character in the string and record it in a hash table or array $\textit{cnt}$. Since the string is a palindrome, the count of each character is either even, or there is exactly one character with an odd count.

Next, starting from the lexicographically smallest character, we sequentially add half of each character's count to the first half of the result string $\textit{t}$. If a character appears an odd number of times, we record it as the middle character $\textit{ch}$. Finally, we concatenate $\textit{t}$, $\textit{ch}$, and the reverse of $\textit{t}$ to obtain the final lexicographically smallest palindromic rearrangement.

The time complexity is $O(n)$, where $n$ is the length of the string. The space complexity is $O(|\Sigma|)$, where $|\Sigma|$ is the size of the character set, which is $26$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        t = []
        ch = ""
        for c in ascii_lowercase:
            v = cnt[c] // 2
            t.append(c * v)
            cnt[c] -= v * 2
            if cnt[c] == 1:
                ch = c
        ans = "".join(t)
        ans = ans + ch + ans[::-1]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
