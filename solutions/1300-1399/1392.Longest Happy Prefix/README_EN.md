---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1392.Longest%20Happy%20Prefix/README_EN.md
rating: 1876
source: Weekly Contest 181 Q4
tags:
    - String
    - String Matching
    - Hash Function
    - Rolling Hash
---

<!-- problem:start -->

# [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix)

## Description

<!-- description:start -->

<p>A string is called a <strong>happy prefix</strong> if is a <strong>non-empty</strong> prefix which is also a suffix (excluding itself).</p>

<p>Given a string <code>s</code>, return <em>the <strong>longest happy prefix</strong> of</em> <code>s</code>. Return an empty string <code>&quot;&quot;</code> if no such prefix exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;level&quot;
<strong>Output:</strong> &quot;l&quot;
<strong>Explanation:</strong> s contains 4 prefix excluding itself (&quot;l&quot;, &quot;le&quot;, &quot;lev&quot;, &quot;leve&quot;), and suffix (&quot;l&quot;, &quot;el&quot;, &quot;vel&quot;, &quot;evel&quot;). The largest prefix which is also suffix is given by &quot;l&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababab&quot;
<strong>Output:</strong> &quot;abab&quot;
<strong>Explanation:</strong> &quot;abab&quot; is the largest prefix which is also suffix. They can overlap in the original string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: String Hashing

**String Hashing** is a method to map a string of any length to a non-negative integer, with the probability of collision being almost zero. String hashing is used to calculate the hash value of a string, which allows for quick determination of whether two strings are equal.

We choose a fixed value BASE, and consider the string as a number in BASE radix, assigning a value greater than 0 to represent each character. Generally, the values we assign are much smaller than BASE. For example, for strings composed of lowercase letters, we can assign a=1, b=2, ..., z=26. We choose a fixed value MOD, and calculate the remainder of the BASE radix number divided by MOD, which is used as the hash value of the string.

Generally, we choose BASE=131 or BASE=13331, at which point the probability of hash value collision is extremely low. As long as the hash values of two strings are the same, we consider the two strings to be equal. Usually, MOD is chosen as $2^{64}$. In C++, we can directly use the unsigned long long type to store this hash value. When calculating, we do not handle arithmetic overflow. When overflow occurs, it is equivalent to automatically taking the modulus of $2^{64}$, which can avoid inefficient modulus operations.

Except for extremely specially constructed data, the above hash algorithm is unlikely to produce collisions. In general, the above hash algorithm can appear in the standard answers of the problem. We can also choose some appropriate values of BASE and MOD (such as large prime numbers), and perform several groups of hash operations. Only when the results are all the same do we consider the original strings to be equal, making it even more difficult to construct data that causes this hash to produce errors.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(1, len(s)):
            if s[:-i] == s[i:]:
                return s[i:]
        return ''
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: KMP Algorithm

According to the problem description, we need to find the longest happy prefix of a string, which is the longest prefix of the string that is also a suffix of the string. We can use the KMP algorithm to solve this problem.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        s += "#"
        n = len(s)
        next = [0] * n
        next[0] = -1
        i, j = 2, 0
        while i < n:
            if s[i - 1] == s[j]:
                j += 1
                next[i] = j
                i += 1
            elif j:
                j = next[j]
            else:
                next[i] = 0
                i += 1
        return s[: next[-1]]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
