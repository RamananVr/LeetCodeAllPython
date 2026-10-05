---
comments: true
difficulty: Hard
rating: 3039
source: Weekly Contest 379 Q4
tags:
    - Bit Manipulation
    - String
    - Dynamic Programming
    - Bitmask
---

<!-- problem:start -->

# [3003. Maximize the Number of Partitions After Operations](https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> and an integer <code>k</code>.</p>

<p>First, you are allowed to change <strong>at most</strong> <strong>one</strong> index in <code>s</code> to another lowercase English letter.</p>

<p>After that, do the following partitioning operation until <code>s</code> is <strong>empty</strong>:</p>

<ul>
	<li>Choose the <strong>longest</strong> <strong>prefix</strong> of <code>s</code> containing at most <code>k</code> <strong>distinct</strong> characters.</li>
	<li><strong>Delete</strong> the prefix from <code>s</code> and increase the number of partitions by one. The remaining characters (if any) in <code>s</code> maintain their initial order.</li>
</ul>

<p>Return an integer denoting the <strong>maximum</strong> number of resulting partitions after the operations by optimally choosing at most one index to change.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;accca&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal way is to change <code>s[2]</code> to something other than a and c, for example, b. then it becomes <code>&quot;acbca&quot;</code>.</p>

<p>Then we perform the operations:</p>

<ol>
	<li>The longest prefix containing at most 2 distinct characters is <code>&quot;ac&quot;</code>, we remove it and <code>s</code> becomes <code>&quot;bca&quot;</code>.</li>
	<li>Now The longest prefix containing at most 2 distinct characters is <code>&quot;bc&quot;</code>, so we remove it and <code>s</code> becomes <code>&quot;a&quot;</code>.</li>
	<li>Finally, we remove <code>&quot;a&quot;</code> and <code>s</code> becomes empty, so the procedure ends.</li>
</ol>

<p>Doing the operations, the string is divided into 3 partitions, so the answer is 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aabaab&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially&nbsp;<code>s</code>&nbsp;contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;xxyz&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal way is to change&nbsp;<code>s[0]</code>&nbsp;or&nbsp;<code>s[1]</code>&nbsp;to something other than characters in&nbsp;<code>s</code>, for example, to change&nbsp;<code>s[0]</code>&nbsp;to&nbsp;<code>w</code>.</p>

<p>Then&nbsp;<code>s</code>&nbsp;becomes <code>&quot;wxyz&quot;</code>, which consists of 4 distinct characters, so as <code>k</code> is 1, it will divide into 4 partitions.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 26</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoized Search

<!-- thinking:start -->

> **Thinking**
>
> $n \le 10^4$ and we may change one character. Trying every change and resimulating partitions is about $O(n^2 |\Sigma|)$, which is tight.
>
> A cut happens only when the current segment’s distinct-letter set exceeds $k$. That set is a $26$-bit mask and the remaining change is $0$ or $1$, so memoization is feasible.
>
> We therefore search $\textit{dfs}(i, \textit{cur}, t)$: index $i$, segment mask $\textit{cur}$, $t$ changes left. Adding $s[i]$ opens a new segment when the popcount exceeds $k$; if a change remains, we also try every replacement letter.

<!-- thinking:end -->

We design a function $\textit{dfs}(i, \textit{cur}, t)$ that represents the maximum number of partitions we can obtain when currently processing index $i$ of string $s$, the current prefix already contains the character set $\textit{cur}$, and we can still modify $t$ characters. Then the answer is $\textit{dfs}(0, 0, 1)$.

The execution logic of function $\textit{dfs}(i, \textit{cur}, t)$ is as follows:

1. If $i \geq n$, it means we have finished processing string $s$, return 1.
2. Calculate the bitmask $v = 1 \ll (s[i] - 'a')$ corresponding to the current character $s[i]$, and calculate the updated character set $\textit{nxt} = \textit{cur} \mid v$.
3. If the number of bits in $\textit{nxt}$ exceeds $k$, it means the current prefix already contains more than $k$ distinct characters. We need to make a partition, increment the partition count by 1, and recursively call $\textit{dfs}(i + 1, v, t)$. Otherwise, continue recursively calling $\textit{dfs}(i + 1, \textit{nxt}, t)$.
4. If $t > 0$, it means we can still modify a character once. We try to change the current character $s[i]$ to any lowercase letter (26 choices in total). For each choice, calculate the updated character set $\textit{nxt} = \textit{cur} \mid (1 \ll j)$, and based on whether it exceeds $k$ distinct characters, choose the corresponding recursive call method to update the maximum partition count.
5. Use a hash table to cache already computed states to avoid redundant calculations.

The time complexity is $O(n \times |\Sigma| \times k)$ and the space complexity is $O(n \times |\Sigma| \times k)$, where $n$ is the length of string $s$, and $|\Sigma|$ is the size of the character set.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i: int, cur: int, t: int) -> int:
            if i >= n:
                return 1
            v = 1 << (ord(s[i]) - ord("a"))
            nxt = cur | v
            if nxt.bit_count() > k:
                ans = dfs(i + 1, v, t) + 1
            else:
                ans = dfs(i + 1, nxt, t)
            if t:
                for j in range(26):
                    nxt = cur | (1 << j)
                    if nxt.bit_count() > k:
                        ans = max(ans, dfs(i + 1, 1 << j, 0) + 1)
                    else:
                        ans = max(ans, dfs(i + 1, nxt, 0))
            return ans

        n = len(s)
        return dfs(0, 0, 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> $n \le 10^4$ and at most one character may change. Trying every change and then cutting the longest valid prefixes is about $O(n^2 |\Sigma|)$, which is tight.
>
> The unchanged transition always calls the next index first. The chain from index $0$ to $n$ has length $n$. Python raises RecursionError at $n=1500$, and Java and Node overflow at $n=8000$.
>
> A segment is cut when it would contain more than $k$ distinct letters, and only one change is available, so few masks are actually reached at one index. Each state also depends only on the next index.
>
> Record the reachable pairs $(\textit{cur}, t)$ from the left, then fill their maximum partition counts from the right. A finished string is worth $1$. If adding the current letter exceeds $k$, open a new segment and add $1$; while a change remains, also try every replacement letter.

<!-- thinking:end -->

State $(\textit{cur}, t)$ means the open segment already contains the letter mask $\textit{cur}$, and $t$ changes remain. The answer is the value of $(0, 1)$ at index $0$.

First mark the states reachable at every index, starting from $(0, 1)$. Let $v = 1 \ll (s[i] - 'a')$ be the bit of the current letter.

- Let $\textit{nxt} = \textit{cur} \mid v$. If $\textit{nxt}$ has more than $k$ bits, the open segment ends here: the next mask is $v$ and $t$ is unchanged. Otherwise the next mask is $\textit{nxt}$.
- If $t = 1$, also replace $s[i]$ by every lowercase letter. For letter $j$, let $\textit{nxt} = \textit{cur} \mid (1 \ll j)$. When that mask has more than $k$ bits, the next state is mask $1 \ll j$ with no change left. Otherwise the next state is mask $\textit{nxt}$ with no change left.

Then let $i$ run from $n - 1$ down to $0$ and evaluate the same transitions. At $i = n$ the string is finished and the value is $1$. A transition that cuts the open segment adds $1$ to the successor's value.

The time complexity is $O(n \times |\Sigma| \times k)$, and the space complexity is $O(n \times |\Sigma| \times k)$, where $n$ is the length of $s$ and $|\Sigma|$ is the alphabet size.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        masks = [1 << (ord(c) - ord("a")) for c in s]
        reach = [set() for _ in range(n + 1)]
        reach[0].add((0, 1))
        for i, v in enumerate(masks):
            for cur, t in reach[i]:
                nxt = cur | v
                if nxt.bit_count() > k:
                    reach[i + 1].add((v, t))
                else:
                    reach[i + 1].add((nxt, t))
                if t:
                    for j in range(26):
                        bit = 1 << j
                        nxt = cur | bit
                        if nxt.bit_count() > k:
                            reach[i + 1].add((bit, 0))
                        else:
                            reach[i + 1].add((nxt, 0))

        def get(i: int, cur: int, t: int) -> int:
            if i == n:
                return 1
            return f[i][(cur, t)]

        f = [dict() for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            v = masks[i]
            for cur, t in reach[i]:
                nxt = cur | v
                if nxt.bit_count() > k:
                    ans = get(i + 1, v, t) + 1
                else:
                    ans = get(i + 1, nxt, t)
                if t:
                    for j in range(26):
                        bit = 1 << j
                        nxt = cur | bit
                        if nxt.bit_count() > k:
                            ans = max(ans, get(i + 1, bit, 0) + 1)
                        else:
                            ans = max(ans, get(i + 1, nxt, 0))
                f[i][(cur, t)] = ans
        return f[0][(0, 1)]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
