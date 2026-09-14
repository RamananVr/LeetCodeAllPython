---
comments: true
difficulty: Easy
rating: 1165
source: Weekly Contest 516 Q1
---

<!-- problem:start -->

# [4030. Check ASCII Palindromic](https://leetcode.com/problems/check-ascii-palindromic)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>Construct a <span data-keyword="binary-string"><strong>binary string</strong></span> by replacing each character in <code>s</code> with the 8-bit binary representation of its ASCII value, <strong>including leading zeros</strong>, while preserving the original order of the characters.</p>

<p>Return <code>true</code> if the resulting binary string is a <span data-keyword="palindrome-string"><strong>palindrome</strong></span>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;ff&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The ASCII value of <code>f</code> is 102, whose 8-bit binary representation is <code>01100110</code>.</li>
	<li>Thus, the binary string is <code>0110011001100110</code>.</li>
	<li>Since this binary string is a <strong>palindrome</strong>, the output is <code>true</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leet&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The ASCII values of <code>l</code>, <code>e</code>, <code>e</code>, and <code>t</code> are 108, 101, 101, and 116, respectively.</li>
	<li>Their 8-bit binary representations are <code>01101100</code>, <code>01100101</code>, <code>01100101</code>, and <code>01110100</code>.</li>
	<li>Thus, the binary string is <code>01101100011001010110010101110100</code>.</li>
	<li>Since this binary string is not a <strong>palindrome</strong>, the output is <code>false</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> Each character expands to a fixed $8$-bit string, including leading zeros, and we test whether the concatenation is a palindrome. $n$ is small enough that we need not rewrite the test in terms of character pairs.
>
> Build $t$ in order and compare it with its reverse.

<!-- thinking:end -->

Following the problem statement, we replace each character of $s$ with the $8$-bit binary representation of its ASCII value (including leading zeros), concatenate them in order to obtain a binary string $t$, and then check whether $t$ is a palindrome.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPalindromic(self, s: str) -> bool:
        t = ''.join(format(ord(c), '08b') for c in s)
        return t == t[::-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
