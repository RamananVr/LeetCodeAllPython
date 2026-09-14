---
comments: true
difficulty: Easy
rating: 1205
source: Weekly Contest 150 Q1
tags:
    - Array
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [1160. Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters)

## Description

<!-- description:start -->

<p>You are given an array of strings <code>words</code> and a string <code>chars</code>.</p>

<p>A string is <strong>good</strong> if it can be formed by characters from <code>chars</code> (each character can only be used once for <strong>each</strong> word in <code>words</code>).</p>

<p>Return <em>the sum of lengths of all good strings in words</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;cat&quot;,&quot;bt&quot;,&quot;hat&quot;,&quot;tree&quot;], chars = &quot;atach&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> The strings that can be formed are &quot;cat&quot; and &quot;hat&quot; so the answer is 3 + 3 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;hello&quot;,&quot;world&quot;,&quot;leetcode&quot;], chars = &quot;welldonehoneyr&quot;
<strong>Output:</strong> 10
<strong>Explanation:</strong> The strings that can be formed are &quot;hello&quot; and &quot;world&quot; so the answer is 5 + 5 = 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length, chars.length &lt;= 100</code></li>
	<li><code>words[i]</code> and <code>chars</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

<!-- thinking:start -->

> **Thinking**
>
> A word is formable iff no letter exceeds the supply in $chars$. Recounting $chars$ for every word repeats work. Count $chars$ once, then compare each word's frequencies: reject if any letter overflows, otherwise add the word length. The alphabet is constant, so each comparison is linear in the word.

<!-- thinking:end -->

We can use an array $cnt$ of length $26$ to count the occurrence of each letter in the string $chars$.

Then we traverse the string array $words$. For each string $w$, we use an array $wc$ of length $26$ to count the occurrence of each letter in the string $w$. If for each letter $c$, $wc[c] \leq cnt[c]$, then we can spell the string $w$ with the letters in $chars$, otherwise we cannot spell the string $w$. If we can spell the string $w$, then we add the length of the string $w$ to the answer.

After the traversal, we can get the answer.

The time complexity is $O(L)$, and the space complexity is $O(C)$. Here, $L$ is the sum of the lengths of all strings in the problem, and $C$ is the size of the character set. In this problem, $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for w in words:
            wc = Counter(w)
            if all(cnt[c] >= v for c, v in wc.items()):
                ans += len(w)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
