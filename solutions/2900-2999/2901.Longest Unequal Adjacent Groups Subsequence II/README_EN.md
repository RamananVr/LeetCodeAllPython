---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2901.Longest%20Unequal%20Adjacent%20Groups%20Subsequence%20II/README_EN.md
rating: 1898
source: Biweekly Contest 115 Q3
tags:
    - Array
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [2901. Longest Unequal Adjacent Groups Subsequence II](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii)

## Description

<!-- description:start -->

<p>You are given a string array <code>words</code>, and an array <code>groups</code>, both arrays having length <code>n</code>.</p>

<p>The <strong>hamming distance</strong> between two strings of equal length is the number of positions at which the corresponding characters are <strong>different</strong>.</p>

<p>You need to select the <strong>longest</strong> <span data-keyword="subsequence-array">subsequence</span> from an array of indices <code>[0, 1, ..., n - 1]</code>, such that for the subsequence denoted as <code>[i<sub>0</sub>, i<sub>1</sub>, ..., i<sub>k-1</sub>]</code> having length <code>k</code>, the following holds:</p>

<ul>
	<li>For <strong>adjacent</strong> indices in the subsequence, their corresponding groups are <strong>unequal</strong>, i.e., <code>groups[i<sub>j</sub>] != groups[i<sub>j+1</sub>]</code>, for each <code>j</code> where <code>0 &lt; j + 1 &lt; k</code>.</li>
	<li><code>words[i<sub>j</sub>]</code> and <code>words[i<sub>j+1</sub>]</code> are <strong>equal</strong> in length, and the <strong>hamming distance</strong> between them is <code>1</code>, where <code>0 &lt; j + 1 &lt; k</code>, for all indices in the subsequence.</li>
</ul>

<p>Return <em>a string array containing the words corresponding to the indices <strong>(in order)</strong> in the selected subsequence</em>. If there are multiple answers, return <em>any of them</em>.</p>

<p><strong>Note:</strong> strings in <code>words</code> may be <strong>unequal</strong> in length.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">words = [&quot;bab&quot;,&quot;dab&quot;,&quot;cab&quot;], groups = [1,2,2]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">[&quot;bab&quot;,&quot;cab&quot;]</span></p>

<p><strong>Explanation: </strong>A subsequence that can be selected is <code>[0,2]</code>.</p>

<ul>
	<li><code>groups[0] != groups[2]</code></li>
	<li><code>words[0].length == words[2].length</code>, and the hamming distance between them is 1.</li>
</ul>

<p>So, a valid answer is <code>[words[0],words[2]] = [&quot;bab&quot;,&quot;cab&quot;]</code>.</p>

<p>Another subsequence that can be selected is <code>[0,1]</code>.</p>

<ul>
	<li><code>groups[0] != groups[1]</code></li>
	<li><code>words[0].length == words[1].length</code>, and the hamming distance between them is <code>1</code>.</li>
</ul>

<p>So, another valid answer is <code>[words[0],words[1]] = [&quot;bab&quot;,&quot;dab&quot;]</code>.</p>

<p>It can be shown that the length of the longest subsequence of indices that satisfies the conditions is <code>2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;], groups = [1,2,3,4]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;]</span></p>

<p><strong>Explanation: </strong>We can select the subsequence <code>[0,1,2,3]</code>.</p>

<p>It satisfies both conditions.</p>

<p>Hence, the answer is <code>[words[0],words[1],words[2],words[3]] = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;]</code>.</p>

<p>It has the longest length among all subsequences of indices that satisfy the conditions.</p>

<p>Hence, it is the only answer.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == words.length == groups.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= groups[i] &lt;= n</code></li>
	<li><code>words</code> consists of <strong>distinct</strong> strings.</li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i]$ as the length of the longest adjacent non-equal subsequence ending with the $i$-th word, and $g[i]$ as the predecessor index of the longest adjacent non-equal subsequence ending with the $i$-th word. Initially, we set $f[i] = 1$ and $g[i] = -1$.

In addition, we define a variable $mx$ to represent the length of the longest adjacent non-equal subsequence.

We traverse $i$ and $j \in [0, i)$, and if $groups[i] \neq groups[j]$, $f[i] \lt f[j] + 1$, and the Hamming distance between $words[i]$ and $words[j]$ is $1$, we update $f[i] = f[j] + 1$, $g[i] = j$, and update $mx = \max(mx, f[i])$.

Finally, we find the index $i$ corresponding to the maximum value in the $f$ array, and then continuously search backwards from $i$ until we find $g[i] = -1$, which gives us the longest adjacent non-equal subsequence.

The time complexity is $O(n^2 \times L)$, and the space complexity is $O(n)$. Here, $L$ represents the maximum length of a word.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        def check(s: str, t: str) -> bool:
            return len(s) == len(t) and sum(a != b for a, b in zip(s, t)) == 1

        n = len(groups)
        f = [1] * n
        g = [-1] * n
        mx = 1
        for i, x in enumerate(groups):
            for j, y in enumerate(groups[:i]):
                if x != y and f[i] < f[j] + 1 and check(words[i], words[j]):
                    f[i] = f[j] + 1
                    g[i] = j
                    mx = max(mx, f[i])
        ans = []
        for i in range(n):
            if f[i] == mx:
                j = i
                while j >= 0:
                    ans.append(words[j])
                    j = g[j]
                break
        return ans[::-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
