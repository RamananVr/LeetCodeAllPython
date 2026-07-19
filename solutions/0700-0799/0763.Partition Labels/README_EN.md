---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0763.Partition%20Labels/README_EN.md
tags:
    - Greedy
    - Hash Table
    - Two Pointers
    - String
---

<!-- problem:start -->

# [763. Partition Labels](https://leetcode.com/problems/partition-labels)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code>. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string <code>&quot;ababcc&quot;</code> can be partitioned into <code>[&quot;abab&quot;, &quot;cc&quot;]</code>, but partitions such as <code>[&quot;aba&quot;, &quot;bcc&quot;]</code> or <code>[&quot;ab&quot;, &quot;ab&quot;, &quot;cc&quot;]</code> are invalid.</p>

<p>Note that the partition is done so that after concatenating all the parts in order, the resultant string should be <code>s</code>.</p>

<p>Return <em>a list of integers representing the size of these parts</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababcbacadefegdehijhklij&quot;
<strong>Output:</strong> [9,7,8]
<strong>Explanation:</strong>
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits s into less parts.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;eccbbbbdec&quot;
<strong>Output:</strong> [10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy

We first use an array or hash table $\textit{last}$ to record the last occurrence of each letter in the string $s$.

Next, we use a greedy approach to partition the string into as many segments as possible.

Traverse the string $s$ from left to right, while maintaining the start index $j$ and end index $i$ of the current segment, both initially set to $0$.

For each letter $c$ visited, get the last occurrence position $\textit{last}[c]$. Since the end index of the current segment must not be less than $\textit{last}[c]$, let $\textit{mx} = \max(\textit{mx}, \textit{last}[c])$.

When visiting the index $\textit{mx}$, it means the current segment ends. The index range of the current segment is $[j,.. i]$, and the length is $i - j + 1$. We add this length to the result array. Then set $j = i + 1$ and continue to find the next segment.

Repeat the above process until the string traversal is complete to get the lengths of all segments.

Time complexity is $O(n)$, and space complexity is $O(|\Sigma|)$. Where $n$ is the length of the string $s$, and $|\Sigma|$ is the size of the character set. In this problem, $|\Sigma| = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        mx = j = 0
        ans = []
        for i, c in enumerate(s):
            mx = max(mx, last[c])
            if mx == i:
                ans.append(i - j + 1)
                j = i + 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
