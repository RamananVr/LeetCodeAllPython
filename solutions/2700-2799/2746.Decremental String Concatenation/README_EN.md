---
comments: true
difficulty: Medium
rating: 2126
source: Biweekly Contest 107 Q3
tags:
    - Array
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [2746. Decremental String Concatenation](https://leetcode.com/problems/decremental-string-concatenation)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array <code>words</code> containing <code>n</code> strings.</p>

<p>Let&#39;s define a <strong>join</strong> operation <code>join(x, y)</code> between two strings <code>x</code> and <code>y</code> as concatenating them into <code>xy</code>. However, if the last character of <code>x</code> is equal to the first character of <code>y</code>, one of them is <strong>deleted</strong>.</p>

<p>For example <code>join(&quot;ab&quot;, &quot;ba&quot;) = &quot;aba&quot;</code> and <code>join(&quot;ab&quot;, &quot;cde&quot;) = &quot;abcde&quot;</code>.</p>

<p>You are to perform <code>n - 1</code> <strong>join</strong> operations. Let <code>str<sub>0</sub> = words[0]</code>. Starting from <code>i = 1</code> up to <code>i = n - 1</code>, for the <code>i<sup>th</sup></code> operation, you can do one of the following:</p>

<ul>
	<li>Make <code>str<sub>i</sub> = join(str<sub>i - 1</sub>, words[i])</code></li>
	<li>Make <code>str<sub>i</sub> = join(words[i], str<sub>i - 1</sub>)</code></li>
</ul>

<p>Your task is to <strong>minimize</strong> the length of <code>str<sub>n - 1</sub></code>.</p>

<p>Return <em>an integer denoting the minimum possible length of</em> <code>str<sub>n - 1</sub></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;aa&quot;,&quot;ab&quot;,&quot;bc&quot;]
<strong>Output:</strong> 4
<strong>Explanation: </strong>In this example, we can perform join operations in the following order to minimize the length of str<sub>2</sub>: 
str<sub>0</sub> = &quot;aa&quot;
str<sub>1</sub> = join(str<sub>0</sub>, &quot;ab&quot;) = &quot;aab&quot;
str<sub>2</sub> = join(str<sub>1</sub>, &quot;bc&quot;) = &quot;aabc&quot; 
It can be shown that the minimum possible length of str<sub>2</sub> is 4.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;ab&quot;,&quot;b&quot;]
<strong>Output:</strong> 2
<strong>Explanation:</strong> In this example, str<sub>0</sub> = &quot;ab&quot;, there are two ways to get str<sub>1</sub>: 
join(str<sub>0</sub>, &quot;b&quot;) = &quot;ab&quot; or join(&quot;b&quot;, str<sub>0</sub>) = &quot;bab&quot;. 
The first string, &quot;ab&quot;, has the minimum length. Hence, the answer is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;aaa&quot;,&quot;c&quot;,&quot;aba&quot;]
<strong>Output:</strong> 6
<strong>Explanation:</strong> In this example, we can perform join operations in the following order to minimize the length of str<sub>2</sub>: 
str<sub>0</sub> = &quot;aaa&quot;
str<sub>1</sub> = join(str<sub>0</sub>, &quot;c&quot;) = &quot;aaac&quot;
str<sub>2</sub> = join(&quot;aba&quot;, str<sub>1</sub>) = &quot;abaaac&quot;
It can be shown that the minimum possible length of str<sub>2</sub> is 6.
</pre>

<div class="notranslate" style="all: initial;">&nbsp;</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 50</code></li>
	<li>Each character in <code>words[i]</code> is an English lowercase letter</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

<!-- thinking:start -->

> **Thinking**
>
> Words must be prepended or appended in order; equal touching letters collapse into one, and we want the shortest final length. Two choices per word at $n\le 1000$ make a raw search impossible.
>
> The future cost depends only on the current first and last letters. $dfs(i,a,b)$ is the extra length from word $i$ with ends $a,b$: append compares $s[0]$ with $b$, prepend compares $s[-1]$ with $a$. Memoization yields $O(n\cdot 26^2)$ states.

<!-- thinking:end -->

We notice that when concatenating strings, the first and last characters of the string will affect the length of the concatenated string. Therefore, we design a function $dfs(i, a, b)$, which represents the minimum length of the concatenated string starting from the $i$-th string, and the first character of the previously concatenated string is $a$, and the last character is $b$.

The execution process of the function $dfs(i, a, b)$ is as follows:

- If $i = n$, it means that all strings have been concatenated, return $0$;
- Otherwise, we consider concatenating the $i$-th string to the end or the beginning of the already concatenated string, and get the lengths $x$ and $y$ of the concatenated string, then $dfs(i, a, b) = \min(x, y) + |words[i]|$.

To avoid repeated calculations, we use the method of memoization search. Specifically, we use a three-dimensional array $f$ to store all the return values of $dfs(i, a, b)$. When we need to calculate $dfs(i, a, b)$, if $f[i][a][b]$ has been calculated, we directly return $f[i][a][b]$; otherwise, we calculate the value of $dfs(i, a, b)$ according to the above recurrence relation, and store it in $f[i][a][b]$.

In the main function, we directly return $|words[0]| + dfs(1, words[0][0], words[0][|words[0]| - 1])$.

The time complexity is $O(n \times C^2)$, and the space complexity is $O(n \times C^2)$. Where $C$ represents the maximum length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @cache
        def dfs(i: int, a: str, b: str) -> int:
            if i >= len(words):
                return 0
            s = words[i]
            x = dfs(i + 1, a, s[-1]) - int(s[0] == b)
            y = dfs(i + 1, s[0], b) - int(s[-1] == a)
            return len(s) + min(x, y)

        return len(words[0]) + dfs(1, words[0][0], words[0][-1])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Each word is attached to the left or the right, and equal letters that meet count once. There can be $1000$ words, and trying the right side first always moves to the next index, so the search has depth $n$. Only the current first and last letters affect later choices. Let $f[i][a][b]$ be the extra length from word $i$ with those ends, set $f[n]$ to $0$, and fill decreasing $i$ over every pair of ends.

<!-- thinking:end -->

Let $f[i][a][b]$ be the shortest extra length when connecting from word $i$, with the string so far starting with $a$ and ending with $b$. The boundary is $f[n][a][b]=0$. For $i$ from $n-1$ down to $1$, and for every pair of ends $a,b$, try both sides. Appending $words[i]$ saves one character when its first character equals $b$, and the new end is its last character. Prepending saves one character when its last character equals $a$, and the new start is its first character. $f[i][a][b]$ is the shorter of those two lengths plus $|words[i]|$. The answer is $|words[0]| + f[1][words[0][0]][words[0][|words[0]|-1]]$.

The time complexity is $O(n \times |\Sigma|^2)$, and the space complexity is $O(n \times |\Sigma|^2)$. Here, $n$ is the number of words, and $|\Sigma|$ is the alphabet size, which is $26$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        f = [[[0] * 26 for _ in range(26)] for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            s = words[i]
            m = len(s)
            c, d = ord(s[0]) - 97, ord(s[-1]) - 97
            for a in range(26):
                for b in range(26):
                    x = f[i + 1][a][d] - (c == b)
                    y = f[i + 1][c][b] - (d == a)
                    f[i][a][b] = m + min(x, y)
        a, b = ord(words[0][0]) - 97, ord(words[0][-1]) - 97
        return len(words[0]) + f[1][a][b]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
