---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2700-2799/2785.Sort%20Vowels%20in%20a%20String/README_EN.md
rating: 1266
source: Biweekly Contest 109 Q2
tags:
    - String
    - Sorting
---

<!-- problem:start -->

# [2785. Sort Vowels in a String](https://leetcode.com/problems/sort-vowels-in-a-string)

## Description

<!-- description:start -->

<p>Given a <strong>0-indexed</strong> string <code>s</code>, <strong>permute</strong> <code>s</code> to get a new string <code>t</code> such that:</p>

<ul>
	<li>All consonants remain in their original places. More formally, if there is an index <code>i</code> with <code>0 &lt;= i &lt; s.length</code> such that <code>s[i]</code> is a consonant, then <code>t[i] = s[i]</code>.</li>
	<li>The vowels must be sorted in the <strong>nondecreasing</strong> order of their <strong>ASCII</strong> values. More formally, for pairs of indices <code>i</code>, <code>j</code> with <code>0 &lt;= i &lt; j &lt; s.length</code> such that <code>s[i]</code> and <code>s[j]</code> are vowels, then <code>t[i]</code> must not have a higher ASCII value than <code>t[j]</code>.</li>
</ul>

<p>Return <em>the resulting string</em>.</p>

<p>The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;lEetcOde&quot;
<strong>Output:</strong> &quot;lEOtcede&quot;
<strong>Explanation:</strong> &#39;E&#39;, &#39;O&#39;, and &#39;e&#39; are the vowels in s; &#39;l&#39;, &#39;t&#39;, &#39;c&#39;, and &#39;d&#39; are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;lYmpH&quot;
<strong>Output:</strong> &quot;lYmpH&quot;
<strong>Explanation:</strong> There are no vowels in s (all characters in s are consonants), so we return &quot;lYmpH&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of letters of the&nbsp;English alphabet&nbsp;in <strong>uppercase and lowercase</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

First, we store all the vowels in the string into an array or list $vs$, then we sort $vs$.

Next, we traverse the string $s$, keeping the consonants unchanged. If it is a vowel, we replace it in order with the letters in the $vs$ array.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Where $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        vs = [c for c in s if c.lower() in "aeiou"]
        vs.sort()
        cs = list(s)
        j = 0
        for i, c in enumerate(cs):
            if c.lower() in "aeiou":
                cs[i] = vs[j]
                j += 1
        return "".join(cs)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
