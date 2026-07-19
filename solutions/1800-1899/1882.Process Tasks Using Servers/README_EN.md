---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1882.Process%20Tasks%20Using%20Servers/README_EN.md
rating: 1979
source: Weekly Contest 243 Q3
tags:
    - Array
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1882. Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> integer arrays <code>servers</code> and <code>tasks</code> of lengths <code>n</code>​​​​​​ and <code>m</code>​​​​​​ respectively. <code>servers[i]</code> is the <strong>weight</strong> of the <code>i<sup>​​​​​​th</sup></code>​​​​ server, and <code>tasks[j]</code> is the <strong>time needed</strong> to process the <code>j<sup>​​​​​​th</sup></code>​​​​ task <strong>in seconds</strong>.</p>

<p>Tasks are assigned to the servers using a <strong>task queue</strong>. Initially, all servers are free, and the queue is <strong>empty</strong>.</p>

<p>At second <code>j</code>, the <code>j<sup>th</sup></code> task is <strong>inserted</strong> into the queue (starting with the <code>0<sup>th</sup></code> task being inserted at second <code>0</code>). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the <strong>smallest weight</strong>, and in case of a tie, it is assigned to a free server with the <strong>smallest index</strong>.</p>

<p>If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned <strong>in order of insertion</strong> following the weight and index priorities above.</p>

<p>A server that is assigned task <code>j</code> at second <code>t</code> will be free again at second <code>t + tasks[j]</code>.</p>

<p>Build an array <code>ans</code>​​​​ of length <code>m</code>, where <code>ans[j]</code> is the <strong>index</strong> of the server the <code>j<sup>​​​​​​th</sup></code> task will be assigned to.</p>

<p>Return <em>the array </em><code>ans</code>​​​​.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> servers = [3,3,2], tasks = [1,2,3,2,1,2]
<strong>Output:</strong> [2,2,0,2,1,2]
<strong>Explanation: </strong>Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
<strong>Output:</strong> [1,4,1,4,1,3,2]
<strong>Explanation: </strong>Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>servers.length == n</code></li>
	<li><code>tasks.length == m</code></li>
	<li><code>1 &lt;= n, m &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= servers[i], tasks[j] &lt;= 2 * 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Min-Heap)

We use a min-heap $\textit{idle}$ to maintain all idle servers, where each element is a tuple $(x, i)$ representing the $i$-th server with weight $x$. We use another min-heap $\textit{busy}$ to maintain all busy servers, where each element is a tuple $(w, s, i)$ representing the $i$-th server that will be idle at time $w$ with weight $s$. Initially, we add all servers to $\textit{idle}$.

Next, we iterate through all tasks. For the $j$-th task, we first remove all servers from $\textit{busy}$ that will be idle at or before time $j$ and add them to $\textit{idle}$. Then we take the server with the smallest weight from $\textit{idle}$, add it to $\textit{busy}$, and assign it to the $j$-th task. If $\textit{idle}$ is empty, we take the server with the earliest idle time from $\textit{busy}$, add it to $\textit{busy}$, and assign it to the $j$-th task.

After iterating through all tasks, we obtain the answer array $\textit{ans}$.

The time complexity is $O((n + m) \log n)$, where $n$ is the number of servers and $m$ is the number of tasks. The space complexity is $O(n)$. Here, $n$ and $m$ are the number of servers and tasks, respectively.

Similar problems:

- [2402. Meeting Rooms III](https://github.com/doocs/leetcode/blob/main/solution/2400-2499/2402.Meeting%20Rooms%20III/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        idle = [(x, i) for i, x in enumerate(servers)]
        heapify(idle)
        busy = []
        ans = []
        for j, t in enumerate(tasks):
            while busy and busy[0][0] <= j:
                _, s, i = heappop(busy)
                heappush(idle, (s, i))
            if idle:
                s, i = heappop(idle)
                heappush(busy, (j + t, s, i))
            else:
                w, s, i = heappop(busy)
                heappush(busy, (w + t, s, i))
            ans.append(i)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
