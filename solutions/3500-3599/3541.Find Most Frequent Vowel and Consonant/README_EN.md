---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3541.Find%20Most%20Frequent%20Vowel%20and%20Consonant/README_EN.md
rating: 1238
source: Biweekly Contest 156 Q1
tags:
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [3541. Find Most Frequent Vowel and Consonant](https://leetcode.com/problems/find-most-frequent-vowel-and-consonant)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> consisting of lowercase English letters (<code>&#39;a&#39;</code> to <code>&#39;z&#39;</code>). </p>

<p>Your task is to:</p>

<ul>
	<li>Find the vowel (one of <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, or <code>&#39;u&#39;</code>) with the <strong>maximum</strong> frequency.</li>
	<li>Find the consonant (all other letters excluding vowels) with the <strong>maximum</strong> frequency.</li>
</ul>

<p>Return the sum of the two frequencies.</p>

<p><strong>Note</strong>: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.</p>
The <strong>frequency</strong> of a letter <code>x</code> is the number of times it occurs in the string.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;successes&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The vowels are: <code>&#39;u&#39;</code> (frequency 1), <code>&#39;e&#39;</code> (frequency 2). The maximum frequency is 2.</li>
	<li>The consonants are: <code>&#39;s&#39;</code> (frequency 4), <code>&#39;c&#39;</code> (frequency 2). The maximum frequency is 4.</li>
	<li>The output is <code>2 + 4 = 6</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aeiaeia&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The vowels are: <code>&#39;a&#39;</code> (frequency 3), <code>&#39;e&#39;</code> ( frequency 2), <code>&#39;i&#39;</code> (frequency 2). The maximum frequency is 3.</li>
	<li>There are no consonants in <code>s</code>. Hence, maximum consonant frequency = 0.</li>
	<li>The output is <code>3 + 0 = 3</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters only.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We first use a hash table or an array of length $26$, $\textit{cnt}$, to count the frequency of each letter. Then, we iterate through this table to find the most frequent vowel and consonant, and return the sum of their frequencies.

We can use a variable $\textit{a}$ to record the maximum frequency of vowels and another variable $\textit{b}$ to record the maximum frequency of consonants. During the iteration, if the current letter is a vowel, we update $\textit{a}$; otherwise, we update $\textit{b}$.

Finally, we return $\textit{a} + \textit{b}$.

The time complexity is $O(n)$, where $n$ is the length of the string. The space complexity is $O(|\Sigma|)$, where $|\Sigma|$ is the size of the alphabet, which is $26$ in this case.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        a = b = 0
        for c, v in cnt.items():
            if c in "aeiou":
                a = max(a, v)
            else:
                b = max(b, v)
        return a + b
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
