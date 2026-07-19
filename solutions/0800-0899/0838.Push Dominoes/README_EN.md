---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0838.Push%20Dominoes/README_EN.md
tags:
    - Two Pointers
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [838. Push Dominoes](https://leetcode.com/problems/push-dominoes)

## Description

<!-- description:start -->

<p>There are <code>n</code> dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.</p>

<p>After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.</p>

<p>When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.</p>

<p>For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.</p>

<p>You are given a string <code>dominoes</code> representing the initial state where:</p>

<ul>
	<li><code>dominoes[i] = &#39;L&#39;</code>, if the <code>i<sup>th</sup></code> domino has been pushed to the left,</li>
	<li><code>dominoes[i] = &#39;R&#39;</code>, if the <code>i<sup>th</sup></code> domino has been pushed to the right, and</li>
	<li><code>dominoes[i] = &#39;.&#39;</code>, if the <code>i<sup>th</sup></code> domino has not been pushed.</li>
</ul>

<p>Return <em>a string representing the final state</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dominoes = &quot;RR.L&quot;
<strong>Output:</strong> &quot;RR.L&quot;
<strong>Explanation:</strong> The first domino expends no additional force on the second domino.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0838.Push%20Dominoes/images/domino.png" style="height: 196px; width: 512px;" />
<pre>
<strong>Input:</strong> dominoes = &quot;.L.R...LR..L..&quot;
<strong>Output:</strong> &quot;LL.RR.LLRRLL..&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == dominoes.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>dominoes[i]</code> is either <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, or <code>&#39;.&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Multi-Source BFS

Treat all initially pushed dominoes (`L` or `R`) as **sources**, which simultaneously propagate their forces outward. Use a queue to perform BFS layer by layer (0, 1, 2, ...):

We define $\text{time[i]}$ to record the first moment when the _i_-th domino is affected by a force, with `-1` indicating it has not been affected yet. We also define $\text{force[i]}$ as a variable-length list that stores the directions (`'L'`, `'R'`) of forces acting on the domino at the same moment. Initially, push all indices of `L/R` dominoes into the queue and set their `time` to 0.

When dequeuing index _i_, if $\text{force[i]}$ contains only one direction, the domino will fall in that direction $f$. Let the index of the next domino be:

$$
j =
\begin{cases}
i - 1, & f = L,\\
i + 1, & f = R.
\end{cases}
$$

If $0 \leq j < n$:

- If $\text{time[j]} = -1$, it means _j_ has not been affected yet. Record $\text{time[j]} = \text{time[i]} + 1$, enqueue it, and append $f$ to $\text{force[j]}$.
- If $\text{time[j]} = \text{time[i]} + 1$, it means _j_ has already been affected by another force at the same "next moment." In this case, append $f$ to $\text{force[j]}$, causing a standoff. Subsequently, since $\text{len(force[j])} = 2$, it will remain upright.

After the queue is emptied, all positions where $\text{force[i]}$ has a length of 1 will fall in the corresponding direction, while positions with a length of 2 will remain as `.`. Finally, concatenate the character array to form the answer.

The complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of dominoes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        q = deque()
        time = [-1] * n
        force = defaultdict(list)
        for i, f in enumerate(dominoes):
            if f != '.':
                q.append(i)
                time[i] = 0
                force[i].append(f)
        ans = ['.'] * n
        while q:
            i = q.popleft()
            if len(force[i]) == 1:
                ans[i] = f = force[i][0]
                j = i - 1 if f == 'L' else i + 1
                if 0 <= j < n:
                    t = time[i]
                    if time[j] == -1:
                        q.append(j)
                        time[j] = t + 1
                        force[j].append(f)
                    elif time[j] == t + 1:
                        force[j].append(f)
        return ''.join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
