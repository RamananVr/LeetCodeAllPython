---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1654.Minimum%20Jumps%20to%20Reach%20Home/README_EN.md
rating: 2124
source: Biweekly Contest 39 Q3
tags:
    - Breadth-First Search
    - Array
    - Hash Table
---

<!-- problem:start -->

# [1654. Minimum Jumps to Reach Home](https://leetcode.com/problems/minimum-jumps-to-reach-home)

## Description

<!-- description:start -->

<p>A certain bug&#39;s home is on the x-axis at position <code>x</code>. Help them get there from position <code>0</code>.</p>

<p>The bug jumps according to the following rules:</p>

<ul>
	<li>It can jump exactly <code>a</code> positions <strong>forward</strong> (to the right).</li>
	<li>It can jump exactly <code>b</code> positions <strong>backward</strong> (to the left).</li>
	<li>It cannot jump backward twice in a row.</li>
	<li>It cannot jump to any <code>forbidden</code> positions.</li>
</ul>

<p>The bug may jump forward <strong>beyond</strong> its home, but it <strong>cannot jump</strong> to positions numbered with <strong>negative</strong> integers.</p>

<p>Given an array of integers <code>forbidden</code>, where <code>forbidden[i]</code> means that the bug cannot jump to the position <code>forbidden[i]</code>, and integers <code>a</code>, <code>b</code>, and <code>x</code>, return <em>the minimum number of jumps needed for the bug to reach its home</em>. If there is no possible sequence of jumps that lands the bug on position <code>x</code>, return <code>-1.</code></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 jumps forward (0 -&gt; 3 -&gt; 6 -&gt; 9) will get the bug home.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
<strong>Output:</strong> 2
<strong>Explanation:</strong> One jump forward (0 -&gt; 16) then one jump backward (16 -&gt; 7) will get the bug home.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= forbidden.length &lt;= 1000</code></li>
	<li><code>1 &lt;= a, b, forbidden[i] &lt;= 2000</code></li>
	<li><code>0 &lt;= x &lt;= 2000</code></li>
	<li>All the elements in <code>forbidden</code> are distinct.</li>
	<li>Position <code>x</code> is not forbidden.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

We can use the position and jumping direction of the flea as the state, and use BFS to search for the shortest path. The key point of this problem is to determine the right boundary, that is, how far the flea can jump.

If $a \geq b$, that is, the distance to jump forward is greater than the distance to jump backward, then if the flea is in a position greater than $x+b$, it can no longer jump forward, because the flea cannot jump backward consecutively. If it continues to jump forward, it will never be able to jump to the position $x$. Therefore, if $a \geq b$, the right boundary can be $x+b$.

If $a < b$, that is, the distance to jump forward is less than the distance to jump backward, then if the position of the flea minus $b$ exceeds $2000$, choose to jump backward, otherwise jump forward. Therefore, if $a < b$, the right boundary does not exceed $6000$.

In summary, we can set the right boundary to $6000$.

Next, we use BFS to search for the shortest path. We use a queue, initially adding the position and jumping direction of the flea as the state to the queue. Each time we take a state from the queue, if the position of this state is equal to $x$, then we have found a path from the initial state to the target state, and we can return the current number of steps. Otherwise, we add the next state of the current state to the queue. There are two cases for the next state:

- Jump forward, the jumping direction is $1$;
- When the current jumping direction is $1$, jump backward, the jumping direction is $0$.

Note that we need to judge whether the next state is legal, that is, the position of the next state does not exceed the right boundary, is not in the forbidden position, and has not been visited.

If the queue is empty, it means that the target position cannot be reached, return $-1$.

The time complexity is $O(M)$, and the space complexity is $O(M)$. Here, $M$ is the right boundary, and in this problem, $M \leq 6000$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        s = set(forbidden)
        q = deque([(0, 1)])
        vis = {(0, 1)}
        ans = 0
        while q:
            for _ in range(len(q)):
                i, k = q.popleft()
                if i == x:
                    return ans
                nxt = [(i + a, 1)]
                if k & 1:
                    nxt.append((i - b, 0))
                for j, k in nxt:
                    if 0 <= j < 6000 and j not in s and (j, k) not in vis:
                        q.append((j, k))
                        vis.add((j, k))
            ans += 1
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
