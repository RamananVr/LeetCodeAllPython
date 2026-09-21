---
comments: true
difficulty: Hard
rating: 2289
source: Biweekly Contest 152 Q3
tags:
    - Trie
    - Array
    - String
---

<!-- problem:start -->

# [3485. Longest Common Prefix of K Strings After Removal](https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal)

## Description

<!-- description:start -->

<p>You are given an array of strings <code>words</code> and an integer <code>k</code>.</p>

<p>For each index <code>i</code> in the range <code>[0, words.length - 1]</code>, find the <strong>length</strong> of the <strong>longest common <span data-keyword="string-prefix">prefix</span></strong> among any <code>k</code> strings (selected at <strong>distinct indices</strong>) from the remaining array after removing the <code>i<sup>th</sup></code> element.</p>

<p>Return an array <code>answer</code>, where <code>answer[i]</code> is the answer for <code>i<sup>th</sup></code> element. If removing the <code>i<sup>th</sup></code> element leaves the array with fewer than <code>k</code> strings, <code>answer[i]</code> is 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;jump&quot;,&quot;run&quot;,&quot;run&quot;,&quot;jump&quot;,&quot;run&quot;], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,4,4,3,4]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Removing index 0 (<code>&quot;jump&quot;</code>):

    <ul>
    	<li><code>words</code> becomes: <code>[&quot;run&quot;, &quot;run&quot;, &quot;jump&quot;, &quot;run&quot;]</code>. <code>&quot;run&quot;</code> occurs 3 times. Choosing any two gives the longest common prefix <code>&quot;run&quot;</code> (length 3).</li>
    </ul>
    </li>
    <li>Removing index 1 (<code>&quot;run&quot;</code>):
    <ul>
    	<li><code>words</code> becomes: <code>[&quot;jump&quot;, &quot;run&quot;, &quot;jump&quot;, &quot;run&quot;]</code>. <code>&quot;jump&quot;</code> occurs twice. Choosing these two gives the longest common prefix <code>&quot;jump&quot;</code> (length 4).</li>
    </ul>
    </li>
    <li>Removing index 2 (<code>&quot;run&quot;</code>):
    <ul>
    	<li><code>words</code> becomes: <code>[&quot;jump&quot;, &quot;run&quot;, &quot;jump&quot;, &quot;run&quot;]</code>. <code>&quot;jump&quot;</code> occurs twice. Choosing these two gives the longest common prefix <code>&quot;jump&quot;</code> (length 4).</li>
    </ul>
    </li>
    <li>Removing index 3 (<code>&quot;jump&quot;</code>):
    <ul>
    	<li><code>words</code> becomes: <code>[&quot;jump&quot;, &quot;run&quot;, &quot;run&quot;, &quot;run&quot;]</code>. <code>&quot;run&quot;</code> occurs 3 times. Choosing any two gives the longest common prefix <code>&quot;run&quot;</code> (length 3).</li>
    </ul>
    </li>
    <li>Removing index 4 (&quot;run&quot;):
    <ul>
    	<li><code>words</code> becomes: <code>[&quot;jump&quot;, &quot;run&quot;, &quot;run&quot;, &quot;jump&quot;]</code>. <code>&quot;jump&quot;</code> occurs twice. Choosing these two gives the longest common prefix <code>&quot;jump&quot;</code> (length 4).</li>
    </ul>
    </li>

</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;dog&quot;,&quot;racer&quot;,&quot;car&quot;], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Removing any index results in an answer of 0.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10<sup>4</sup></code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
	<li>The sum of <code>words[i].length</code> is smaller than or equal <code>10<sup>5</sup></code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> For each deleted word we want the LCP of any $k$ remaining strings. The total length is $\le 10^5$, so each query cannot rebuild the trie.
>
> The maximum depth of a trie node with count $\ge k$ is the global answer. Deleting a word only hurts ancestors whose count is exactly $k$.
>
> A segment tree keyed by depth stores how many nodes still have count $\ge k$. We decrement the fragile depths of the deleted word, query the max surviving depth, and roll back. If $n-1<k$, every answer is $0$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        ans = [0] * n
        if n - 1 < k:
            return ans

        trie = [{'count': 0, 'depth': 0, 'children': [-1] * 26}]
        for word in words:
            cur = 0
            for c in word:
                idx = ord(c) - 97
                if trie[cur]['children'][idx] == -1:
                    trie[cur]['children'][idx] = len(trie)
                    trie.append(
                        {
                            'count': 0,
                            'depth': trie[cur]['depth'] + 1,
                            'children': [-1] * 26,
                        }
                    )
                cur = trie[cur]['children'][idx]
                trie[cur]['count'] += 1

        max_depth = 0
        for i in range(1, len(trie)):
            if trie[i]['count'] >= k:
                max_depth = max(max_depth, trie[i]['depth'])

        global_count = [0] * (max_depth + 1)
        for i in range(1, len(trie)):
            node = trie[i]
            if node['count'] >= k and node['depth'] <= max_depth:
                global_count[node['depth']] += 1

        fragile_list = [[] for _ in range(n)]
        for i, word in enumerate(words):
            cur = 0
            for c in word:
                idx = ord(c) - 97
                cur = trie[cur]['children'][idx]
                if trie[cur]['count'] == k:
                    fragile_list[i].append(trie[cur]['depth'])

        seg_size = max_depth
        if seg_size < 1:
            return ans

        tree = [-1] * (4 * (seg_size + 1))

        def build(idx: int, l: int, r: int) -> None:
            if l == r:
                tree[idx] = l if global_count[l] > 0 else -1
                return
            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1])

        def update(idx: int, l: int, r: int, pos: int, new_val: int) -> None:
            if l == r:
                tree[idx] = l if new_val > 0 else -1
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(idx * 2, l, mid, pos, new_val)
            else:
                update(idx * 2 + 1, mid + 1, r, pos, new_val)
            tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1])

        build(1, 1, seg_size)
        for i in range(n):
            for d in fragile_list[i]:
                update(1, 1, seg_size, d, global_count[d] - 1)
            res = tree[1]
            ans[i] = 0 if res == -1 else res
            for d in fragile_list[i]:
                update(1, 1, seg_size, d, global_count[d])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
