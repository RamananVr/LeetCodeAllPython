---
comments: true
difficulty: Medium
tags:
    - Trie
    - Array
    - Hash Table
    - String
    - Binary Search
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> and an array of strings <code>words</code>, return <em>the number of</em> <code>words[i]</code> <em>that is a subsequence of</em> <code>s</code>.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<ul>
	<li>For example, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcde&quot;, words = [&quot;a&quot;,&quot;bb&quot;,&quot;acd&quot;,&quot;ace&quot;]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three strings in words that are a subsequence of s: &quot;a&quot;, &quot;acd&quot;, &quot;ace&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;dsahjpjauf&quot;, words = [&quot;ahjpjau&quot;,&quot;ja&quot;,&quot;ahbwzgqnuk&quot;,&quot;tnmlanowax&quot;]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words.length &lt;= 5000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>s</code> and <code>words[i]</code> consist of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bucketing

<!-- thinking:start -->

> **Thinking**
>
> $|s|\le 5\times 10^4$; a pointer scan per word rereads $s$. Bucket words by their next needed letter and, while scanning $s$, advance only that bucket.
>
> A finished word counts; otherwise the remainder goes to the bucket of its new head. Each character of each word is handled once.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(deque)
        for w in words:
            d[w[0]].append(w)
        ans = 0
        for c in s:
            for _ in range(len(d[c])):
                t = d[c].popleft()
                if len(t) == 1:
                    ans += 1
                else:
                    d[t[1]].append(t[1:])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Bucketing (Index Pointers)

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 slices leftover strings. Store $(word\_index, matched\_len)$ instead; same buckets, less allocation.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(deque)
        for i, w in enumerate(words):
            d[w[0]].append((i, 0))
        ans = 0
        for c in s:
            for _ in range(len(d[c])):
                i, j = d[c].popleft()
                j += 1
                if j == len(words[i]):
                    ans += 1
                else:
                    d[words[i][j]].append((i, j))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Binary Search

<!-- thinking:start -->

> **Thinking**
>
> Bucketing keeps all words live. Alternatively, store every index of each letter in $s$ and binary-search the next position for each character of $w$.
>
> A test is $O(|w|\log n)$ and needs no queues.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def check(w):
            i = -1
            for c in w:
                j = bisect_right(d[c], i)
                if j == len(d[c]):
                    return False
                i = d[c][j]
            return True

        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        return sum(check(w) for w in words)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
