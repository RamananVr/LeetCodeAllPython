---
comments: true
difficulty: Easy
rating: 1279
source: Weekly Contest 126 Q1
tags:
    - Array
    - Hash Table
    - String
---

<!-- problem:start -->

# [1002. Find Common Characters](https://leetcode.com/problems/find-common-characters)

## Description

<!-- description:start -->

<p>Given a string array <code>words</code>, return <em>an array of all characters that show up in all strings within the </em><code>words</code><em> (including duplicates)</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["bella","label","roller"]
<strong>Output:</strong> ["e","l","l"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["cool","lock","cook"]
<strong>Output:</strong> ["c","o"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

<!-- thinking:start -->

> **Thinking**
>
> Scanning every word for each letter is feasible: both the number of words and their lengths are at most $100$. Repeatedly walking the same alphabet still wastes comparisons.
>
> A letter appears in the answer as many times as its minimum frequency over all words — the intersection of the multisets.
>
> We therefore count the first word, take a pointwise $\min$ with every later word, and expand the counts. The alphabet has size $26$, so extra space is constant.

<!-- thinking:end -->

We use an array $cnt$ of length $26$ to record the minimum number of times each character appears in all strings. Finally, we traverse the $cnt$ array and add characters with a count greater than $0$ to the answer.

The time complexity is $O(n \sum w_i)$, and the space complexity is $O(|\Sigma|)$. Here, $n$ is the length of the string array $words$, $w_i$ is the length of the $i$-th string in the array $words$, and $|\Sigma|$ is the size of the character set, which is $26$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for w in words:
            t = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], t[c])
        return list(cnt.elements())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
