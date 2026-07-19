---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0966.Vowel%20Spellchecker/README_EN.md
tags:
    - Array
    - Hash Table
    - String
---

<!-- problem:start -->

# [966. Vowel Spellchecker](https://leetcode.com/problems/vowel-spellchecker)

## Description

<!-- description:start -->

<p>Given a <code>wordlist</code>, we want to implement a spellchecker that converts a query word into a correct word.</p>

<p>For a given <code>query</code> word, the spell checker handles two categories of spelling mistakes:</p>

<ul>
	<li>Capitalization: If the query matches a word in the wordlist (<strong>case-insensitive</strong>), then the query word is returned with the same case as the case in the wordlist.

    <ul>
    	<li>Example: <code>wordlist = [&quot;yellow&quot;]</code>, <code>query = &quot;YellOw&quot;</code>: <code>correct = &quot;yellow&quot;</code></li>
    	<li>Example: <code>wordlist = [&quot;Yellow&quot;]</code>, <code>query = &quot;yellow&quot;</code>: <code>correct = &quot;Yellow&quot;</code></li>
    	<li>Example: <code>wordlist = [&quot;yellow&quot;]</code>, <code>query = &quot;yellow&quot;</code>: <code>correct = &quot;yellow&quot;</code></li>
    </ul>
    </li>
    <li>Vowel Errors: If after replacing the vowels <code>(&#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, &#39;u&#39;)</code> of the query word with any vowel individually, it matches a word in the wordlist (<strong>case-insensitive</strong>), then the query word is returned with the same case as the match in the wordlist.
    <ul>
    	<li>Example: <code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yollow&quot;</code>: <code>correct = &quot;YellOw&quot;</code></li>
    	<li>Example: <code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yeellow&quot;</code>: <code>correct = &quot;&quot;</code> (no match)</li>
    	<li>Example: <code>wordlist = [&quot;YellOw&quot;]</code>, <code>query = &quot;yllw&quot;</code>: <code>correct = &quot;&quot;</code> (no match)</li>
    </ul>
    </li>

</ul>

<p>In addition, the spell checker operates under the following precedence rules:</p>

<ul>
	<li>When the query exactly matches a word in the wordlist (<strong>case-sensitive</strong>), you should return the same word back.</li>
	<li>When the query matches a word up to capitalization, you should return the first such match in the wordlist.</li>
	<li>When the query matches a word up to vowel errors, you should return the first such match in the wordlist.</li>
	<li>If the query has no matches in the wordlist, you should return the empty string.</li>
</ul>

<p>Given some <code>queries</code>, return a list of words <code>answer</code>, where <code>answer[i]</code> is the correct word for <code>query = queries[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
<strong>Output:</strong> ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> wordlist = ["yellow"], queries = ["YellOw"]
<strong>Output:</strong> ["yellow"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= wordlist.length, queries.length &lt;= 5000</code></li>
	<li><code>1 &lt;= wordlist[i].length, queries[i].length &lt;= 7</code></li>
	<li><code>wordlist[i]</code> and <code>queries[i]</code> consist only of only English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We traverse the $\textit{wordlist}$ and store the words in hash tables $\textit{low}$ and $\textit{pat}$ according to case-insensitive and vowel-insensitive rules, respectively. The key of $\textit{low}$ is the lowercase form of the word, and the key of $\textit{pat}$ is the string obtained by replacing the vowels of the word with `*`, with the value being the word itself. We use the hash table $\textit{s}$ to store the words in $\textit{wordlist}$.

We traverse $\textit{queries}$, for each word $\textit{q}$, if $\textit{q}$ is in $\textit{s}$, it means $\textit{q}$ is in $\textit{wordlist}$, and we directly add $\textit{q}$ to the answer array $\textit{ans}$; otherwise, if the lowercase form of $\textit{q}$ is in $\textit{low}$, it means $\textit{q}$ is in $\textit{wordlist}$ and is case-insensitive, and we add $\textit{low}[q.\text{lower}()]$ to the answer array $\textit{ans}$; otherwise, if the string obtained by replacing the vowels of $\textit{q}$ with `*` is in $\textit{pat}$, it means $\textit{q}$ is in $\textit{wordlist}$ and is vowel-insensitive, and we add $\textit{pat}[f(q)]$ to the answer array $\textit{ans}$; otherwise, it means $\textit{q}$ is not in $\textit{wordlist}$, and we add an empty string to the answer array $\textit{ans}$.

Finally, we return the answer array $\textit{ans}$.

The time complexity is $O(n + m)$, and the space complexity is $O(n)$, where $n$ and $m$ are the lengths of $\textit{wordlist}$ and $\textit{queries}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def f(w):
            t = []
            for c in w:
                t.append("*" if c in "aeiou" else c)
            return "".join(t)

        s = set(wordlist)
        low, pat = {}, {}
        for w in wordlist:
            t = w.lower()
            low.setdefault(t, w)
            pat.setdefault(f(t), w)

        ans = []
        for q in queries:
            if q in s:
                ans.append(q)
                continue
            q = q.lower()
            if q in low:
                ans.append(low[q])
                continue
            q = f(q)
            if q in pat:
                ans.append(pat[q])
                continue
            ans.append("")
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
