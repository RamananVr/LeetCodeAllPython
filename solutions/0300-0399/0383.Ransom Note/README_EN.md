---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0383.Ransom%20Note/README_EN.md
tags:
    - Hash Table
    - String
    - Counting
---

<!-- problem:start -->

# [383. Ransom Note](https://leetcode.com/problems/ransom-note)

## Description

<!-- description:start -->

<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code><em> if </em><code>ransomNote</code><em> can be constructed by using the letters from </em><code>magazine</code><em> and </em><code>false</code><em> otherwise</em>.</p>

<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li>
	<li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table or Array

We can use a hash table or an array $cnt$ of length $26$ to record the number of times each character appears in the string `magazine`. Then traverse the string `ransomNote`, for each character $c$ in it, we decrease the number of $c$ by $1$ in $cnt$. If the number of $c$ is less than $0$ after the decrease, it means that the number of $c$ in `magazine` is not enough, so it cannot be composed of `ransomNote`, just return $false$.

Otherwise, after the traversal, it means that each character in `ransomNote` can be found in `magazine`. Therefore, return $true$.

The time complexity is $O(m + n)$, and the space complexity is $O(C)$. Where $m$ and $n$ are the lengths of the strings `ransomNote` and `magazine` respectively; and $C$ is the size of the character set, which is $26$ in this question.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)
        for c in ransomNote:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
