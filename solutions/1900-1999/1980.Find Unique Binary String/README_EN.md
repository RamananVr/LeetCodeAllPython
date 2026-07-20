---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1900-1999/1980.Find%20Unique%20Binary%20String/README_EN.md
rating: 1361
source: Weekly Contest 255 Q2
tags:
    - Array
    - Hash Table
    - String
    - Backtracking
---

<!-- problem:start -->

# [1980. Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string)

## Description

<!-- description:start -->

<p>Given an array of strings <code>nums</code> containing <code>n</code> <strong>unique</strong> binary strings each of length <code>n</code>, return <em>a binary string of length </em><code>n</code><em> that <strong>does not appear</strong> in </em><code>nums</code><em>. If there are multiple answers, you may return <strong>any</strong> of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;01&quot;,&quot;10&quot;]
<strong>Output:</strong> &quot;11&quot;
<strong>Explanation:</strong> &quot;11&quot; does not appear in nums. &quot;00&quot; would also be correct.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;00&quot;,&quot;01&quot;]
<strong>Output:</strong> &quot;11&quot;
<strong>Explanation:</strong> &quot;11&quot; does not appear in nums. &quot;10&quot; would also be correct.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;111&quot;,&quot;011&quot;,&quot;001&quot;]
<strong>Output:</strong> &quot;101&quot;
<strong>Explanation:</strong> &quot;101&quot; does not appear in nums. &quot;000&quot;, &quot;010&quot;, &quot;100&quot;, and &quot;110&quot; would also be correct.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 16</code></li>
	<li><code>nums[i].length == n</code></li>
	<li><code>nums[i] </code>is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li>All the strings of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Enumeration

Since the number of `'1'`s in a binary string of length $n$ can be $0, 1, 2, \cdots, n$ (a total of $n + 1$ possibilities), we can always find a new binary string whose count of `'1'`s differs from every string in $\textit{nums}$.

We use an integer $\textit{mask}$ to record the counts of `'1'`s across all strings, where the $i$-th bit of $\textit{mask}$ being $1$ indicates that a binary string of length $n$ with exactly $i$ occurrences of `'1'` exists in $\textit{nums}$, and $0$ otherwise.

We then enumerate $i$ starting from $0$, representing the count of `'1'`s in a binary string of length $n$. If the $i$-th bit of $\textit{mask}$ is $0$, it means no binary string of length $n$ with exactly $i$ occurrences of `'1'` exists, and we can return that string as the answer.

The time complexity is $O(L)$, where $L$ is the total length of all strings in $\textit{nums}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        mask = 0
        for x in nums:
            mask |= 1 << x.count("1")
        for i in count(0):
            if mask >> i & 1 ^ 1:
                return "1" * i + "0" * (len(nums) - i)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Construction

We can construct a binary string $\textit{ans}$ of length $n$, where the $i$-th bit of $\textit{ans}$ differs from the $i$-th bit of $\textit{nums}[i]$. Since all strings in $\textit{nums}$ are distinct, $\textit{ans}$ will not appear in $\textit{nums}$.

The time complexity is $O(n)$, where $n$ is the length of the strings in $\textit{nums}$. Ignoring the space used by the answer string, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = [None] * len(nums)
        for i, s in enumerate(nums):
            ans[i] = "1" if s[i] == "0" else "0"
        return "".join(ans)
```

<!-- solution:end -->

<!-- tabs:end -->

<!-- problem:end -->
