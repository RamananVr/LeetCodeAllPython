---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1684.Count%20the%20Number%20of%20Consistent%20Strings/README_EN.md
rating: 1288
source: Biweekly Contest 41 Q1
tags:
    - Bit Manipulation
    - Array
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [1684. Count the Number of Consistent Strings](https://leetcode.com/problems/count-the-number-of-consistent-strings)

## Description

<!-- description:start -->

<p>You are given a string <code>allowed</code> consisting of <strong>distinct</strong> characters and an array of strings <code>words</code>. A string is <strong>consistent </strong>if all characters in the string appear in the string <code>allowed</code>.</p>

<p>Return<em> the number of <strong>consistent</strong> strings in the array </em><code>words</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> allowed = &quot;ab&quot;, words = [&quot;ad&quot;,&quot;bd&quot;,&quot;aaab&quot;,&quot;baa&quot;,&quot;badab&quot;]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Strings &quot;aaab&quot; and &quot;baa&quot; are consistent since they only contain characters &#39;a&#39; and &#39;b&#39;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> allowed = &quot;abc&quot;, words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;ab&quot;,&quot;ac&quot;,&quot;bc&quot;,&quot;abc&quot;]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All strings are consistent.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> allowed = &quot;cad&quot;, words = [&quot;cc&quot;,&quot;acd&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bac&quot;,&quot;bad&quot;,&quot;ac&quot;,&quot;d&quot;]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Strings &quot;cc&quot;, &quot;acd&quot;, &quot;ac&quot;, and &quot;d&quot; are consistent.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= allowed.length &lt;=<sup> </sup>26</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li>The characters in <code>allowed</code> are <strong>distinct</strong>.</li>
	<li><code>words[i]</code> and <code>allowed</code> contain only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table or Array

A straightforward approach is to use a hash table or array $s$ to record the characters in `allowed`. Then iterate over the `words` array, for each string $w$, determine whether it is composed of characters in `allowed`. If so, increment the answer.

The time complexity is $O(m)$, and the space complexity is $O(C)$. Here, $m$ is the total length of all strings, and $C$ is the size of the character set `allowed`. In this problem, $C \leq 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        return sum(all(c in s for c in w) for w in words)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Bit Manipulation

We can also use a single integer to represent the occurrence of characters in each string. In this integer, each bit in the binary representation indicates whether a character appears.

We simply define a function $f(w)$ that can convert a string $w$ into an integer. Each bit in the binary representation of the integer indicates whether a character appears. For example, the string `ab` can be converted into the integer $3$, which is represented in binary as $11$. The string `abd` can be converted into the integer $11$, which is represented in binary as $1011$.

Back to the problem, to determine whether a string $w$ is composed of characters in `allowed`, we can check whether the result of the bitwise OR operation between $f(allowed)$ and $f(w)$ is equal to $f(allowed)$. If so, increment the answer.

The time complexity is $O(m)$, where $m$ is the total length of all strings. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def f(w):
            return reduce(or_, (1 << (ord(c) - ord('a')) for c in w))

        mask = f(allowed)
        return sum((mask | f(w)) == mask for w in words)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
