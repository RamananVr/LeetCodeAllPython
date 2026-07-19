---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3600-3699/3666.Minimum%20Operations%20to%20Equalize%20Binary%20String/README_EN.md
rating: 2476
source: Biweekly Contest 164 Q4
tags:
    - Breadth-First Search
    - Union Find
    - Math
    - String
    - Ordered Set
---

<!-- problem:start -->

# [3666. Minimum Operations to Equalize Binary String](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string)

## Description

<!-- description:start -->

<p>You are given a binary string <code>s</code>, and an integer <code>k</code>.</p>

<p>In one operation, you must choose <strong>exactly</strong> <code>k</code> <strong>different</strong> indices and <strong>flip</strong> each <code>&#39;0&#39;</code> to <code>&#39;1&#39;</code> and each <code>&#39;1&#39;</code> to <code>&#39;0&#39;</code>.</p>

<p>Return the <strong>minimum</strong> number of operations required to make all characters in the string equal to <code>&#39;1&#39;</code>. If it is not possible, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;110&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is one <code>&#39;0&#39;</code> in <code>s</code>.</li>
	<li>Since <code>k = 1</code>, we can flip it directly in one operation.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0101&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal set of operations choosing <code>k = 3</code> indices in each operation is:</p>

<ul>
	<li><strong>Operation 1</strong>: Flip indices <code>[0, 1, 3]</code>. <code>s</code> changes from <code>&quot;0101&quot;</code> to <code>&quot;1000&quot;</code>.</li>
	<li><strong>Operation 2</strong>: Flip indices <code>[1, 2, 3]</code>. <code>s</code> changes from <code>&quot;1000&quot;</code> to <code>&quot;1111&quot;</code>.</li>
</ul>

<p>Thus, the minimum number of operations is 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;101&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>Since <code>k = 2</code> and <code>s</code> has only one <code>&#39;0&#39;</code>, it is impossible to flip exactly <code>k</code> indices to make all <code>&#39;1&#39;</code>. Hence, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>​​​​​​​5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS + Ordered Set

We denote the length of string $s$ as $n$, and the current number of '0's in the string as $\textit{cur}$. In each operation, we select $k$ indices to flip, where $x$ indices flip from '0' to '1', and $k-x$ indices flip from '1' to '0'. Then the number of '0's in the string after flipping is $\textit{cur} + k - 2x$.

The value of $x$ needs to satisfy the following conditions:

1. At most $\min(\textit{cur}, k)$ '0's can be taken, because we cannot flip more than $\textit{cur}$ '0's, so $0 \leq x \leq \min(\textit{cur}, k)$.
2. At most $n - \textit{cur}$ '1's can be taken, because we cannot flip more than $n - \textit{cur}$ '1's, so $k - x \leq n - \textit{cur}$, i.e., $x \geq k - n + \textit{cur}$.

Therefore, the range of $x$ is $[\max(k - n + \textit{cur}, 0), \min(\textit{cur}, k)]$, and the range of the number of '0's in the string after flipping is $[\textit{cur} + k - 2 \cdot \min(\textit{cur}, k), \textit{cur} + k - 2 \cdot \max(k - n + \textit{cur}, 0)]$.

We notice that the parity of the number of '0's in the string after flipping is the same as the parity of the number of '0's in the string before flipping. Therefore, we can use two ordered sets to store states where the number of '0's is even and odd, respectively.

We use BFS to search the state transition graph, where the initial state is the number of '0's in the string, and the target state is 0. Each time we dequeue a state $\textit{cur}$, we calculate the range $[l, r]$ of the number of '0's in the string after flipping, find all states in the range $[l, r]$ in the ordered set, add them to the queue, and remove them from the ordered set.

If we visit state 0 during the BFS process, we return the current number of operations; if state 0 is not visited after BFS ends, we return -1.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $O(n)$ is the number of states that may be visited during the BFS process, and $O(\log n)$ is the time complexity of inserting and deleting elements in the ordered set.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        ts = [SortedSet() for _ in range(2)]
        for i in range(n + 1):
            ts[i % 2].add(i)
        cnt0 = s.count('0')
        ts[cnt0 % 2].remove(cnt0)
        q = deque([cnt0])
        ans = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0:
                    return ans
                l = cur + k - 2 * min(cur, k)
                r = cur + k - 2 * max(k - n + cur, 0)
                t = ts[l % 2]
                j = t.bisect_left(l)
                while j < len(t) and t[j] <= r:
                    q.append(t[j])
                    t.remove(t[j])
            ans += 1
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
