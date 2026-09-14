---
comments: true
difficulty: Medium
rating: 1563
source: Weekly Contest 417 Q2
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [3305. Count of Substrings Containing Every Vowel and K Consonants I](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i)

## Description

<!-- description:start -->

<p>You are given a string <code>word</code> and a <strong>non-negative</strong> integer <code>k</code>.</p>

<p>Return the total number of <span data-keyword="substring-nonempty">substrings</span> of <code>word</code> that contain every vowel (<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>) <strong>at least</strong> once and <strong>exactly</strong> <code>k</code> consonants.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;aeioqq&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no substring with every vowel.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;aeiou&quot;, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only substring with every vowel and zero consonants is <code>word[0..4]</code>, which is <code>&quot;aeiou&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;</span>ieaouqqieaouqq<span class="example-io">&quot;, k = 1</span></p>

<p><strong>Output:</strong> 3</p>

<p><strong>Explanation:</strong></p>

<p>The substrings with every vowel and one consonant are:</p>

<ul>
	<li><code>word[0..5]</code>, which is <code>&quot;ieaouq&quot;</code>.</li>
	<li><code>word[6..11]</code>, which is <code>&quot;qieaou&quot;</code>.</li>
	<li><code>word[7..12]</code>, which is <code>&quot;ieaouq&quot;</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>5 &lt;= word.length &lt;= 250</code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
	<li><code>0 &lt;= k &lt;= word.length - 5</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Problem Transformation + Sliding Window

<!-- thinking:start -->

> **Thinking**
>
> With $|\textit{word}| \le 250$, enumerating substrings works, but a window that must contain every vowel and exactly $k$ consonants is not monotone in a single constraint.
>
> We rewrite “exactly $k$ consonants” as $f(k)-f(k+1)$, where $f(t)$ counts substrings with all five vowels and at least $t$ consonants. The “at least” form lets the left pointer advance whenever the window is valid.
>
> Every substring ending at the current right end and starting in $[0, l)$ is then valid, so we add $l$. A map tracks the five vowels; consonants use a separate counter $x$.

<!-- thinking:end -->

We can transform the problem into solving the following two subproblems:

1. Find the total number of substrings where each vowel appears at least once and contains at least $k$ consonants, denoted as $\textit{f}(k)$;
2. Find the total number of substrings where each vowel appears at least once and contains at least $k + 1$ consonants, denoted as $\textit{f}(k + 1)$.

Then the answer is $\textit{f}(k) - \textit{f}(k + 1)$.

Therefore, we design a function $\textit{f}(k)$ to count the total number of substrings where each vowel appears at least once and contains at least $k$ consonants.

We can use a hash table $\textit{cnt}$ to count the occurrences of each vowel, a variable $\textit{ans}$ to store the answer, a variable $\textit{l}$ to record the left boundary of the sliding window, and a variable $\textit{x}$ to record the number of consonants in the current window.

Traverse the string. If the current character is a vowel, add it to the hash table $\textit{cnt}$; otherwise, increment $\textit{x}$ by one. If $\textit{x} \ge k$ and the size of the hash table $\textit{cnt}$ is $5$, it means the current window meets the conditions. We then move the left boundary in a loop until the window no longer meets the conditions. At this point, all substrings ending at the right boundary $\textit{r}$ and with the left boundary in the range $[0, .. \textit{l} - 1]$ meet the conditions, totaling $\textit{l}$ substrings. We add $\textit{l}$ to the answer. Continue traversing the string until the end, and we get $\textit{f}(k)$.

Finally, we return $\textit{f}(k) - \textit{f}(k + 1)$.

The time complexity is $O(n)$, where $n$ is the length of the string $\textit{word}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def f(k: int) -> int:
            cnt = Counter()
            ans = l = x = 0
            for c in word:
                if c in "aeiou":
                    cnt[c] += 1
                else:
                    x += 1
                while x >= k and len(cnt) == 5:
                    d = word[l]
                    if d in "aeiou":
                        cnt[d] -= 1
                        if cnt[d] == 0:
                            cnt.pop(d)
                    else:
                        x -= 1
                    l += 1
                ans += l
            return ans

        return f(k) - f(k + 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
