---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3144.Minimum%20Substring%20Partition%20of%20Equal%20Character%20Frequency/README_EN.md
rating: 1917
source: Biweekly Contest 130 Q3
tags:
    - Hash Table
    - String
    - Dynamic Programming
    - Counting
---

<!-- problem:start -->

# [3144. Minimum Substring Partition of Equal Character Frequency](https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, you need to partition it into one or more <strong>balanced</strong> <span data-keyword="substring">substrings</span>. For example, if <code>s == &quot;ababcc&quot;</code> then <code>(&quot;abab&quot;, &quot;c&quot;, &quot;c&quot;)</code>, <code>(&quot;ab&quot;, &quot;abc&quot;, &quot;c&quot;)</code>, and <code>(&quot;ababcc&quot;)</code> are all valid partitions, but <code>(&quot;a&quot;, <strong>&quot;bab&quot;</strong>, &quot;cc&quot;)</code>, <code>(<strong>&quot;aba&quot;</strong>, &quot;bc&quot;, &quot;c&quot;)</code>, and <code>(&quot;ab&quot;, <strong>&quot;abcc&quot;</strong>)</code> are not. The unbalanced substrings are bolded.</p>

<p>Return the <strong>minimum</strong> number of substrings that you can partition <code>s</code> into.</p>

<p><strong>Note:</strong> A <strong>balanced</strong> string is a string where each character in the string occurs the same number of times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;fabccddg&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>We can partition the string <code>s</code> into 3 substrings in one of the following ways: <code>(&quot;fab, &quot;ccdd&quot;, &quot;g&quot;)</code>, or <code>(&quot;fabc&quot;, &quot;cd&quot;, &quot;dg&quot;)</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abababaccddb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>We can partition the string <code>s</code> into 2 substrings like so: <code>(&quot;abab&quot;, &quot;abaccddb&quot;)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists only of English lowercase letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoized Search + Hash Table

We design a function $\textit{dfs}(i)$, which represents the minimum number of substrings starting from $s[i]$. The answer is $\textit{dfs}(0)$.

The calculation process of the function $\textit{dfs}(i)$ is as follows:

If $i \geq n$, it means all characters have been processed, so return $0$.

Otherwise, we maintain a hash table $\textit{cnt}$ to represent the frequency of each character in the current substring. Additionally, we maintain a hash table $\textit{freq}$ to represent the frequency of each character's occurrence count.

Then we enumerate $j$ from $i$ to $n-1$, representing the end position of the current substring. For each $j$, we update $\textit{cnt}$ and $\textit{freq}$, then check if the size of $\textit{freq}$ is $1$. If it is, we can split from $j+1$, and the answer is $1 + \textit{dfs}(j+1)$. We take the minimum answer among all $j$ as the return value of the function.

To avoid repeated calculations, we use memoized search.

The time complexity is $O(n^2)$, and the space complexity is $O(n \times |\Sigma|)$. Here, $n$ is the length of the string $s$, and $|\Sigma|$ represents the size of the character set, which is $26$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            cnt = defaultdict(int)
            freq = defaultdict(int)
            ans = n - i
            for j in range(i, n):
                if cnt[s[j]]:
                    freq[cnt[s[j]]] -= 1
                    if not freq[cnt[s[j]]]:
                        freq.pop(cnt[s[j]])
                cnt[s[j]] += 1
                freq[cnt[s[j]]] += 1
                if len(freq) == 1 and (t := 1 + dfs(j + 1)) < ans:
                    ans = t
            return ans

        n = len(s)
        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Memoized Search (Optimization)

We can optimize Solution 1 by not maintaining the $\textit{freq}$ hash table. Instead, we only need to maintain a hash table $\textit{cnt}$, which represents the frequency of each character in the current substring. Additionally, we maintain two variables $k$ and $m$ to represent the number of distinct characters in the current substring and the maximum frequency of any character, respectively. For a substring $s[i..j]$, if $j-i+1 = m \times k$, then this substring is a balanced substring.

The time complexity is $O(n^2)$, and the space complexity is $O(n \times |\Sigma|)$. Here, $n$ is the length of the string $s$, and $|\Sigma|$ represents the size of the character set, which is $26$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            cnt = defaultdict(int)
            m = 0
            ans = n - i
            for j in range(i, n):
                cnt[s[j]] += 1
                m = max(m, cnt[s[j]])
                if j - i + 1 == m * len(cnt):
                    ans = min(ans, 1 + dfs(j + 1))
            return ans

        n = len(s)
        ans = dfs(0)
        dfs.cache_clear()
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming

We can convert the memoized search into dynamic programming. Define the state $f[i]$ as the minimum number of substrings required to partition the first $i$ characters. Initially, $f[0] = 0$, and the rest $f[i] = +\infty$ or $f[i] = n$.

Next, we enumerate $i$ from $0$ to $n-1$. For each $i$, we maintain a hash table $\textit{cnt}$ to represent the frequency of each character in the current substring. Additionally, we maintain two variables $k$ and $m$ to represent the number of distinct characters in the current substring and the maximum frequency of any character, respectively. For a substring $s[j..i]$, if $i-j+1 = m \times k$, then this substring is a balanced substring. At this point, we can partition from $j$, so $f[i+1] = \min(f[i+1], f[j] + 1)$.

The final answer is $f[n]$.

The time complexity is $O(n^2)$, and the space complexity is $O(n + |\Sigma|)$. Here, $n$ is the length of the string $s$, and $|\Sigma|$ represents the size of the character set, which is $26$ in this problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        f = [inf] * (n + 1)
        f[0] = 0
        for i in range(n):
            cnt = defaultdict(int)
            m = 0
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                m = max(m, cnt[s[j]])
                if i - j + 1 == len(cnt) * m:
                    f[i + 1] = min(f[i + 1], f[j] + 1)
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
