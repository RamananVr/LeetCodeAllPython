---
comments: true
difficulty: Easy
tags:
    - Hash Table
    - String
---

<!-- problem:start -->

# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones)

## Description

<!-- description:start -->

<p>You&#39;re given strings <code>jewels</code> representing the types of stones that are jewels, and <code>stones</code> representing the stones you have. Each character in <code>stones</code> is a type of stone you have. You want to know how many of the stones you have are also jewels.</p>

<p>Letters are case sensitive, so <code>&quot;a&quot;</code> is considered a different type of stone from <code>&quot;A&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> jewels = "aA", stones = "aAAbbbb"
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> jewels = "z", stones = "ZZ"
<strong>Output:</strong> 0
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;jewels.length, stones.length &lt;= 50</code></li>
	<li><code>jewels</code> and <code>stones</code> consist of only English letters.</li>
	<li>All the characters of&nbsp;<code>jewels</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table or Array

<!-- thinking:start -->

> **Thinking**
>
> Count how many stones are jewels. Length $50$: put jewels in a set and test each stone. Case matters.

<!-- thinking:end -->

We can first use a hash table or array $s$ to record all types of jewels. Then traverse all the stones, and if the current stone is a jewel, increment the answer by one.

Time complexity is $O(m+n)$, and space complexity is $O(|\Sigma|)$, where $m$ and $n$ are the lengths of the strings $jewels$ and $stones$ respectively, and $\Sigma$ is the character set, which in this problem is the set of all uppercase and lowercase English letters.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        return sum(c in s for c in stones)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
