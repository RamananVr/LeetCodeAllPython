---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1181.Before%20and%20After%20Puzzle/README_EN.md
rating: 1558
source: Biweekly Contest 8 Q2
tags:
    - Array
    - Hash Table
    - String
    - Sorting
---

<!-- problem:start -->

# [1181. Before and After Puzzle 🔒](https://leetcode.com/problems/before-and-after-puzzle)

## Description

<!-- description:start -->

<p>Given a list of <code>phrases</code>, generate a list of&nbsp;Before and After puzzles.</p>

<p>A <em>phrase</em> is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are&nbsp;no consecutive spaces&nbsp;in a phrase.</p>

<p><em>Before and After&nbsp;puzzles</em> are phrases that are formed by merging&nbsp;two phrases where the <strong>last&nbsp;word of the first&nbsp;phrase</strong> is the same as the <strong>first word of the second phrase</strong>. Note that only the <em>last word of the first phrase</em> and the <em>first word of the second phrase</em> are merged in this process.</p>

<p>Return the&nbsp;Before and After&nbsp;puzzles that can be formed by every two phrases&nbsp;<code>phrases[i]</code>&nbsp;and&nbsp;<code>phrases[j]</code>&nbsp;where&nbsp;<code>i != j</code>. Note that the order of matching two phrases matters, we want to consider both orders.</p>

<p>You should return a list of&nbsp;<strong>distinct</strong>&nbsp;strings <strong>sorted&nbsp;lexicographically</strong>, after removing all <em>duplicate</em> phrases in the generated Before and After puzzles.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">phrases = [&quot;writing code&quot;,&quot;code rocks&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;writing code rocks&quot;]</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">phrases = [&quot;mission statement&quot;,&quot;a quick bite to eat&quot;,&quot;a chip off the old block&quot;,&quot;chocolate bar&quot;,&quot;mission impossible&quot;,&quot;a man on a mission&quot;,&quot;block party&quot;,&quot;eat my words&quot;,&quot;bar of soap&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;a chip off the old block party&quot;,&quot;a man on a mission impossible&quot;,&quot;a man on a mission statement&quot;,&quot;a quick bite to eat my words&quot;,&quot;chocolate bar of soap&quot;]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">phrases = [&quot;a&quot;,&quot;b&quot;,&quot;a&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;a&quot;]</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">phrases = [&quot;ab ba&quot;,&quot;ba ab&quot;,&quot;ab ba&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;ab ba ab&quot;,&quot;ba ab ba&quot;]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= phrases.length &lt;= 100</code></li>
	<li><code>1 &lt;= phrases[i].length &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sorting

First, we traverse the `phrases` list, storing the first and last words of each phrase in the array $ps$, where $ps[i][0]$ and $ps[i][1]$ represent the first and last words of the $i$th phrase, respectively.

Next, we enumerate all $(i, j)$, where $i, j \in [0, n)$ and $i \neq j$. If $ps[i][1] = ps[j][0]$, then we can concatenate the $i$th phrase and the $j$th phrase to get a new phrase $phrases[i] + phrases[j][len(ps[j][0]):]$, and add the new phrase to the hash table $s$.

Finally, we convert the hash table $s$ into an array and sort it to get the answer.

The time complexity is $O(n^2 \times m \times (\log n + \log m))$, and the space complexity is $O(n^2 \times m)$. Here, $n$ and $m$ represent the length of the `phrases` array and the average length of each phrase, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        ps = []
        for p in phrases:
            ws = p.split()
            ps.append((ws[0], ws[-1]))
        n = len(ps)
        ans = []
        for i in range(n):
            for j in range(n):
                if i != j and ps[i][1] == ps[j][0]:
                    ans.append(phrases[i] + phrases[j][len(ps[j][0]) :])
        return sorted(set(ans))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
