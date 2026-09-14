---
comments: true
difficulty: Easy
rating: 1288
source: Weekly Contest 417 Q1
tags:
    - Bit Manipulation
    - Recursion
    - Math
    - Simulation
---

<!-- problem:start -->

# [3304. Find the K-th Character in String Game I](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i)

## Description

<!-- description:start -->

<p>Alice and Bob are playing a game. Initially, Alice has a string <code>word = &quot;a&quot;</code>.</p>

<p>You are given a <strong>positive</strong> integer <code>k</code>.</p>

<p>Now Bob will ask Alice to perform the following operation <strong>forever</strong>:</p>

<ul>
	<li>Generate a new string by <strong>changing</strong> each character in <code>word</code> to its <strong>next</strong> character in the English alphabet, and <strong>append</strong> it to the <em>original</em> <code>word</code>.</li>
</ul>

<p>For example, performing the operation on <code>&quot;c&quot;</code> generates <code>&quot;cd&quot;</code> and performing the operation on <code>&quot;zb&quot;</code> generates <code>&quot;zbac&quot;</code>.</p>

<p>Return the value of the <code>k<sup>th</sup></code> character in <code>word</code>, after enough operations have been done for <code>word</code> to have <strong>at least</strong> <code>k</code> characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;b&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>word = &quot;a&quot;</code>. We need to do the operation three times:</p>

<ul>
	<li>Generated string is <code>&quot;b&quot;</code>, <code>word</code> becomes <code>&quot;ab&quot;</code>.</li>
	<li>Generated string is <code>&quot;bc&quot;</code>, <code>word</code> becomes <code>&quot;abbc&quot;</code>.</li>
	<li>Generated string is <code>&quot;bccd&quot;</code>, <code>word</code> becomes <code>&quot;abbcbccd&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;c&quot;</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 500</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> Each operation appends a copy of the current word with every letter shifted by one, doubling the length. Since $k \le 500$, we can simulate until the length is at least $k$.
>
> Storing offsets in $0..25$ avoids building strings: the appended half is the old half plus one, modulo $26$.
>
> The answer is the letter at index $k-1$ once the array is long enough.

<!-- thinking:end -->

We can use an array $\textit{word}$ to store the string after each operation. When the length of $\textit{word}$ is less than $k$, we continuously perform operations on $\textit{word}$.

Finally, return $\textit{word}[k - 1]$.

The time complexity is $O(k)$, and the space complexity is $O(k)$. Here, $k$ is the input parameter.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = [0]
        while len(word) < k:
            word.extend([(x + 1) % 26 for x in word])
        return chr(ord("a") + word[k - 1])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
