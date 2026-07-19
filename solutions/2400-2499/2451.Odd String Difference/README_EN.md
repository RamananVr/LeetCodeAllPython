---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2451.Odd%20String%20Difference/README_EN.md
rating: 1406
source: Biweekly Contest 90 Q1
tags:
    - Array
    - Hash Table
    - String
---

<!-- problem:start -->

# [2451. Odd String Difference](https://leetcode.com/problems/odd-string-difference)

## Description

<!-- description:start -->

<p>You are given an array of equal-length strings <code>words</code>. Assume that the length of each string is <code>n</code>.</p>

<p>Each string <code>words[i]</code> can be converted into a <strong>difference integer array</strong> <code>difference[i]</code> of length <code>n - 1</code> where <code>difference[i][j] = words[i][j+1] - words[i][j]</code> where <code>0 &lt;= j &lt;= n - 2</code>. Note that the difference between two letters is the difference between their <strong>positions</strong> in the alphabet i.e.&nbsp;the position of <code>&#39;a&#39;</code> is <code>0</code>, <code>&#39;b&#39;</code> is <code>1</code>, and <code>&#39;z&#39;</code> is <code>25</code>.</p>

<ul>
	<li>For example, for the string <code>&quot;acb&quot;</code>, the difference integer array is <code>[2 - 0, 1 - 2] = [2, -1]</code>.</li>
</ul>

<p>All the strings in words have the same difference integer array, <strong>except one</strong>. You should find that string.</p>

<p>Return<em> the string in </em><code>words</code><em> that has different <strong>difference integer array</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;adc&quot;,&quot;wzy&quot;,&quot;abc&quot;]
<strong>Output:</strong> &quot;abc&quot;
<strong>Explanation:</strong> 
- The difference integer array of &quot;adc&quot; is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of &quot;wzy&quot; is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of &quot;abc&quot; is [1 - 0, 2 - 1] = [1, 1]. 
The odd array out is [1, 1], so we return the corresponding string, &quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;aaa&quot;,&quot;bob&quot;,&quot;ccc&quot;,&quot;ddd&quot;]
<strong>Output:</strong> &quot;bob&quot;
<strong>Explanation:</strong> All the integer arrays are [0, 0] except for &quot;bob&quot;, which corresponds to [13, -13].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= words.length &lt;= 100</code></li>
	<li><code>n == words[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 20</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table Simulation

We use a hash table $d$ to maintain the mapping relationship between the difference array of the string and the string itself, where the difference array is an array composed of the differences of adjacent characters in the string. Since the problem guarantees that except for one string, the difference arrays of other strings are the same, we only need to find the string with a different difference array.

The time complexity is $O(m \times n)$, and the space complexity is $O(m + n)$. Here, $m$ and $n$ are the length of the string and the number of strings, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)
        for s in words:
            t = tuple(ord(b) - ord(a) for a, b in pairwise(s))
            d[t].append(s)
        return next(ss[0] for ss in d.values() if len(ss) == 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- solution:end -->

<!-- problem:end -->
