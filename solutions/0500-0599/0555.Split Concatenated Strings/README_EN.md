---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0555.Split%20Concatenated%20Strings/README_EN.md
tags:
    - Greedy
    - Array
    - String
---

<!-- problem:start -->

# [555. Split Concatenated Strings 🔒](https://leetcode.com/problems/split-concatenated-strings)

## Description

<!-- description:start -->

<p>You are given an array of strings <code>strs</code>. You could concatenate these strings together into a loop, where for each string, you could choose to reverse it or not. Among all the possible loops</p>

<p>Return <em>the lexicographically largest string after cutting the loop, which will make the looped string into a regular one</em>.</p>

<p>Specifically, to find the lexicographically largest string, you need to experience two phases:</p>

<ol>
	<li>Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.</li>
	<li>Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.</li>
</ol>

<p>And your job is to find the lexicographically largest one among all the possible regular strings.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;abc&quot;,&quot;xyz&quot;]
<strong>Output:</strong> &quot;zyxcba&quot;
<strong>Explanation:</strong> You can get the looped string &quot;-abcxyz-&quot;, &quot;-abczyx-&quot;, &quot;-cbaxyz-&quot;, &quot;-cbazyx-&quot;, where &#39;-&#39; represents the looped status. 
The answer string came from the fourth looped one, where you could cut from the middle character &#39;a&#39; and get &quot;zyxcba&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;abc&quot;]
<strong>Output:</strong> &quot;cba&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 1000</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 1000</code></li>
	<li><code>1 &lt;= sum(strs[i].length) &lt;= 1000</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy

We first traverse the string array `strs`. For each string $s$, if the reversed string $t$ is greater than $s$, we replace $s$ with $t$.

Then we enumerate each position $i$ in the string array `strs` as a split point, dividing the string array `strs` into two parts: $strs[i + 1:]$ and $strs[:i]$. We then concatenate these two parts to get a new string $t$. Next, we enumerate each position $j$ in the current string $strs[i]$. The suffix part is $a = strs[i][j:]$, and the prefix part is $b = strs[i][:j]$. We can concatenate $a$, $t$, and $b$ to get a new string $cur$. If $cur$ is greater than the current answer, we update the answer. This considers the case where $strs[i]$ is reversed. We also need to consider the case where $strs[i]$ is not reversed, i.e., concatenate $a$, $t$, and $b$ in reverse order to get a new string $cur$. If $cur$ is greater than the current answer, we update the answer.

Finally, we return the answer.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string array `strs`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [s[::-1] if s[::-1] > s else s for s in strs]
        ans = ''.join(strs)
        for i, s in enumerate(strs):
            t = ''.join(strs[i + 1 :]) + ''.join(strs[:i])
            for j in range(len(s)):
                a = s[j:]
                b = s[:j]
                ans = max(ans, a + t + b)
                ans = max(ans, b[::-1] + t + a[::-1])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
