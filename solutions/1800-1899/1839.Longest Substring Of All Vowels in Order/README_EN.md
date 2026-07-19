---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1839.Longest%20Substring%20Of%20All%20Vowels%20in%20Order/README_EN.md
rating: 1580
source: Weekly Contest 238 Q3
tags:
    - String
    - Sliding Window
---

<!-- problem:start -->

# [1839. Longest Substring Of All Vowels in Order](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order)

## Description

<!-- description:start -->

<p>A string is considered <strong>beautiful</strong> if it satisfies the following conditions:</p>

<ul>
	<li>Each of the 5 English vowels (<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, <code>&#39;u&#39;</code>) must appear <strong>at least once</strong> in it.</li>
	<li>The letters must be sorted in <strong>alphabetical order</strong> (i.e. all <code>&#39;a&#39;</code>s before <code>&#39;e&#39;</code>s, all <code>&#39;e&#39;</code>s before <code>&#39;i&#39;</code>s, etc.).</li>
</ul>

<p>For example, strings <code>&quot;aeiou&quot;</code> and <code>&quot;aaaaaaeiiiioou&quot;</code> are considered <strong>beautiful</strong>, but <code>&quot;uaeio&quot;</code>, <code>&quot;aeoiu&quot;</code>, and <code>&quot;aaaeeeooo&quot;</code> are <strong>not beautiful</strong>.</p>

<p>Given a string <code>word</code> consisting of English vowels, return <em>the <strong>length of the longest beautiful substring</strong> of </em><code>word</code><em>. If no such substring exists, return </em><code>0</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;aeiaaio<u>aaaaeiiiiouuu</u>ooaauuaeiu&quot;
<strong>Output:</strong> 13
<b>Explanation:</b> The longest beautiful substring in word is &quot;aaaaeiiiiouuu&quot; of length 13.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;aeeeiiiioooauuu<u>aeiou</u>&quot;
<strong>Output:</strong> 5
<b>Explanation:</b> The longest beautiful substring in word is &quot;aeiou&quot; of length 5.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;a&quot;
<strong>Output:</strong> 0
<b>Explanation:</b> There is no beautiful substring, so return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>word</code> consists of characters <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers + Simulation

We can first transform the string `word`. For example, for `word="aaaeiouu"`, we can transform it into data items `('a', 3)`, `('e', 1)`, `('i', 1)`, `('o', 1)`, `('u', 2)` and store them in an array `arr`. Each data item's first element represents a vowel, and the second element represents the number of times the vowel appears consecutively. This transformation can be implemented using two pointers.

Next, we traverse the array `arr`, each time taking $5$ adjacent data items, and judge whether the vowels in these data items are `'a'`, `'e'`, `'i'`, `'o'`, `'u'` respectively. If so, calculate the total number of times the vowels appear in these $5$ data items, which is the length of the current beautiful substring, and update the maximum value of the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the string `word`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        arr = []
        n = len(word)
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            arr.append((word[i], j - i))
            i = j
        ans = 0
        for i in range(len(arr) - 4):
            a, b, c, d, e = arr[i : i + 5]
            if a[0] + b[0] + c[0] + d[0] + e[0] == "aeiou":
                ans = max(ans, a[1] + b[1] + c[1] + d[1] + e[1])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
