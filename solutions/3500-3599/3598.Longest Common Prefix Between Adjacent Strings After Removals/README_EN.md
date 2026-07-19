---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3598.Longest%20Common%20Prefix%20Between%20Adjacent%20Strings%20After%20Removals/README_EN.md
rating: 1655
source: Weekly Contest 456 Q2
tags:
    - Array
    - String
---

<!-- problem:start -->

# [3598. Longest Common Prefix Between Adjacent Strings After Removals](https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals)

## Description

<!-- description:start -->

<p>You are given an array of strings <code>words</code>. For each index <code>i</code> in the range <code>[0, words.length - 1]</code>, perform the following steps:</p>

<ul>
	<li>Remove the element at index <code>i</code> from the <code>words</code> array.</li>
	<li>Compute the <strong>length</strong> of the <strong>longest common <span data-keyword="string-prefix">prefix</span></strong> among all <strong>adjacent</strong> pairs in the modified array.</li>
</ul>

<p>Return an array <code>answer</code>, where <code>answer[i]</code> is the length of the longest common prefix between the adjacent pairs after removing the element at index <code>i</code>. If <strong>no</strong> adjacent pairs remain or if <strong>none</strong> share a common prefix, then <code>answer[i]</code> should be 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;jump&quot;,&quot;run&quot;,&quot;run&quot;,&quot;jump&quot;,&quot;run&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,0,0,3,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Removing index 0:
	<ul>
		<li><code>words</code> becomes <code>[&quot;run&quot;, &quot;run&quot;, &quot;jump&quot;, &quot;run&quot;]</code></li>
		<li>Longest adjacent pair is <code>[&quot;run&quot;, &quot;run&quot;]</code> having a common prefix <code>&quot;run&quot;</code> (length 3)</li>
	</ul>
	</li>
	<li>Removing index 1:
	<ul>
		<li><code>words</code> becomes <code>[&quot;jump&quot;, &quot;run&quot;, &quot;jump&quot;, &quot;run&quot;]</code></li>
		<li>No adjacent pairs share a common prefix (length 0)</li>
	</ul>
	</li>
	<li>Removing index 2:
	<ul>
		<li><code>words</code> becomes <code>[&quot;jump&quot;, &quot;run&quot;, &quot;jump&quot;, &quot;run&quot;]</code></li>
		<li>No adjacent pairs share a common prefix (length 0)</li>
	</ul>
	</li>
	<li>Removing index 3:
	<ul>
		<li><code>words</code> becomes <code>[&quot;jump&quot;, &quot;run&quot;, &quot;run&quot;, &quot;run&quot;]</code></li>
		<li>Longest adjacent pair is <code>[&quot;run&quot;, &quot;run&quot;]</code> having a common prefix <code>&quot;run&quot;</code> (length 3)</li>
	</ul>
	</li>
	<li>Removing index 4:
	<ul>
		<li>words becomes <code>[&quot;jump&quot;, &quot;run&quot;, &quot;run&quot;, &quot;jump&quot;]</code></li>
		<li>Longest adjacent pair is <code>[&quot;run&quot;, &quot;run&quot;]</code> having a common prefix <code>&quot;run&quot;</code> (length 3)</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;dog&quot;,&quot;racer&quot;,&quot;car&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Removing any index results in an answer of 0.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10<sup>4</sup></code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
	<li>The sum of <code>words[i].length</code> is smaller than or equal <code>10<sup>5</sup></code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Ordered Set

We define a function $\textit{calc}(s, t)$, which calculates the length of the longest common prefix between strings $s$ and $t$. We can use an ordered set to maintain the longest common prefix lengths of all adjacent string pairs.

Define a function $\textit{add}(i, j)$, which adds the longest common prefix length of the string pair at indices $i$ and $j$ to the ordered set. Define a function $\textit{remove}(i, j)$, which removes the longest common prefix length of the string pair at indices $i$ and $j$ from the ordered set.

First, we compute the longest common prefix lengths for all adjacent string pairs and store them in the ordered set. Then, for each index $i$, we perform the following steps:

1. Remove the longest common prefix length of the string pair at indices $i$ and $i + 1$.
2. Remove the longest common prefix length of the string pair at indices $i - 1$ and $i$.
3. Add the longest common prefix length of the string pair at indices $i - 1$ and $i + 1$.
4. Add the current maximum value in the ordered set (if it exists and is greater than 0) to the answer.
5. Remove the longest common prefix length of the string pair at indices $i - 1$ and $i + 1$.
6. Add the longest common prefix length of the string pair at indices $i - 1$ and $i$.
7. Add the longest common prefix length of the string pair at indices $i$ and $i + 1$.

In this way, after removing each string, we can quickly compute the longest common prefix length between adjacent string pairs.

The time complexity is $O(L + n \times \log n)$, and the space complexity is $O(n)$, where $L$ is the total length of all strings and $n$ is the number of strings.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        @cache
        def calc(s: str, t: str) -> int:
            k = 0
            for a, b in zip(s, t):
                if a != b:
                    break
                k += 1
            return k

        def add(i: int, j: int):
            if 0 <= i < n and 0 <= j < n:
                sl.add(calc(words[i], words[j]))

        def remove(i: int, j: int):
            if 0 <= i < n and 0 <= j < n:
                sl.remove(calc(words[i], words[j]))

        n = len(words)
        sl = SortedList(calc(a, b) for a, b in pairwise(words))
        ans = []
        for i in range(n):
            remove(i, i + 1)
            remove(i - 1, i)
            add(i - 1, i + 1)
            ans.append(sl[-1] if sl and sl[-1] > 0 else 0)
            remove(i - 1, i + 1)
            add(i - 1, i)
            add(i, i + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
