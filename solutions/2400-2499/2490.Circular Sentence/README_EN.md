---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2490.Circular%20Sentence/README_EN.md
rating: 1262
source: Weekly Contest 322 Q1
tags:
    - String
---

<!-- problem:start -->

# [2490. Circular Sentence](https://leetcode.com/problems/circular-sentence)

## Description

<!-- description:start -->

<p>A <strong>sentence</strong> is a list of words that are separated by a<strong> single</strong> space with no leading or trailing spaces.</p>

<ul>
	<li>For example, <code>&quot;Hello World&quot;</code>, <code>&quot;HELLO&quot;</code>, <code>&quot;hello world hello world&quot;</code> are all sentences.</li>
</ul>

<p>Words consist of <strong>only</strong> uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.</p>

<p>A sentence is <strong>circular </strong>if:</p>

<ul>
	<li>The last character of each word in the sentence is equal to the first character of its next word.</li>
	<li>The last character of the last word is equal to the first character of the first word.</li>
</ul>

<p>For example, <code>&quot;leetcode exercises sound delightful&quot;</code>, <code>&quot;eetcode&quot;</code>, <code>&quot;leetcode eats soul&quot; </code>are all circular sentences. However, <code>&quot;Leetcode is cool&quot;</code>, <code>&quot;happy Leetcode&quot;</code>, <code>&quot;Leetcode&quot;</code> and <code>&quot;I like Leetcode&quot;</code> are <strong>not</strong> circular sentences.</p>

<p>Given a string <code>sentence</code>, return <code>true</code><em> if it is circular</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;leetcode exercises sound delightful&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The words in sentence are [&quot;leetcode&quot;, &quot;exercises&quot;, &quot;sound&quot;, &quot;delightful&quot;].
- leetcod<u>e</u>&#39;s&nbsp;last character is equal to <u>e</u>xercises&#39;s first character.
- exercise<u>s</u>&#39;s&nbsp;last character is equal to <u>s</u>ound&#39;s first character.
- soun<u>d</u>&#39;s&nbsp;last character is equal to <u>d</u>elightful&#39;s first character.
- delightfu<u>l</u>&#39;s&nbsp;last character is equal to <u>l</u>eetcode&#39;s first character.
The sentence is circular.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;eetcode&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The words in sentence are [&quot;eetcode&quot;].
- eetcod<u>e</u>&#39;s&nbsp;last character is equal to <u>e</u>etcode&#39;s first character.
The sentence is circular.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;Leetcode is cool&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The words in sentence are [&quot;Leetcode&quot;, &quot;is&quot;, &quot;cool&quot;].
- Leetcod<u>e</u>&#39;s&nbsp;last character is <strong>not</strong> equal to <u>i</u>s&#39;s first character.
The sentence is <strong>not</strong> circular.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 500</code></li>
	<li><code>sentence</code> consist of only lowercase and uppercase English letters and spaces.</li>
	<li>The words in <code>sentence</code> are separated by a single space.</li>
	<li>There are no leading or trailing spaces.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We split the string into words by spaces, then check whether the last character of each word is equal to the first character of the next word. If they are not equal, return `false`. Otherwise, return `true` after traversing all the words.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ss = sentence.split()
        n = len(ss)
        return all(s[-1] == ss[(i + 1) % n][0] for i, s in enumerate(ss))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Simulation (Space Optimization)

We can first check whether the first and last characters of the string are equal. If they are not equal, return `false`. Otherwise, traverse the string. If the current character is a space, check whether the previous character and the next character are equal. If they are not equal, return `false`. Otherwise, return `true` after traversing all the characters.

The time complexity is $O(n)$, where $n$ is the length of the string. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isCircularSentence(self, s: str) -> bool:
        return s[0] == s[-1] and all(
            c != " " or s[i - 1] == s[i + 1] for i, c in enumerate(s)
        )
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
