---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1657.Determine%20if%20Two%20Strings%20Are%20Close/README_EN.md
rating: 1530
source: Weekly Contest 215 Q2
tags:
    - Hash Table
    - String
    - Counting
    - Sorting
---

<!-- problem:start -->

# [1657. Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close)

## Description

<!-- description:start -->

<p>Two strings are considered <strong>close</strong> if you can attain one from the other using the following operations:</p>

<ul>
	<li>Operation 1: Swap any two <strong>existing</strong> characters.

    <ul>
    	<li>For example, <code>a<u>b</u>cd<u>e</u> -&gt; a<u>e</u>cd<u>b</u></code></li>
    </ul>
    </li>
    <li>Operation 2: Transform <strong>every</strong> occurrence of one <strong>existing</strong> character into another <strong>existing</strong> character, and do the same with the other character.
    <ul>
    	<li>For example, <code><u>aa</u>c<u>abb</u> -&gt; <u>bb</u>c<u>baa</u></code> (all <code>a</code>&#39;s turn into <code>b</code>&#39;s, and all <code>b</code>&#39;s turn into <code>a</code>&#39;s)</li>
    </ul>
    </li>

</ul>

<p>You can use the operations on either string as many times as necessary.</p>

<p>Given two strings, <code>word1</code> and <code>word2</code>, return <code>true</code><em> if </em><code>word1</code><em> and </em><code>word2</code><em> are <strong>close</strong>, and </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;abc&quot;, word2 = &quot;bca&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> You can attain word2 from word1 in 2 operations.
Apply Operation 1: &quot;a<u>bc</u>&quot; -&gt; &quot;a<u>cb</u>&quot;
Apply Operation 1: &quot;<u>a</u>c<u>b</u>&quot; -&gt; &quot;<u>b</u>c<u>a</u>&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;a&quot;, word2 = &quot;aa&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>It is impossible to attain word2 from word1, or vice versa, in any number of operations.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;cabbba&quot;, word2 = &quot;abbccc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> You can attain word2 from word1 in 3 operations.
Apply Operation 1: &quot;ca<u>b</u>bb<u>a</u>&quot; -&gt; &quot;ca<u>a</u>bb<u>b</u>&quot;
Apply Operation 2: &quot;<u>c</u>aa<u>bbb</u>&quot; -&gt; &quot;<u>b</u>aa<u>ccc</u>&quot;
Apply Operation 2: &quot;<u>baa</u>ccc&quot; -&gt; &quot;<u>abb</u>ccc&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word1</code> and <code>word2</code> contain only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Sorting

According to the problem description, two strings are close if they meet the following two conditions simultaneously:

1. The strings `word1` and `word2` must contain the same types of letters.
2. The arrays obtained by sorting the counts of all characters in `word1` and `word2` must be the same.

Therefore, we can first use an array or hash table to count the occurrences of each letter in `word1` and `word2` respectively, and then compare whether they are the same. If they are not the same, return `false` early.

Otherwise, we sort the corresponding counts, and then compare whether the counts at the corresponding positions are the same. If they are not the same, return `false`.

At the end of the traversal, return `true`.

The time complexity is $O(m + n + C \times \log C)$, and the space complexity is $O(C)$. Here, $m$ and $n$ are the lengths of the strings `word1` and `word2` respectively, and $C$ is the number of letter types. In this problem, $C=26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return sorted(cnt1.values()) == sorted(cnt2.values()) and set(
            cnt1.keys()
        ) == set(cnt2.keys())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
