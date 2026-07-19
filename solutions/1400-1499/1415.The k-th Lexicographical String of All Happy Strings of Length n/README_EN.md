---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1415.The%20k-th%20Lexicographical%20String%20of%20All%20Happy%20Strings%20of%20Length%20n/README_EN.md
rating: 1575
source: Biweekly Contest 24 Q3
tags:
    - String
    - Backtracking
---

<!-- problem:start -->

# [1415. The k-th Lexicographical String of All Happy Strings of Length n](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n)

## Description

<!-- description:start -->

<p>A <strong>happy string</strong> is a string that:</p>

<ul>
	<li>consists only of letters of the set <code>[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</code>.</li>
	<li><code>s[i] != s[i + 1]</code> for all values of <code>i</code> from <code>1</code> to <code>s.length - 1</code> (string is 1-indexed).</li>
</ul>

<p>For example, strings <strong>&quot;abc&quot;, &quot;ac&quot;, &quot;b&quot;</strong> and <strong>&quot;abcbabcbcb&quot;</strong> are all happy strings and strings <strong>&quot;aa&quot;, &quot;baa&quot;</strong> and <strong>&quot;ababbc&quot;</strong> are not happy strings.</p>

<p>Given two integers <code>n</code> and <code>k</code>, consider a list of all happy strings of length <code>n</code> sorted in lexicographical order.</p>

<p>Return <em>the kth string</em> of this list or return an <strong>empty string</strong> if there are less than <code>k</code> happy strings of length <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 3
<strong>Output:</strong> &quot;c&quot;
<strong>Explanation:</strong> The list [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;] contains all happy strings of length 1. The third string is &quot;c&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 4
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There are only 3 happy strings of length 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 9
<strong>Output:</strong> &quot;cab&quot;
<strong>Explanation:</strong> There are 12 different happy string of length 3 [&quot;aba&quot;, &quot;abc&quot;, &quot;aca&quot;, &quot;acb&quot;, &quot;bab&quot;, &quot;bac&quot;, &quot;bca&quot;, &quot;bcb&quot;, &quot;cab&quot;, &quot;cac&quot;, &quot;cba&quot;, &quot;cbc&quot;]. You will find the 9<sup>th</sup> string = &quot;cab&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

We use a string $\textit{s}$ to record the current string, initially an empty string. Then, we design a function $\text{dfs}$ to generate all happy strings of length $n$.

The implementation of the function $\text{dfs}$ is as follows:

1. If the length of the current string is equal to $n$, add the current string to the answer array $\textit{ans}$ and return;
2. If the length of the answer array is greater than or equal to $k$, return directly;
3. Otherwise, we iterate over the character set $\{a, b, c\}$. For each character $c$, if the current string is empty or the last character of the current string is not equal to $c$, add the character $c$ to the current string, then recursively call $\text{dfs}$. After the recursion ends, remove the last character of the current string.

Finally, we check if the length of the answer array is less than $k$. If it is, return an empty string; otherwise, return the $k$-th element of the answer array.

The time complexity is $O(n \times 2^n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs():
            if len(s) == n:
                ans.append("".join(s))
                return
            if len(ans) >= k:
                return
            for c in "abc":
                if not s or s[-1] != c:
                    s.append(c)
                    dfs()
                    s.pop()

        ans = []
        s = []
        dfs()
        return "" if len(ans) < k else ans[k - 1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Mathematics

We can directly calculate what the $k$-th happy string is, without generating all happy strings.

Starting from the first happy string of length $n$, we can determine what each character position should be.

For a happy string of length $n$, the first character has $3$ choices, the second character has $2$ choices (cannot be the same as the first), the third character also has $2$ choices (cannot be the same as the second), and so on, until the $n$-th character also has $2$ choices (cannot be the same as the $(n-1)$-th). Therefore, the total number of happy strings of length $n$ is $3 \times 2^{n-1}$.

If $k$ is greater than the total number of happy strings of length $n$, we return an empty string directly.

Otherwise, we start from the first character and determine each character's position one by one. For the $i$-th character, we enumerate the character set $\{a, b, c\}$. If the last character of the current string is not equal to $c$, we calculate the number of remaining happy strings. If $k$ is less than or equal to that count, we append character $c$ to the current string and move on to the next position; otherwise, we subtract that count from $k$ and continue enumerating the next character.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
        cs = "abc"
        ans = []
        for i in range(n):
            remain = 1 << (n - i - 1)
            for c in cs:
                if ans and ans[-1] == c:
                    continue
                if k <= remain:
                    ans.append(c)
                    break
                k -= remain
        return "".join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
