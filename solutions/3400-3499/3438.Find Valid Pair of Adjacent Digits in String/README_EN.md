---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3438.Find%20Valid%20Pair%20of%20Adjacent%20Digits%20in%20String/README_EN.md
rating: 1225
source: Biweekly Contest 149 Q1
tags:
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [3438. Find Valid Pair of Adjacent Digits in String](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> consisting only of digits. A <strong>valid pair</strong> is defined as two <strong>adjacent</strong> digits in <code>s</code> such that:</p>

<ul>
	<li>The first digit is <strong>not equal</strong> to the second.</li>
	<li>Each digit in the pair appears in <code>s</code> <strong>exactly</strong> as many times as its numeric value.</li>
</ul>

<p>Return the first <strong>valid pair</strong> found in the string <code>s</code> when traversing from left to right. If no valid pair exists, return an empty string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;2523533&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;23&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Digit <code>&#39;2&#39;</code> appears 2 times and digit <code>&#39;3&#39;</code> appears 3 times. Each digit in the pair <code>&quot;23&quot;</code> appears in <code>s</code> exactly as many times as its numeric value. Hence, the output is <code>&quot;23&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;221&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;21&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Digit <code>&#39;2&#39;</code> appears 2 times and digit <code>&#39;1&#39;</code> appears 1 time. Hence, the output is <code>&quot;21&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;22&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no valid adjacent pairs.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> only consists of digits from <code>&#39;1&#39;</code> to <code>&#39;9&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We can use an array $\textit{cnt}$ of length $10$ to record the occurrences of each digit in the string $\textit{s}$.

Then, we traverse the adjacent digit pairs in the string $\textit{s}$. If the two digits are not equal and the occurrences of these two digits are equal to the digits themselves, we have found a valid pair of adjacent digits and return it.

After traversing, if no valid pair of adjacent digits is found, we return an empty string.

The time complexity is $O(n)$, where $n$ is the length of the string $\textit{s}$. The space complexity is $O(|\Sigma|)$, where $\Sigma$ is the character set of the string $\textit{s}$. In this problem, $\Sigma = \{1, 2, \ldots, 9\}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = [0] * 10
        for x in map(int, s):
            cnt[x] += 1
        for x, y in pairwise(map(int, s)):
            if x != y and cnt[x] == x and cnt[y] == y:
                return f"{x}{y}"
        return ""
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
