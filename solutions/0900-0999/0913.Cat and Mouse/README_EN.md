---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0913.Cat%20and%20Mouse/README_EN.md
tags:
    - Graph
    - Topological Sort
    - Memoization
    - Math
    - Dynamic Programming
    - Game Theory
---

<!-- problem:start -->

# [913. Cat and Mouse](https://leetcode.com/problems/cat-and-mouse)

## Description

<!-- description:start -->

<p>A game on an <strong>undirected</strong> graph is played by two players, Mouse and Cat, who alternate turns.</p>

<p>The graph is given as follows: <code>graph[a]</code> is a list of all nodes <code>b</code> such that <code>ab</code> is an edge of the graph.</p>

<p>The mouse starts at node <code>1</code> and goes first, the cat starts at node <code>2</code> and goes second, and there is a hole at node <code>0</code>.</p>

<p>During each player&#39;s turn, they <strong>must</strong> travel along one&nbsp;edge of the graph that meets where they are.&nbsp; For example, if the Mouse is at node 1, it <strong>must</strong> travel to any node in <code>graph[1]</code>.</p>

<p>Additionally, it is not allowed for the Cat to travel to the Hole (node <code>0</code>).</p>

<p>Then, the game can end in three&nbsp;ways:</p>

<ul>
	<li>If ever the Cat occupies the same node as the Mouse, the Cat wins.</li>
	<li>If ever the Mouse reaches the Hole, the Mouse wins.</li>
	<li>If ever a position is repeated (i.e., the players are in the same position as a previous turn, and&nbsp;it is the same player&#39;s turn to move), the game is a draw.</li>
</ul>

<p>Given a <code>graph</code>, and assuming both players play optimally, return</p>

<ul>
	<li><code>1</code>&nbsp;if the mouse wins the game,</li>
	<li><code>2</code>&nbsp;if the cat wins the game, or</li>
	<li><code>0</code>&nbsp;if the game is a draw.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0913.Cat%20and%20Mouse/images/cat1.jpg" style="width: 300px; height: 300px;" />
<pre>
<strong>Input:</strong> graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0913.Cat%20and%20Mouse/images/cat2.jpg" style="width: 200px; height: 200px;" />
<pre>
<strong>Input:</strong> graph = [[1,3],[0],[3],[0,2]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= graph.length &lt;= 50</code></li>
	<li><code>1&nbsp;&lt;= graph[i].length &lt; graph.length</code></li>
	<li><code>0 &lt;= graph[i][j] &lt; graph.length</code></li>
	<li><code>graph[i][j] != i</code></li>
	<li><code>graph[i]</code> is unique.</li>
	<li>The mouse and the cat can always move.&nbsp;</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Topological Sorting

According to the problem description, the state of the game is determined by the position of the mouse, the position of the cat, and the player who is moving. The outcome can be directly determined in the following situations:

- When the positions of the cat and the mouse are the same, the cat wins. This is a winning state for the cat and a losing state for the mouse.
- When the mouse is at the hole, the mouse wins. This is a winning state for the mouse and a losing state for the cat.

To determine the result of the initial state, we need to traverse all states starting from the boundary states. Each state includes the position of the mouse, the position of the cat, and the player who is moving. Based on the current state, we can determine all possible states from the previous round. The player who moved in the previous round is the opposite of the player who is moving in the current state, and the positions of the players in the previous round are different from their positions in the current state.

We use the tuple $(m, c, t)$ to represent the current state and $(pm, pc, pt)$ to represent a possible state from the previous round. The possible states from the previous round are:

- If the player moving in the current round is the mouse, then the player moving in the previous round is the cat. The position of the mouse in the previous round is the same as the current position of the mouse, and the position of the cat in the previous round is any adjacent node of the current position of the cat.
- If the player moving in the current round is the cat, then the player moving in the previous round is the mouse. The position of the cat in the previous round is the same as the current position of the cat, and the position of the mouse in the previous round is any adjacent node of the current position of the mouse.

Initially, all states except the boundary states are unknown. Starting from the boundary states, for each state, we determine all possible states from the previous round and update the results. The update logic is as follows:

1. If the player moving in the previous round is the same as the winner in the current round, then the player moving in the previous round can reach the current state and win. We directly update the state of the previous round to the winner of the current round.
2. If the player moving in the previous round is different from the winner in the current round, and all states that the player moving in the previous round can reach are losing states for that player, then we update the state of the previous round to the winner of the current round.

For the second update logic, we need to record the degree of each state. Initially, the degree of each state represents the number of nodes the player moving in that state can move to, which is the number of adjacent nodes of the node where the player is located. If the player is the cat and the node is adjacent to the hole, the degree of that state is reduced by $1$.

When all states have been updated, the result of the initial state is the final result.

The time complexity is $O(n^3)$, and the space complexity is $O(n^2)$. Here, $n$ is the number of nodes in the graph.

<!-- tabs:start -->

#### Python3

```python
HOLE, MOUSE_START, CAT_START = 0, 1, 2
MOUSE_TURN, CAT_TURN = 0, 1
MOUSE_WIN, CAT_WIN, TIE = 1, 2, 0

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def get_prev_states(state):
            m, c, t = state
            pt = t ^ 1
            pre = []
            if pt == CAT_TURN:
                for pc in graph[c]:
                    if pc != HOLE:
                        pre.append((m, pc, pt))
            else:
                for pm in graph[m]:
                    pre.append((pm, c, pt))
            return pre

        n = len(graph)
        ans = [[[0, 0] for _ in range(n)] for _ in range(n)]
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                degree[i][j][MOUSE_TURN] = len(graph[i])
                degree[i][j][CAT_TURN] = len(graph[j])
            for j in graph[HOLE]:
                degree[i][j][CAT_TURN] -= 1
        q = deque()
        for j in range(1, n):
            ans[0][j][MOUSE_TURN] = ans[0][j][CAT_TURN] = MOUSE_WIN
            q.append((0, j, MOUSE_TURN))
            q.append((0, j, CAT_TURN))
        for i in range(1, n):
            ans[i][i][MOUSE_TURN] = ans[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))
        while q:
            state = q.popleft()
            t = ans[state[0]][state[1]][state[2]]
            for prev_state in get_prev_states(state):
                pm, pc, pt = prev_state
                if ans[pm][pc][pt] == TIE:
                    win = (t == MOUSE_WIN and pt == MOUSE_TURN) or (
                        t == CAT_WIN and pt == CAT_TURN
                    )
                    if win:
                        ans[pm][pc][pt] = t
                        q.append(prev_state)
                    else:
                        degree[pm][pc][pt] -= 1
                        if degree[pm][pc][pt] == 0:
                            ans[pm][pc][pt] = t
                            q.append(prev_state)
        return ans[MOUSE_START][CAT_START][MOUSE_TURN]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
