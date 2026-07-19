---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1147.Longest%20Chunked%20Palindrome%20Decomposition/README_EN.md
rating: 1912
source: Weekly Contest 148 Q4
tags:
    - Greedy
    - Two Pointers
    - String
    - Dynamic Programming
    - Hash Function
    - Rolling Hash
---

<!-- problem:start -->

# [1147. Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition)

## Description

<!-- description:start -->

<p>You are given a string <code>text</code>. You should split it to k substrings <code>(subtext<sub>1</sub>, subtext<sub>2</sub>, ..., subtext<sub>k</sub>)</code> such that:</p>

<ul>
	<li><code>subtext<sub>i</sub></code> is a <strong>non-empty</strong> string.</li>
	<li>The concatenation of all the substrings is equal to <code>text</code> (i.e., <code>subtext<sub>1</sub> + subtext<sub>2</sub> + ... + subtext<sub>k</sub> == text</code>).</li>
	<li><code>subtext<sub>i</sub> == subtext<sub>k - i + 1</sub></code> for all valid values of <code>i</code> (i.e., <code>1 &lt;= i &lt;= k</code>).</li>
</ul>

<p>Return the largest possible value of <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;ghiabcdefhelloadamhelloabcdefghi&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> We can split the string on &quot;(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;merchant&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can split the string on &quot;(merchant)&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;antaprezatepzapreanta&quot;
<strong>Output:</strong> 11
<strong>Explanation:</strong> We can split the string on &quot;(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 1000</code></li>
	<li><code>text</code> consists only of lowercase English characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Two Pointers

We can start from both ends of the string, looking for the shortest, identical, and non-overlapping prefixes and suffixes:

- If such prefixes and suffixes cannot be found, then the entire string is treated as a segmented palindrome, and the answer is incremented by $1$;
- If such prefixes and suffixes are found, then this prefix and suffix are treated as a segmented palindrome, and the answer is incremented by $2$, then continue to find the prefixes and suffixes of the remaining string.

The proof of the above greedy strategy is as follows:

Suppose there is a prefix $A_1$ and a suffix $A_2$ that meet the conditions, and there is a prefix $B_1$ and a suffix $B_4$ that meet the conditions. Since $A_1 = A_2$ and $B_1=B_4$, then $B_3=B_1=B_4=B_2$, and $C_1 = C_2$. Therefore, if we greedily split $B_1$ and $B_4$, then the remaining $C_1$ and $C_2$, and $B_2$ and $B_3$ can also be successfully split. Therefore, we should greedily choose the shortest identical prefix and suffix to split, so that in the remaining string, more segmented palindromes may be split.

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1147.Longest%20Chunked%20Palindrome%20Decomposition/images/demo.png" style="width: 300px;" /></p>

The time complexity is $O(n^2)$, and the space complexity is $O(n)$ or $O(1)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestDecomposition(self, text: str) -> int:
        ans = 0
        i, j = 0, len(text) - 1
        while i <= j:
            k = 1
            ok = False
            while i + k - 1 < j - k + 1:
                if text[i : i + k] == text[j - k + 1 : j + 1]:
                    ans += 2
                    i += k
                    j -= k
                    ok = True
                    break
                k += 1
            if not ok:
                ans += 1
                break
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: String Hash

**String hash** is to map a string of any length to a non-negative integer, and its collision probability is almost $0$. String hash is used to calculate the hash value of a string and quickly determine whether two strings are equal.

Therefore, based on Solution 1, we can use the method of string hash to compare whether two strings are equal in $O(1)$ time.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestDecomposition(self, text: str) -> int:
        def get(l, r):
            return (h[r] - h[l - 1] * p[r - l + 1]) % mod

        n = len(text)
        base = 131
        mod = int(1e9) + 7
        h = [0] * (n + 10)
        p = [1] * (n + 10)
        for i, c in enumerate(text):
            t = ord(c) - ord('a') + 1
            h[i + 1] = (h[i] * base) % mod + t
            p[i + 1] = (p[i] * base) % mod

        ans = 0
        i, j = 0, n - 1
        while i <= j:
            k = 1
            ok = False
            while i + k - 1 < j - k + 1:
                if get(i + 1, i + k) == get(j - k + 2, j + 1):
                    ans += 2
                    i += k
                    j -= k
                    ok = True
                    break
                k += 1
            if not ok:
                ans += 1
                break
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
