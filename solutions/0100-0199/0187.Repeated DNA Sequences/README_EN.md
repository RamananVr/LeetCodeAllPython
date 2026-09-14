---
comments: true
difficulty: Medium
tags:
    - Bit Manipulation
    - Hash Table
    - String
    - Sliding Window
    - Hash Function
    - Rolling Hash
    - Boyer–Moore
    - Extended KMP
---

<!-- problem:start -->

# [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences)

## Description

<!-- description:start -->

<p>The <strong>DNA sequence</strong> is composed of a series of nucleotides abbreviated as <code>&#39;A&#39;</code>, <code>&#39;C&#39;</code>, <code>&#39;G&#39;</code>, and <code>&#39;T&#39;</code>.</p>

<ul>
	<li>For example, <code>&quot;ACGAATTCCG&quot;</code> is a <strong>DNA sequence</strong>.</li>
</ul>

<p>When studying <strong>DNA</strong>, it is useful to identify repeated sequences within the DNA.</p>

<p>Given a string <code>s</code> that represents a <strong>DNA sequence</strong>, return all the <strong><code>10</code>-letter-long</strong> sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
<strong>Output:</strong> ["AAAAACCCCC","CCCCCAAAAA"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "AAAAAAAAAAAAA"
<strong>Output:</strong> ["AAAAAAAAAA"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;A&#39;</code>, <code>&#39;C&#39;</code>, <code>&#39;G&#39;</code>, or <code>&#39;T&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

<!-- thinking:start -->

> **Thinking**
>
> Length-$10$ substrings that appear at least twice. $n\le 10^5$, so pairwise comparison of all windows is impossible. Slide $s[i..i+9]$, count in a hash map, and append a string the second time it appears.

<!-- thinking:end -->

We define a hash table $cnt$ to store the occurrence count of all substrings of length $10$.

We iterate through all substrings of length $10$ in the string $s$. For the current substring $t$, we update its count in the hash table. If the count of $t$ is $2$, we add it to the answer.

After the iteration, we return the answer array.

The time complexity is $O(n \times 10)$, and the space complexity is $O(n \times 10)$. Here, $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter()
        ans = []
        for i in range(len(s) - 10 + 1):
            t = s[i : i + 10]
            cnt[t] += 1
            if cnt[t] == 2:
                ans.append(t)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Rabin-Karp String Matching Algorithm

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 hashes a length-$10$ slice every step. The alphabet has four letters, so the window is an integer; rolling it in and out is $O(1)$ per step and the total time is $O(n)$.

<!-- thinking:end -->

This method essentially combines sliding window and hash. Similar to 0028. Find the Index of the First Occurrence in a String, this problem can use a hash function to reduce the time complexity of counting subsequences to $O(1)$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string $s$.

<!-- solution:end -->

<!-- problem:end -->
