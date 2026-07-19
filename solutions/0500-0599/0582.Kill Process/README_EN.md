---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0500-0599/0582.Kill%20Process/README_EN.md
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Array
    - Hash Table
---

<!-- problem:start -->

# [582. Kill Process 🔒](https://leetcode.com/problems/kill-process)

## Description

<!-- description:start -->

<p>You have <code>n</code> processes forming a rooted tree structure. You are given two integer arrays <code>pid</code> and <code>ppid</code>, where <code>pid[i]</code> is the ID of the <code>i<sup>th</sup></code> process and <code>ppid[i]</code> is the ID of the <code>i<sup>th</sup></code> process&#39;s parent process.</p>

<p>Each process has only <strong>one parent process</strong> but may have multiple children processes. Only one process has <code>ppid[i] = 0</code>, which means this process has <strong>no parent process</strong> (the root of the tree).</p>

<p>When a process is <strong>killed</strong>, all of its children processes will also be killed.</p>

<p>Given an integer <code>kill</code> representing the ID of a process you want to kill, return <em>a list of the IDs of the processes that will be killed. You may return the answer in <strong>any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0582.Kill%20Process/images/ptree.jpg" style="width: 207px; height: 302px;" />
<pre>
<strong>Input:</strong> pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
<strong>Output:</strong> [5,10]
<strong>Explanation:</strong>&nbsp;The processes colored in red are the processes that should be killed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> pid = [1], ppid = [0], kill = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == pid.length</code></li>
	<li><code>n == ppid.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= pid[i] &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ppid[i] &lt;= 5 * 10<sup>4</sup></code></li>
	<li>Only one process has no parent.</li>
	<li>All the values of <code>pid</code> are <strong>unique</strong>.</li>
	<li><code>kill</code> is <strong>guaranteed</strong> to be in <code>pid</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

We first construct a graph $g$ based on $pid$ and $ppid$, where $g[i]$ represents all child processes of process $i$. Then, starting from the process $kill$, we perform depth-first search to obtain all killed processes.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of processes.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def dfs(i: int):
            ans.append(i)
            for j in g[i]:
                dfs(j)

        g = defaultdict(list)
        for i, p in zip(pid, ppid):
            g[p].append(i)
        ans = []
        dfs(kill)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
