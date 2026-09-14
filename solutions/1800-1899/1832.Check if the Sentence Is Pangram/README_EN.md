---
comments: true
difficulty: Easy
rating: 1166
source: Weekly Contest 237 Q1
tags:
    - Hash Table
    - String
---

<!-- problem:start -->

# [1832. Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram)

## Description

<!-- description:start -->

<p>A <strong>pangram</strong> is a sentence where every letter of the English alphabet appears at least once.</p>

<p>Given a string <code>sentence</code> containing only lowercase English letters, return<em> </em><code>true</code><em> if </em><code>sentence</code><em> is a <strong>pangram</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;thequickbrownfoxjumpsoverthelazydog&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> sentence contains at least one of every letter of the English alphabet.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;leetcode&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 1000</code></li>
	<li><code>sentence</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Array or Hash Table

<!-- thinking:start -->

> **Thinking**
>
> We must test whether every lowercase letter appears. A linear scan is enough; only the presence set matters.
>
> Insert characters into a set and check whether its size is $26$.

<!-- thinking:end -->

Traverse the string `sentence`, use an array or hash table to record the letters that have appeared, and finally check whether there are $26$ letters in the array or hash table.

The time complexity is $O(n)$, and the space complexity is $O(C)$. Where $n$ is the length of the string `sentence`, and $C$ is the size of the character set. In this problem, $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Bit Manipulation

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 stores a hash set. With only $26$ letters, bit $i$ of an integer $mask$ can mark letter $i$. The sentence is a pangram iff $mask=2^{26}-1$, using constant extra space.

<!-- thinking:end -->

We can also use an integer $mask$ to record the letters that have appeared, where the $i$-th bit of $mask$ indicates whether the $i$-th letter has appeared.

Finally, check whether there are $26$ $1$s in the binary representation of $mask$, that is, check whether $mask$ is equal to $2^{26} - 1$. If so, return `true`, otherwise return `false`.

The time complexity is $O(n)$, where $n$ is the length of the string `sentence`. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mask = 0
        for c in sentence:
            mask |= 1 << (ord(c) - ord('a'))
        return mask == (1 << 26) - 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
