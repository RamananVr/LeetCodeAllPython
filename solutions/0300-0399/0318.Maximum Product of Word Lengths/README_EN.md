---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0318.Maximum%20Product%20of%20Word%20Lengths/README_EN.md
tags:
    - Bit Manipulation
    - Array
    - String
---

<!-- problem:start -->

# [318. Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths)

## Description

<!-- description:start -->

<p>Given a string array <code>words</code>, return <em>the maximum value of</em> <code>length(word[i]) * length(word[j])</code> <em>where the two words do not share common letters</em>. If no such two words exist, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;xtfn&quot;,&quot;abcdef&quot;]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The two words can be &quot;abcw&quot;, &quot;xtfn&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The two words can be &quot;ab&quot;, &quot;cd&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> No such pair of words.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bit Manipulation

The problem requires us to find two strings without common letters, so that their length product is maximized. We can represent each string with a binary number $mask[i]$, where each bit of this binary number indicates whether the string contains a certain letter. If two strings do not have common letters, then the bitwise AND result of the two binary numbers corresponding to these strings is $0$, that is, $mask[i] \& mask[j] = 0$.

We traverse each string. For the current string $words[i]$ we are traversing, we first calculate the corresponding binary number $mask[i]$, and then traverse all strings $words[j]$ where $j \in [0, i)$. We check whether $mask[i] \& mask[j] = 0$ holds. If it holds, we update the answer to $\max(ans, |words[i]| \times |words[j]|)$.

After the traversal, we return the answer.

The time complexity is $O(n^2 + L)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string array $words$, and $L$ is the sum of the lengths of all strings in the string array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0] * len(words)
        ans = 0
        for i, s in enumerate(words):
            for c in s:
                mask[i] |= 1 << (ord(c) - ord("a"))
            for j, t in enumerate(words[:i]):
                if (mask[i] & mask[j]) == 0:
                    ans = max(ans, len(s) * len(t))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = defaultdict(int)
        ans = 0
        for s in words:
            a = len(s)
            x = 0
            for c in s:
                x |= 1 << (ord(c) - ord("a"))
            for y, b in mask.items():
                if (x & y) == 0:
                    ans = max(ans, a * b)
            mask[x] = max(mask[x], a)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
