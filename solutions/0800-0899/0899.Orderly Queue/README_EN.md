---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0899.Orderly%20Queue/README_EN.md
tags:
    - Math
    - String
    - Sorting
---

<!-- problem:start -->

# [899. Orderly Queue](https://leetcode.com/problems/orderly-queue)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose one of the first <code>k</code> letters of <code>s</code> and append it at the end of the string.</p>

<p>Return <em>the lexicographically smallest string you could have after applying the mentioned step any number of moves</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cba&quot;, k = 1
<strong>Output:</strong> &quot;acb&quot;
<strong>Explanation:</strong> 
In the first move, we move the 1<sup>st</sup> character &#39;c&#39; to the end, obtaining the string &quot;bac&quot;.
In the second move, we move the 1<sup>st</sup> character &#39;b&#39; to the end, obtaining the final result &quot;acb&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;baaca&quot;, k = 3
<strong>Output:</strong> &quot;aaabc&quot;
<strong>Explanation:</strong> 
In the first move, we move the 1<sup>st</sup> character &#39;b&#39; to the end, obtaining the string &quot;aacab&quot;.
In the second move, we move the 3<sup>rd</sup> character &#39;c&#39; to the end, obtaining the final result &quot;aaabc&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Case-by-case Judgment

If $k = 1$, we can only move the first character of the string to the end of the string each time, resulting in $|s|$ different states. We return the string with the smallest lexicographic order.

If $k > 1$, for a string like $abc[xy]def$, we can move $a$, $b$, and $c$ to the end in order, resulting in $[xy]defabc$. Then we move $y$ and $x$ to the end, resulting in $defabc[yx]$. Finally, we move $d$, $e$, and $f$ to the end, resulting in $abc[yx]def$. This way, we have swapped $y$ and $x$.

Therefore, as long as $k > 1$, we can swap any two adjacent characters in the string, eventually obtaining a string sorted in ascending order.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return "".join(sorted(s))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
