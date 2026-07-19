---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2700-2799/2707.Extra%20Characters%20in%20a%20String/README_EN.md
rating: 1735
source: Biweekly Contest 105 Q2
tags:
    - Trie
    - Array
    - Hash Table
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [2707. Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> string <code>s</code> and a dictionary of words <code>dictionary</code>. You have to break <code>s</code> into one or more <strong>non-overlapping</strong> substrings such that each substring is present in <code>dictionary</code>. There may be some <strong>extra characters</strong> in <code>s</code> which are not present in any of the substrings.</p>

<p>Return <em>the <strong>minimum</strong> number of extra characters left over if you break up </em><code>s</code><em> optimally.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetscode&quot;, dictionary = [&quot;leet&quot;,&quot;code&quot;,&quot;leetcode&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can break s in two substrings: &quot;leet&quot; from index 0 to 3 and &quot;code&quot; from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;sayhelloworld&quot;, dictionary = [&quot;hello&quot;,&quot;world&quot;]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can break s in two substrings: &quot;hello&quot; from index 3 to 7 and &quot;world&quot; from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 50</code></li>
	<li><code>dictionary[i]</code>&nbsp;and <code>s</code> consists of only lowercase English letters</li>
	<li><code>dictionary</code> contains distinct words</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Dynamic Programming

We can use a hash table $ss$ to record all words in the dictionary, which allows us to quickly determine whether a string is in the dictionary.

Next, we define $f[i]$ to represent the minimum number of extra characters in the first $i$ characters of string $s$, initially $f[0] = 0$.

When $i \ge 1$, the $i$th character $s[i - 1]$ can be an extra character, in which case $f[i] = f[i - 1] + 1$. If there exists an index $j \in [0, i - 1]$ such that $s[j..i)$ is in the hash table $ss$, then we can take $s[j..i)$ as a word, in which case $f[i] = f[j]$.

In summary, we can get the state transition equation:

$$
f[i] = \min \{ f[i - 1] + 1, \min_{j \in [0, i - 1]} f[j] \}
$$

where $i \ge 1$, and $j \in [0, i - 1]$ and $s[j..i)$ is in the hash table $ss$.

The final answer is $f[n]$.

The time complexity is $O(n^3 + L)$, and the space complexity is $O(n + L)$. Here, $n$ is the length of string $s$, and $L$ is the sum of the lengths of all words in the dictionary.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ss = set(dictionary)
        n = len(s)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(i):
                if s[j:i] in ss and f[j] < f[i]:
                    f[i] = f[j]
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Trie + Dynamic Programming

We can use a trie to optimize the time complexity of Solution 1.

Specifically, we first insert each word in the dictionary into the trie $root$ in reverse order, then we define $f[i]$ to represent the minimum number of extra characters in the first $i$ characters of string $s$, initially $f[0] = 0$.

When $i \ge 1$, the $i$th character $s[i - 1]$ can be an extra character, in which case $f[i] = f[i - 1] + 1$. We can also enumerate the index $j$ in reverse order in the range $[0..i-1]$, and determine whether $s[j..i)$ is in the trie $root$. If it exists, then we can take $s[j..i)$ as a word, in which case $f[i] = f[j]$.

The time complexity is $O(n^2 + L)$, and the space complexity is $O(n + L \times |\Sigma|)$. Here, $n$ is the length of string $s$, and $L$ is the sum of the lengths of all words in the dictionary. Additionally, $|\Sigma|$ is the size of the character set. In this problem, the character set is lowercase English letters, so $|\Sigma| = 26$.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = ['children', 'is_end']

    def __init__(self):
        self.children: List[Node | None] = [None] * 26
        self.is_end = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Node()
        for w in dictionary:
            node = root
            for c in w[::-1]:
                i = ord(c) - ord('a')
                if node.children[i] is None:
                    node.children[i] = Node()
                node = node.children[i]
            node.is_end = True

        n = len(s)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            node = root
            for j in range(i - 1, -1, -1):
                node = node.children[ord(s[j]) - ord('a')]
                if node is None:
                    break
                if node.is_end and f[j] < f[i]:
                    f[i] = f[j]
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
