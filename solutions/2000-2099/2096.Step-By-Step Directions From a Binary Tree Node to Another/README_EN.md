---
comments: true
difficulty: Medium
rating: 1804
source: Weekly Contest 270 Q3
tags:
    - Tree
    - Depth-First Search
    - String
    - Binary Tree
    - Lowest Common Ancestor
    - Binary Lifting
---

<!-- problem:start -->

# [2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another)

## Description

<!-- description:start -->

<p>You are given the <code>root</code> of a <strong>binary tree</strong> with <code>n</code> nodes. Each node is uniquely assigned a value from <code>1</code> to <code>n</code>. You are also given an integer <code>startValue</code> representing the value of the start node <code>s</code>, and a different integer <code>destValue</code> representing the value of the destination node <code>t</code>.</p>

<p>Find the <strong>shortest path</strong> starting from node <code>s</code> and ending at node <code>t</code>. Generate step-by-step directions of such path as a string consisting of only the <strong>uppercase</strong> letters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, and <code>&#39;U&#39;</code>. Each letter indicates a specific direction:</p>

<ul>
	<li><code>&#39;L&#39;</code> means to go from a node to its <strong>left child</strong> node.</li>
	<li><code>&#39;R&#39;</code> means to go from a node to its <strong>right child</strong> node.</li>
	<li><code>&#39;U&#39;</code> means to go from a node to its <strong>parent</strong> node.</li>
</ul>

<p>Return <em>the step-by-step directions of the <strong>shortest path</strong> from node </em><code>s</code><em> to node</em> <code>t</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2096.Step-By-Step%20Directions%20From%20a%20Binary%20Tree%20Node%20to%20Another/images/eg1.png" style="width: 214px; height: 163px;" />
<pre>
<strong>Input:</strong> root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
<strong>Output:</strong> &quot;UURL&quot;
<strong>Explanation:</strong> The shortest path is: 3 &rarr; 1 &rarr; 5 &rarr; 2 &rarr; 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2096.Step-By-Step%20Directions%20From%20a%20Binary%20Tree%20Node%20to%20Another/images/eg2.png" style="width: 74px; height: 102px;" />
<pre>
<strong>Input:</strong> root = [2,1], startValue = 2, destValue = 1
<strong>Output:</strong> &quot;L&quot;
<strong>Explanation:</strong> The shortest path is: 2 &rarr; 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= Node.val &lt;= n</code></li>
	<li>All the values in the tree are <strong>unique</strong>.</li>
	<li><code>1 &lt;= startValue, destValue &lt;= n</code></li>
	<li><code>startValue != destValue</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Lowest Common Ancestor + DFS

<!-- thinking:start -->

> **Thinking**
>
> The unique path goes through the LCA. Upward edges become `U`; the descent uses `L`/`R`. Three tree walks are fine for $n \le 10^5$.
>
> Find the LCA, DFS both directions from it, replace the start path by `U`s, and concatenate.

<!-- thinking:end -->

We can first find the lowest common ancestor of nodes $\textit{startValue}$ and $\textit{destValue}$, denoted as $\textit{node}$. Then, starting from $\textit{node}$, we find the paths to $\textit{startValue}$ and $\textit{destValue}$ respectively. The path from $\textit{startValue}$ to $\textit{node}$ will consist of a number of $\textit{U}$s, and the path from $\textit{node}$ to $\textit{destValue}$ will be the $\textit{path}$. Finally, we concatenate these two paths.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def lca(node: Optional[TreeNode], p: int, q: int):
            if node is None or node.val in (p, q):
                return node
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)
            if left and right:
                return node
            return left or right

        def dfs(node: Optional[TreeNode], x: int, path: List[str]):
            if node is None:
                return False
            if node.val == x:
                return True
            path.append("L")
            if dfs(node.left, x, path):
                return True
            path[-1] = "R"
            if dfs(node.right, x, path):
                return True
            path.pop()
            return False

        node = lca(root, startValue, destValue)

        path_to_start = []
        path_to_dest = []

        dfs(node, startValue, path_to_start)
        dfs(node, destValue, path_to_dest)

        return "U" * len(path_to_start) + "".join(path_to_dest)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Lowest Common Ancestor + DFS (Optimized)

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 finds the LCA then walks twice more. Paths from the root share a prefix; stripping it is exactly “up to the LCA then down.” The extra LCA search disappears.
>
> Two DFS strings, skip the common prefix of length $i$, emit $(|start|-i)$ `U`s plus the destination suffix.

<!-- thinking:end -->

We can start from $\textit{root}$, find the paths to $\textit{startValue}$ and $\textit{destValue}$, denoted as $\textit{pathToStart}$ and $\textit{pathToDest}$, respectively. Then, remove the longest common prefix of $\textit{pathToStart}$ and $\textit{pathToDest}$. At this point, the length of $\textit{pathToStart}$ is the number of $\textit{U}$s in the answer, and the path of $\textit{pathToDest}$ is the path in the answer. We just need to concatenate these two paths.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def dfs(node: Optional[TreeNode], x: int, path: List[str]):
            if node is None:
                return False
            if node.val == x:
                return True
            path.append("L")
            if dfs(node.left, x, path):
                return True
            path[-1] = "R"
            if dfs(node.right, x, path):
                return True
            path.pop()
            return False

        path_to_start = []
        path_to_dest = []

        dfs(root, startValue, path_to_start)
        dfs(root, destValue, path_to_dest)
        i = 0
        while (
            i < len(path_to_start)
            and i < len(path_to_dest)
            and path_to_start[i] == path_to_dest[i]
        ):
            i += 1
        return "U" * (len(path_to_start) - i) + "".join(path_to_dest[i:])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Explicit-Stack Lowest Common Ancestor

<!-- thinking:start -->

> **Thinking**
>
> The shortest path goes through the lowest common ancestor. Every step above that ancestor is `U`, and the descent from the ancestor to the destination is `L` or `R`. Three linear walks fit $n \le 10^5$.
>
> Both the ancestor search and the direction search enter the left child first. A left chain can be $n$ nodes long, so recursion overflows before the direction string is finished.
>
> The ancestor is known only after both subtrees return: the current node is the ancestor when both sides found a target, otherwise the non-empty side is passed upward. An explicit stack separates “expand both children” from “both children have returned,” and the direction search pushes a backtrack marker before the left child. A failed left subtree rewrites the last step to `R` and searches the right child, stopping when the target is found.
>
> The length of the start path is the number of `U`s, concatenated with the path from the ancestor to the destination.

<!-- thinking:end -->

An explicit stack finds the lowest common ancestor of $\textit{startValue}$ and $\textit{destValue}$, denoted as $\textit{node}$. State $0$ expands the two children, and state $1$ decides the ancestor after both sides return: the current node when both sides are non-empty, otherwise the non-empty side. The same stack then walks from $\textit{node}$, recording `L` to the left and rewriting that step to `R` when the left subtree misses the target. The number of steps from $\textit{startValue}$ back to $\textit{node}$ is the number of `U`s, followed by the direction string from $\textit{node}$ to $\textit{destValue}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def lca(root: Optional[TreeNode], p: int, q: int):
            ret = {}
            stk = [(root, 0)]
            while stk:
                node, state = stk.pop()
                if state == 0:
                    if node is None:
                        continue
                    if node.val in (p, q):
                        ret[id(node)] = node
                        continue
                    stk.append((node, 1))
                    stk.append((node.right, 0))
                    stk.append((node.left, 0))
                else:
                    left = ret.get(id(node.left)) if node.left is not None else None
                    right = ret.get(id(node.right)) if node.right is not None else None
                    if left and right:
                        ret[id(node)] = node
                    else:
                        ret[id(node)] = left or right
            return ret.get(id(root))

        def dfs(start: Optional[TreeNode], x: int, path: List[str]) -> bool:
            stk = [(start, 0)]
            while stk:
                node, state = stk.pop()
                if state == 0:
                    if node is None:
                        continue
                    if node.val == x:
                        return True
                    path.append('L')
                    stk.append((node, 1))
                    stk.append((node.left, 0))
                elif state == 1:
                    path[-1] = 'R'
                    stk.append((node, 2))
                    stk.append((node.right, 0))
                else:
                    path.pop()
            return False

        node = lca(root, startValue, destValue)
        path_to_start: List[str] = []
        path_to_dest: List[str] = []
        dfs(node, startValue, path_to_start)
        dfs(node, destValue, path_to_dest)
        return 'U' * len(path_to_start) + ''.join(path_to_dest)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 4: Explicit-Stack Root Paths

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 still runs a separate ancestor search and then walks twice from that ancestor. Paths from the root share a prefix, and stripping it is the same as climbing back to the ancestor and then descending, so the dedicated ancestor search can be dropped.
>
> The two direction searches can still follow a chain of length $n$, so they use the same explicit stack: push a backtrack marker, then the left child, and rewrite the last step to `R` when the left subtree fails.
>
> After the common prefix of length $i$ is removed, the answer is $(|\textit{start}|-i)$ `U`s plus the destination suffix.

<!-- thinking:end -->

An explicit stack walks from $\textit{root}$ to $\textit{startValue}$ and to $\textit{destValue}$, producing $\textit{pathToStart}$ and $\textit{pathToDest}$. A failed left subtree rewrites the last step to `R` before the right child is searched, so the strings match the previous depth-first order. After the longest common prefix is removed, the remaining length of $\textit{pathToStart}$ is the number of `U`s, and the remaining part of $\textit{pathToDest}$ is the downward path. Concatenate the two pieces.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

<!-- tabs:start -->

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def dfs(start: Optional[TreeNode], x: int, path: List[str]) -> bool:
            stk = [(start, 0)]
            while stk:
                node, state = stk.pop()
                if state == 0:
                    if node is None:
                        continue
                    if node.val == x:
                        return True
                    path.append('L')
                    stk.append((node, 1))
                    stk.append((node.left, 0))
                elif state == 1:
                    path[-1] = 'R'
                    stk.append((node, 2))
                    stk.append((node.right, 0))
                else:
                    path.pop()
            return False

        path_to_start: List[str] = []
        path_to_dest: List[str] = []
        dfs(root, startValue, path_to_start)
        dfs(root, destValue, path_to_dest)
        i = 0
        while (
            i < len(path_to_start)
            and i < len(path_to_dest)
            and path_to_start[i] == path_to_dest[i]
        ):
            i += 1
        return 'U' * (len(path_to_start) - i) + ''.join(path_to_dest[i:])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
