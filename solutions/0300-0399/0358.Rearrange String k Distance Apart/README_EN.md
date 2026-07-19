---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0358.Rearrange%20String%20k%20Distance%20Apart/README_EN.md
tags:
    - Greedy
    - Hash Table
    - String
    - Counting
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [358. Rearrange String k Distance Apart 🔒](https://leetcode.com/problems/rearrange-string-k-distance-apart)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> and an integer <code>k</code>, rearrange <code>s</code> such that the same characters are <strong>at least</strong> distance <code>k</code> from each other. If it is not possible to rearrange the string, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabbcc&quot;, k = 3
<strong>Output:</strong> &quot;abcabc&quot;
<strong>Explanation:</strong> The same letters are at least a distance of 3 from each other.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabc&quot;, k = 3
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> It is not possible to rearrange the string.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaadbbcc&quot;, k = 2
<strong>Output:</strong> &quot;abacabcd&quot;
<strong>Explanation:</strong> The same letters are at least a distance of 2 from each other.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Hash Table + Priority Queue (Max Heap)

We use a hash table or array $\textit{cnt}$ to count the occurrences of each character in the string. Then, we use a max heap $\textit{pq}$ to store each character and its count. Each element in the heap is a tuple $(v, c)$, where $v$ is the count and $c$ is the character.

When rearranging the string, we repeatedly pop the top element $(v, c)$ from the heap, add character $c$ to the result string, and push $(v-1, c)$ into a queue $\textit{q}$. When the length of the queue $\textit{q}$ reaches $k$ or more, we pop the front element; if its $v$ is greater than $0$, we push it back into the heap. Repeat this process until the heap is empty.

Finally, we check whether the length of the result string equals the original string. If so, we return the result string; otherwise, we return an empty string.

The time complexity is $O(n \log n)$, where $n$ is the length of the string. The space complexity is $O(|\Sigma|)$, where $|\Sigma|$ is the size of the character set, which is $26$ in this problem.

Related problems:

- [767. Reorganize String](https://github.com/doocs/leetcode/blob/main/solution/0700-0799/0767.Reorganize%20String/README.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        cnt = Counter(s)
        pq = [(-v, c) for c, v in cnt.items()]
        heapify(pq)
        q = deque()
        ans = []
        while pq:
            v, c = heappop(pq)
            ans.append(c)
            q.append((v + 1, c))
            if len(q) >= k:
                e = q.popleft()
                if e[0]:
                    heappush(pq, e)
        return "" if len(ans) < len(s) else "".join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
