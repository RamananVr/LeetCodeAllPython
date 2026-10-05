---
comments: true
difficulty: Medium
rating: 2081
source: Weekly Contest 415 Q3
tags:
    - Greedy
    - Trie
    - Segment Tree
    - Array
    - String
    - Binary Search
    - Dynamic Programming
    - String Matching
    - Hash Function
    - Rolling Hash
---

<!-- problem:start -->

# [3291. Minimum Number of Valid Strings to Form Target I](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i)

## Description

<!-- description:start -->

<p>You are given an array of strings <code>words</code> and a string <code>target</code>.</p>

<p>A string <code>x</code> is called <strong>valid</strong> if <code>x</code> is a <span data-keyword="string-prefix">prefix</span> of <strong>any</strong> string in <code>words</code>.</p>

<p>Return the <strong>minimum</strong> number of <strong>valid</strong> strings that can be <em>concatenated</em> to form <code>target</code>. If it is <strong>not</strong> possible to form <code>target</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abc&quot;,&quot;aaaaa&quot;,&quot;bcdef&quot;], target = &quot;aabcdabc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The target string can be formed by concatenating:</p>

<ul>
	<li>Prefix of length 2 of <code>words[1]</code>, i.e. <code>&quot;aa&quot;</code>.</li>
	<li>Prefix of length 3 of <code>words[2]</code>, i.e. <code>&quot;bcd&quot;</code>.</li>
	<li>Prefix of length 3 of <code>words[0]</code>, i.e. <code>&quot;abc&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abababab&quot;,&quot;ab&quot;], target = &quot;ababaababa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The target string can be formed by concatenating:</p>

<ul>
	<li>Prefix of length 5 of <code>words[0]</code>, i.e. <code>&quot;ababa&quot;</code>.</li>
	<li>Prefix of length 5 of <code>words[0]</code>, i.e. <code>&quot;ababa&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abcdef&quot;], target = &quot;xyz&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 5 * 10<sup>3</sup></code></li>
	<li>The input is generated such that <code>sum(words[i].length) &lt;= 10<sup>5</sup></code>.</li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= target.length &lt;= 5 * 10<sup>3</sup></code></li>
	<li><code>target</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Trie + Memoization

<!-- thinking:start -->

> **Thinking**
>
> Concatenate prefixes of $\textit{words}$ to form $\textit{target}$ with as few pieces as possible. $|target|\le 5\times 10^3$ and total word length $10^5$; trying every word at every index repeats prefixes.
>
> Store every word in a trie. From $i$, walk $\textit{target}$ down the trie; each existing node is a cut, plus $\textit{dfs}(j+1)$. After memoization each start walks at most $O(n)$.

<!-- thinking:end -->

We can use a trie to store all valid strings and then use memoization to calculate the answer.

We design a function $\textit{dfs}(i)$, which represents the minimum number of strings needed to concatenate starting from the $i$-th character of the string $\textit{target}$. The answer is $\textit{dfs}(0)$.

The function $\textit{dfs}(i)$ is calculated as follows:

- If $i \geq n$, it means the string $\textit{target}$ has been completely traversed, so we return $0$;
- Otherwise, we can find valid strings in the trie that start with $\textit{target}[i]$, and then recursively calculate $\textit{dfs}(i + \text{len}(w))$, where $w$ is the valid string found. We take the minimum of these values and add $1$ as the return value of $\textit{dfs}(i)$.

To avoid redundant calculations, we use memoization.

The time complexity is $O(n^2 + L)$, and the space complexity is $O(n + L)$. Here, $n$ is the length of the string $\textit{target}$, and $L$ is the total length of all valid strings.

<!-- tabs:start -->

#### Python3

```python
def min(a: int, b: int) -> int:
    return a if a < b else b

class Trie:
    def __init__(self):
        self.children: List[Optional[Trie]] = [None] * 26

    def insert(self, w: str):
        node = self
        for i in map(lambda c: ord(c) - 97, w):
            if node.children[i] is None:
                node.children[i] = Trie()
            node = node.children[i]

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            node = trie
            ans = inf
            for j in range(i, n):
                k = ord(target[j]) - 97
                if node.children[k] is None:
                    break
                node = node.children[k]
                ans = min(ans, 1 + dfs(j + 1))
            return ans

        trie = Trie()
        for w in words:
            trie.insert(w)
        n = len(target)
        ans = dfs(0)
        return ans if ans < inf else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Trie + Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Trying every word at every index repeats prefixes. $|target|$ can reach $5\times 10^3$, and whenever $\textit{target}[i]$ is the first letter of some word the first call always lands on $i+1$, so the chain has depth $n$. A piece must be a prefix of some word, so the fewest pieces from $i$ depend only on later indices. Store the words in a trie, set $f[n]=0$, and fill $i$ from $n-1$ down to $0$: walk $\textit{target}$ down the trie and update $f[i]$ with $1+f[j+1]$ at every existing node. If $f[0]$ is still at least the sentinel, return $-1$.

<!-- thinking:end -->

We store every string in $\textit{words}$ in a trie. Let $f[i]$ be the minimum number of strings needed starting from index $i$ of $\textit{target}$, with $f[n] = 0$. The answer is $f[0]$.

Scan $i$ from $n - 1$ down to $0$. Starting from the trie root, walk down $\textit{target}[i..]$. Each time the walk enters an existing node, that prefix is a valid string, and we update $f[i]$ with $1 + f[j + 1]$.

If $f[0]$ is at least the preset upper bound, $\textit{target}$ cannot be formed and we return $-1$. Otherwise we return $f[0]$.

The time complexity is $O(n^2 + L)$, and the space complexity is $O(n + L)$. Here, $n$ is the length of $\textit{target}$, and $L$ is the total length of all valid strings.

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children: List[Optional[Trie]] = [None] * 26

    def insert(self, w: str):
        node = self
        for i in map(lambda c: ord(c) - 97, w):
            if node.children[i] is None:
                node.children[i] = Trie()
            node = node.children[i]

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        n = len(target)
        f = [inf] * (n + 1)
        f[n] = 0
        for i in range(n - 1, -1, -1):
            node = trie
            for j in range(i, n):
                k = ord(target[j]) - 97
                if node.children[k] is None:
                    break
                node = node.children[k]
                f[i] = min(f[i], 1 + f[j + 1])
        return f[0] if f[0] < inf else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
