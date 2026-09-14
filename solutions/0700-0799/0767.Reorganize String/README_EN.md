---
comments: true
difficulty: Medium
tags:
    - Greedy
    - Hash Table
    - String
    - Counting
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [767. Reorganize String](https://leetcode.com/problems/reorganize-string)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, rearrange the characters of <code>s</code> so that any two adjacent characters are not the same.</p>

<p>Return <em>any possible rearrangement of</em> <code>s</code> <em>or return</em> <code>&quot;&quot;</code> <em>if not possible</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> "aba"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaab"
<strong>Output:</strong> ""
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

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Rearrange so no two adjacent characters match. If one letter exceeds $\lceil n/2\rceil$, it is impossible.
>
> Place the most frequent letters on even indices first, then restart at index $1$, which separates copies.
>
> Fill from `most_common` into a buffer, wrapping $i$ to $1$ when it passes $n$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        cnt = Counter(s)
        mx = max(cnt.values())
        if mx > (n + 1) // 2:
            return ''
        i = 0
        ans = [None] * n
        for k, v in cnt.most_common():
            while v:
                ans[i] = k
                v -= 1
                i += 2
                if i >= n:
                    i = 1
        return ''.join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Even-index placement is specific to distance $1$. The same greedy as “rearrange $k$ apart” uses a max-heap plus a cooldown queue of length $k=2$.
>
> Pop the current most frequent letter, enqueue it, and return it to the heap after $k$ steps. If the built string is short, fail.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        return self.rearrangeString(s, 2)

    def rearrangeString(self, s: str, k: int) -> str:
        h = [(-v, c) for c, v in Counter(s).items()]
        heapify(h)
        q = deque()
        ans = []
        while h:
            v, c = heappop(h)
            v *= -1
            ans.append(c)
            q.append((v - 1, c))
            if len(q) >= k:
                w, c = q.popleft()
                if w:
                    heappush(h, (-w, c))
        return "" if len(ans) != len(s) else "".join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
