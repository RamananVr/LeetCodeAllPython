---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0734.Sentence%20Similarity/README_EN.md
tags:
    - Array
    - Hash Table
    - String
---

<!-- problem:start -->

# [734. Sentence Similarity 🔒](https://leetcode.com/problems/sentence-similarity)

## Description

<!-- description:start -->

<p>We can represent a sentence as an array of words, for example, the sentence <code>&quot;I am happy with leetcode&quot;</code> can be represented as <code>arr = [&quot;I&quot;,&quot;am&quot;,happy&quot;,&quot;with&quot;,&quot;leetcode&quot;]</code>.</p>

<p>Given two sentences <code>sentence1</code> and <code>sentence2</code> each represented as a string array and given an array of string pairs <code>similarPairs</code> where <code>similarPairs[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> indicates that the two words <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> are similar.</p>

<p>Return <em><code>true</code> if <code>sentence1</code> and <code>sentence2</code> are similar, or <code>false</code> if they are not similar</em>.</p>

<p>Two sentences are similar if:</p>

<ul>
	<li>They have <strong>the same length</strong> (i.e., the same number of words)</li>
	<li><code>sentence1[i]</code> and <code>sentence2[i]</code> are similar.</li>
</ul>

<p>Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words <code>a</code> and <code>b</code> are similar, and the words <code>b</code> and <code>c</code> are similar, <code>a</code> and <code>c</code> are <strong>not necessarily similar</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sentence1 = [&quot;great&quot;,&quot;acting&quot;,&quot;skills&quot;], sentence2 = [&quot;fine&quot;,&quot;drama&quot;,&quot;talent&quot;], similarPairs = [[&quot;great&quot;,&quot;fine&quot;],[&quot;drama&quot;,&quot;acting&quot;],[&quot;skills&quot;,&quot;talent&quot;]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sentence1 = [&quot;great&quot;], sentence2 = [&quot;great&quot;], similarPairs = []
<strong>Output:</strong> true
<strong>Explanation:</strong> A word is similar to itself.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> sentence1 = [&quot;great&quot;], sentence2 = [&quot;doubleplus&quot;,&quot;good&quot;], similarPairs = [[&quot;great&quot;,&quot;doubleplus&quot;]]
<strong>Output:</strong> false
<strong>Explanation:</strong> As they don&#39;t have the same length, we return false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence1.length, sentence2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= sentence1[i].length, sentence2[i].length &lt;= 20</code></li>
	<li><code>sentence1[i]</code> and <code>sentence2[i]</code> consist of English letters.</li>
	<li><code>0 &lt;= similarPairs.length &lt;= 1000</code></li>
	<li><code>similarPairs[i].length == 2</code></li>
	<li><code>1 &lt;= x<sub>i</sub>.length, y<sub>i</sub>.length &lt;= 20</code></li>
	<li><code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> consist of lower-case and upper-case English letters.</li>
	<li>All the pairs <code>(x<sub>i</sub>,<sub> </sub>y<sub>i</sub>)</code> are <strong>distinct</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

First, we check if the lengths of $\textit{sentence1}$ and $\textit{sentence2}$ are equal. If they are not equal, return $\text{false}$.

Then we use a hash table $\textit{s}$ to store all similar word pairs. For each word pair $[x, y]$ in $\textit{similarPairs}$, we add $x$ and $y$ to the hash table $\textit{s}$.

Next, we traverse $\textit{sentence1}$ and $\textit{sentence2}$. For each position $i$, if $\textit{sentence1}[i]$ is not equal to $\textit{sentence2}[i]$, and $(\textit{sentence1}[i], \textit{sentence2}[i])$ and $(\textit{sentence2}[i], \textit{sentence1}[i])$ are not in the hash table $\textit{s}$, then return $\text{false}$.

If the traversal ends without returning $\text{false}$, it means $\textit{sentence1}$ and $\textit{sentence2}$ are similar, so return $\text{true}$.

The time complexity is $O(L)$, and the space complexity is $O(L)$, where $L$ is the sum of the lengths of all strings in the problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        s = {(x, y) for x, y in similarPairs}
        for x, y in zip(sentence1, sentence2):
            if x != y and (x, y) not in s and (y, x) not in s:
                return False
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
