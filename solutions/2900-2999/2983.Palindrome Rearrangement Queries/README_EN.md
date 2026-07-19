---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2983.Palindrome%20Rearrangement%20Queries/README_EN.md
rating: 2779
source: Weekly Contest 378 Q4
tags:
    - Array
    - Hash Table
    - String
    - Prefix Sum
---

<!-- problem:start -->

# [2983. Palindrome Rearrangement Queries](https://leetcode.com/problems/palindrome-rearrangement-queries)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> string <code>s</code> having an <strong>even</strong> length <code>n</code>.</p>

<p>You are also given a <strong>0-indexed</strong> 2D integer array, <code>queries</code>, where <code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, d<sub>i</sub>]</code>.</p>

<p>For each query <code>i</code>, you are allowed to perform the following operations:</p>

<ul>
	<li>Rearrange the characters within the <strong>substring</strong> <code>s[a<sub>i</sub>:b<sub>i</sub>]</code>, where <code>0 &lt;= a<sub>i</sub> &lt;= b<sub>i</sub> &lt; n / 2</code>.</li>
	<li>Rearrange the characters within the <strong>substring</strong> <code>s[c<sub>i</sub>:d<sub>i</sub>]</code>, where <code>n / 2 &lt;= c<sub>i</sub> &lt;= d<sub>i</sub> &lt; n</code>.</li>
</ul>

<p>For each query, your task is to determine whether it is possible to make <code>s</code> a <strong>palindrome</strong> by performing the operations.</p>

<p>Each query is answered <strong>independently</strong> of the others.</p>

<p>Return <em>a <strong>0-indexed</strong> array </em><code>answer</code><em>, where </em><code>answer[i] == true</code><em> if it is possible to make </em><code>s</code><em> a palindrome by performing operations specified by the </em><code>i<sup>th</sup></code><em> query, and </em><code>false</code><em> otherwise.</em></p>

<ul>
	<li>A <strong>substring</strong> is a contiguous sequence of characters within a string.</li>
	<li><code>s[x:y]</code> represents the substring consisting of characters from the index <code>x</code> to index <code>y</code> in <code>s</code>, <strong>both inclusive</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabc&quot;, queries = [[1,1,3,5],[0,2,5,5]]
<strong>Output:</strong> [true,true]
<strong>Explanation:</strong> In this example, there are two queries:
In the first query:
- a<sub>0</sub> = 1, b<sub>0</sub> = 1, c<sub>0</sub> = 3, d<sub>0</sub> = 5.
- So, you are allowed to rearrange s[1:1] =&gt; a<u>b</u>cabc and s[3:5] =&gt; abc<u>abc</u>.
- To make s a palindrome, s[3:5] can be rearranged to become =&gt; abc<u>cba</u>.
- Now, s is a palindrome. So, answer[0] = true.
In the second query:
- a<sub>1</sub> = 0, b<sub>1</sub> = 2, c<sub>1</sub> = 5, d<sub>1</sub> = 5.
- So, you are allowed to rearrange s[0:2] =&gt; <u>abc</u>abc and s[5:5] =&gt; abcab<u>c</u>.
- To make s a palindrome, s[0:2] can be rearranged to become =&gt; <u>cba</u>abc.
- Now, s is a palindrome. So, answer[1] = true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbcdecbba&quot;, queries = [[0,2,7,9]]
<strong>Output:</strong> [false]
<strong>Explanation:</strong> In this example, there is only one query.
a<sub>0</sub> = 0, b<sub>0</sub> = 2, c<sub>0</sub> = 7, d<sub>0</sub> = 9.
So, you are allowed to rearrange s[0:2] =&gt; <u>abb</u>cdecbba and s[7:9] =&gt; abbcdec<u>bba</u>.
It is not possible to make s a palindrome by rearranging these substrings because s[3:6] is not a palindrome.
So, answer[0] = false.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;acbcab&quot;, queries = [[1,2,4,5]]
<strong>Output:</strong> [true]
<strong>Explanation: </strong>In this example, there is only one query.
a<sub>0</sub> = 1, b<sub>0</sub> = 2, c<sub>0</sub> = 4, d<sub>0</sub> = 5.
So, you are allowed to rearrange s[1:2] =&gt; a<u>cb</u>cab and s[4:5] =&gt; acbc<u>ab</u>.
To make s a palindrome s[1:2] can be rearranged to become a<u>bc</u>cab.
Then, s[4:5] can be rearranged to become abcc<u>ba</u>.
Now, s is a palindrome. So, answer[0] = true.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 4</code></li>
	<li><code>a<sub>i</sub> == queries[i][0], b<sub>i</sub> == queries[i][1]</code></li>
	<li><code>c<sub>i</sub> == queries[i][2], d<sub>i</sub> == queries[i][3]</code></li>
	<li><code>0 &lt;= a<sub>i</sub> &lt;= b<sub>i</sub> &lt; n / 2</code></li>
	<li><code>n / 2 &lt;= c<sub>i</sub> &lt;= d<sub>i</sub> &lt; n </code></li>
	<li><code>n</code> is even.</li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum + Case Discussion

Let's denote the length of string $s$ as $n$, then half of the length is $m = \frac{n}{2}$. Next, we divide string $s$ into two equal-length segments, where the second segment is reversed to get string $t$, and the first segment remains as $s$. For each query $[a_i, b_i, c_i, d_i]$, where $c_i$ and $d_i$ need to be transformed to $n - 1 - d_i$ and $n - 1 - c_i$. The problem is transformed into: for each query $[a_i, b_i, c_i, d_i]$, determine whether $s[a_i, b_i]$ and $t[c_i, d_i]$ can be rearranged to make strings $s$ and $t$ equal.

We preprocess the following information:

1. The prefix sum array $pre_1$ of string $s$, where $pre_1[i][j]$ represents the quantity of character $j$ in the first $i$ characters of string $s$;
2. The prefix sum array $pre_2$ of string $t$, where $pre_2[i][j]$ represents the quantity of character $j$ in the first $i$ characters of string $t$;
3. The difference array $diff$ of strings $s$ and $t$, where $diff[i]$ represents the quantity of different characters in the first $i$ characters of strings $s$ and $t$.

For each query $[a_i, b_i, c_i, d_i]$, let's assume $a_i \le c_i$, then we need to discuss the following cases:

1. The prefix substrings $s[..a_i-1]$ and $t[..a_i-1]$ of strings $s$ and $t$ must be equal, and the suffix substrings $s[\max(b_i, d_i)+1..]$ and $t[\max(b_i, d_i)..]$ must also be equal, otherwise, it is impossible to rearrange to make strings $s$ and $t$ equal;
2. If $d_i \le b_i$, it means the interval $[a_i, b_i]$ contains the interval $[c_i, d_i]$. If the substrings $s[a_i, b_i]$ and $t[a_i, b_i]$ contain the same quantity of characters, then it is possible to rearrange to make strings $s$ and $t$ equal, otherwise, it is impossible;
3. If $b_i < c_i$, it means the intervals $[a_i, b_i]$ and $[c_i, d_i]$ do not intersect. Then the substrings $s[b_i+1, c_i-1]$ and $t[b_i+1, c_i-1]$ must be equal, and the substrings $s[a_i, b_i]$ and $t[a_i, b_i]$ must be equal, and the substrings $s[c_i, d_i]$ and $t[c_i, d_i]$ must be equal, otherwise, it is impossible to rearrange to make strings $s$ and $t$ equal.
4. If $c_i \le b_i < d_i$, it means the intervals $[a_i, b_i]$ and $[c_i, d_i]$ intersect. Then the characters contained in $s[a_i, b_i]$, minus the characters contained in $t[a_i, c_i-1]$, must be equal to the characters contained in $t[c_i, d_i]$, minus the characters contained in $s[b_i+1, d_i]$, otherwise, it is impossible to rearrange to make strings $s$ and $t$ equal.

Based on the above analysis, we iterate through each query $[a_i, b_i, c_i, d_i]$, and determine whether it satisfies the above conditions.

The time complexity is $O((n + q) \times |\Sigma|)$, and the space complexity is $O(n \times |\Sigma|)$. Where $n$ and $q$ are the lengths of string $s$ and the query array $queries$ respectively; and $|\Sigma|$ is the size of the character set. In this problem, the character set is lowercase English letters, so $|\Sigma| = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def count(pre: List[List[int]], i: int, j: int) -> List[int]:
            return [x - y for x, y in zip(pre[j + 1], pre[i])]

        def sub(cnt1: List[int], cnt2: List[int]) -> List[int]:
            res = []
            for x, y in zip(cnt1, cnt2):
                if x - y < 0:
                    return []
                res.append(x - y)
            return res

        def check(
            pre1: List[List[int]], pre2: List[List[int]], a: int, b: int, c: int, d: int
        ) -> bool:
            if diff[a] > 0 or diff[m] - diff[max(b, d) + 1] > 0:
                return False
            if d <= b:
                return count(pre1, a, b) == count(pre2, a, b)
            if b < c:
                return (
                    diff[c] - diff[b + 1] == 0
                    and count(pre1, a, b) == count(pre2, a, b)
                    and count(pre1, c, d) == count(pre2, c, d)
                )
            cnt1 = sub(count(pre1, a, b), count(pre2, a, c - 1))
            cnt2 = sub(count(pre2, c, d), count(pre1, b + 1, d))
            return bool(cnt1) and bool(cnt2) and cnt1 == cnt2

        n = len(s)
        m = n // 2
        t = s[m:][::-1]
        s = s[:m]
        pre1 = [[0] * 26 for _ in range(m + 1)]
        pre2 = [[0] * 26 for _ in range(m + 1)]
        diff = [0] * (m + 1)
        for i, (c1, c2) in enumerate(zip(s, t), 1):
            pre1[i] = pre1[i - 1][:]
            pre2[i] = pre2[i - 1][:]
            pre1[i][ord(c1) - ord("a")] += 1
            pre2[i][ord(c2) - ord("a")] += 1
            diff[i] = diff[i - 1] + int(c1 != c2)
        ans = []
        for a, b, c, d in queries:
            c, d = n - 1 - d, n - 1 - c
            ok = (
                check(pre1, pre2, a, b, c, d)
                if a <= c
                else check(pre2, pre1, c, d, a, b)
            )
            ans.append(ok)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
