---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0784.Letter%20Case%20Permutation/README_EN.md
tags:
    - Bit Manipulation
    - String
    - Backtracking
---

<!-- problem:start -->

# [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, you&nbsp;can transform every letter individually to be lowercase or uppercase to create another string.</p>

<p>Return <em>a list of all possible strings we could create</em>. Return the output in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a1b2&quot;
<strong>Output:</strong> [&quot;a1b2&quot;,&quot;a1B2&quot;,&quot;A1b2&quot;,&quot;A1B2&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;3z4&quot;
<strong>Output:</strong> [&quot;3z4&quot;,&quot;3Z4&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 12</code></li>
	<li><code>s</code> consists of lowercase English letters, uppercase English letters, and digits.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

Since each letter in $s$ can be converted to uppercase or lowercase, we can use the DFS (Depth-First Search) method to enumerate all possible cases.

Specifically, traverse the string $s$ from left to right. For each letter encountered, you can choose to convert it to uppercase or lowercase, and then continue to traverse the subsequent letters. When you reach the end of the string, you get a conversion scheme and add it to the answer.

The method of converting case can be implemented using bitwise operations. For a letter, the difference between the ASCII codes of its lowercase and uppercase forms is $32$, so we can achieve case conversion by XORing the ASCII code of the letter with $32$.

The time complexity is $O(n \times 2^n)$, where $n$ is the length of the string $s$. For each letter, we can choose to convert it to uppercase or lowercase, so there are $2^n$ conversion schemes in total. For each conversion scheme, we need $O(n)$ time to generate a new string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(i: int) -> None:
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                t[i] = chr(ord(t[i]) ^ 32)
                dfs(i + 1)

        t = list(s)
        ans = []
        dfs(0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Binary Enumeration

For a letter, we can convert it to uppercase or lowercase. Therefore, for each letter, we can use a binary bit to represent its conversion scheme, where $1$ represents lowercase and $0$ represents uppercase.

First, we count the number of letters in the string $s$, denoted as $n$. Then, there are $2^n$ conversion schemes in total. We can use each bit of a binary number to represent the conversion scheme of each letter, enumerating from $0$ to $2^n-1$.

Specifically, we can use a variable $i$ to represent the current binary number being enumerated, where the $j$-th bit of $i$ represents the conversion scheme of the $j$-th letter. That is, the $j$-th bit of $i$ being $1$ means the $j$-th letter is converted to lowercase, and $0$ means the $j$-th letter is converted to uppercase.

The time complexity is $O(n \times 2^n)$, where $n$ is the length of the string $s$. For each letter, we can choose to convert it to uppercase or lowercase, so there are $2^n$ conversion schemes in total. For each conversion scheme, we need $O(n)$ time to generate a new string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = sum(c.isalpha() for c in s)
        for i in range(1 << n):
            j, t = 0, []
            for c in s:
                if c.isalpha():
                    c = c.lower() if (i >> j) & 1 else c.upper()
                    j += 1
                t.append(c)
            ans.append(''.join(t))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
