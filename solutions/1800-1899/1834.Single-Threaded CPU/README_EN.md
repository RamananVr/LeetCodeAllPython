---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1834.Single-Threaded%20CPU/README_EN.md
rating: 1797
source: Weekly Contest 237 Q3
tags:
    - Array
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1834. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu)

## Description

<!-- description:start -->

<p>You are given <code>n</code>​​​​​​ tasks labeled from <code>0</code> to <code>n - 1</code> represented by a 2D integer array <code>tasks</code>, where <code>tasks[i] = [enqueueTime<sub>i</sub>, processingTime<sub>i</sub>]</code> means that the <code>i<sup>​​​​​​th</sup></code>​​​​ task will be available to process at <code>enqueueTime<sub>i</sub></code> and will take <code>processingTime<sub>i</sub></code><sub> </sub>to finish processing.</p>

<p>You have a single-threaded CPU that can process <strong>at most one</strong> task at a time and will act in the following way:</p>

<ul>
	<li>If the CPU is idle and there are no available tasks to process, the CPU remains idle.</li>
	<li>If the CPU is idle and there are available tasks, the CPU will choose the one with the <strong>shortest processing time</strong>. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.</li>
	<li>Once a task is started, the CPU will <strong>process the entire task</strong> without stopping.</li>
	<li>The CPU can finish a task then start a new one instantly.</li>
</ul>

<p>Return <em>the order in which the CPU will process the tasks.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tasks = [[1,2],[2,4],[3,2],[4,1]]
<strong>Output:</strong> [0,2,3,1]
<strong>Explanation: </strong>The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
<strong>Output:</strong> [4,3,2,0,1]
<strong>Explanation</strong><strong>: </strong>The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>tasks.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= enqueueTime<sub>i</sub>, processingTime<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Priority Queue (Min Heap)

First, we sort the tasks by `enqueueTime` in ascending order. Next, we use a priority queue (min heap) to maintain the currently executable tasks. The elements in the queue are `(processingTime, index)`, which represent the execution time and the index of the task. We also use a variable $t$ to represent the current time, initially set to $0$.

Next, we simulate the execution process of the tasks.

If the current queue is empty, it means there are no executable tasks at the moment. We update $t$ to the larger value between the `enqueueTime` of the next task and the current time $t$. Then, we add all tasks with `enqueueTime` less than or equal to $t$ to the queue.

Then, we take out a task from the queue, add its index to the answer array, and update $t$ to the sum of the current time $t$ and the execution time of the current task.

We repeat the above process until the queue is empty and all tasks have been added to the queue.

The time complexity is $O(n \times \log n)$, where $n$ is the number of tasks.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        ans = []
        q = []
        n = len(tasks)
        i = t = 0
        while q or i < n:
            if not q:
                t = max(t, tasks[i][0])
            while i < n and tasks[i][0] <= t:
                heappush(q, (tasks[i][1], tasks[i][2]))
                i += 1
            pt, j = heappop(q)
            ans.append(j)
            t += pt
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
