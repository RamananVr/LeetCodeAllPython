---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2532.Time%20to%20Cross%20a%20Bridge/README_EN.md
rating: 2588
source: Weekly Contest 327 Q4
tags:
    - Array
    - Simulation
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2532. Time to Cross a Bridge](https://leetcode.com/problems/time-to-cross-a-bridge)

## Description

<!-- description:start -->

<p>There are <code>k</code> workers who want to move <code>n</code> boxes from the right (old) warehouse to the left (new) warehouse. You are given the two integers <code>n</code> and <code>k</code>, and a 2D integer array <code>time</code> of size <code>k x 4</code> where <code>time[i] = [right<sub>i</sub>, pick<sub>i</sub>, left<sub>i</sub>, put<sub>i</sub>]</code>.</p>

<p>The warehouses are separated by a river and connected by a bridge. Initially, all <code>k</code> workers are waiting on the left side of the bridge. To move the boxes, the <code>i<sup>th</sup></code> worker can do the following:</p>

<ul>
	<li>Cross the bridge to the right side in <code>right<sub>i</sub></code> minutes.</li>
	<li>Pick a box from the right warehouse in <code>pick<sub>i</sub></code> minutes.</li>
	<li>Cross the bridge to the left side in <code>left<sub>i</sub></code> minutes.</li>
	<li>Put the box into the left warehouse in <code>put<sub>i</sub></code> minutes.</li>
</ul>

<p>The <code>i<sup>th</sup></code> worker is <strong>less efficient</strong> than the j<code><sup>th</sup></code> worker if either condition is met:</p>

<ul>
	<li><code>left<sub>i</sub> + right<sub>i</sub> &gt; left<sub>j</sub> + right<sub>j</sub></code></li>
	<li><code>left<sub>i</sub> + right<sub>i</sub> == left<sub>j</sub> + right<sub>j</sub></code> and <code>i &gt; j</code></li>
</ul>

<p>The following rules regulate the movement of the workers through the bridge:</p>

<ul>
	<li>Only one worker can use the bridge at a time.</li>
	<li>When the bridge is unused prioritize the <strong>least efficient</strong> worker (who have picked up the box) on the right side to cross. If not,&nbsp;prioritize the <strong>least efficient</strong> worker on the left side to cross.</li>
	<li>If enough workers have already been dispatched from the left side to pick up all the remaining boxes, <strong>no more</strong> workers will be sent from the left side.</li>
</ul>

<p>Return the <strong>elapsed minutes</strong> at which the last box reaches the <strong>left side of the bridge</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<pre>
From 0 to 1 minutes: worker 2 crosses the bridge to the right.
From 1 to 2 minutes: worker 2 picks up a box from the right warehouse.
From 2 to 6 minutes: worker 2 crosses the bridge to the left.
From 6 to 7 minutes: worker 2 puts a box at the left warehouse.
The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left side of the bridge.
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, k = 2, time =</span> [[1,5,1,8],[10,10,10,10]]</p>

<p><strong>Output:</strong> 37</p>

<p><strong>Explanation:</strong></p>

<pre>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2500-2599/2532.Time%20to%20Cross%20a%20Bridge/images/378539249-c6ce3c73-40e7-4670-a8b5-7ddb9abede11.png" style="width: 450px; height: 176px;" />
</pre>

<p>The last box reaches the left side at 37 seconds. Notice, how we <strong>do not</strong> put the last boxes down, as that would take more time, and they are already on the left with the workers.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 10<sup>4</sup></code></li>
	<li><code>time.length == k</code></li>
	<li><code>time[i].length == 4</code></li>
	<li><code>1 &lt;= left<sub>i</sub>, pick<sub>i</sub>, right<sub>i</sub>, put<sub>i</sub> &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Max-Heap and Min-Heap) + Simulation

First, we sort the workers by efficiency in descending order, so the worker with the highest index has the lowest efficiency.

Next, we use four priority queues to simulate the state of the workers:

- `wait_in_left`: Max-heap, storing the indices of workers currently waiting on the left bank;
- `wait_in_right`: Max-heap, storing the indices of workers currently waiting on the right bank;
- `work_in_left`: Min-heap, storing the time when workers currently working on the left bank finish placing boxes and the indices of the workers;
- `work_in_right`: Min-heap, storing the time when workers currently working on the right bank finish picking up boxes and the indices of the workers.

Initially, all workers are on the left bank, so `wait_in_left` stores the indices of all workers. We use the variable `cur` to record the current time.

Then, we simulate the entire process. First, we check if any worker in `work_in_left` has finished placing boxes at the current time. If so, we move the worker to `wait_in_left` and remove the worker from `work_in_left`. Similarly, we check if any worker in `work_in_right` has finished picking up boxes. If so, we move the worker to `wait_in_right` and remove the worker from `work_in_right`.

Next, we check if there are any workers waiting on the left bank at the current time, denoted as `left_to_go`. At the same time, we check if there are any workers waiting on the right bank, denoted as `right_to_go`. If there are no workers waiting to cross the river, we directly update `cur` to the next time when a worker finishes placing boxes and continue the simulation.

If `right_to_go` is `true`, we take a worker from `wait_in_right`, update `cur` to the current time plus the time it takes for the worker to cross from the right bank to the left bank. If all workers have crossed to the right bank at this point, we directly return `cur` as the answer; otherwise, we move the worker to `work_in_left`.

If `left_to_go` is `true`, we take a worker from `wait_in_left`, update `cur` to the current time plus the time it takes for the worker to cross from the left bank to the right bank, then move the worker to `work_in_right` and decrement the number of boxes.

Repeat the above process until the number of boxes is zero. At this point, `cur` is the answer.

The time complexity is $O(n \times \log k)$, and the space complexity is $O(k)$. Here, $n$ and $k$ are the number of workers and the number of boxes, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        time.sort(key=lambda x: x[0] + x[2])
        cur = 0
        wait_in_left, wait_in_right = [], []
        work_in_left, work_in_right = [], []
        for i in range(k):
            heappush(wait_in_left, -i)
        while 1:
            while work_in_left:
                t, i = work_in_left[0]
                if t > cur:
                    break
                heappop(work_in_left)
                heappush(wait_in_left, -i)
            while work_in_right:
                t, i = work_in_right[0]
                if t > cur:
                    break
                heappop(work_in_right)
                heappush(wait_in_right, -i)
            left_to_go = n > 0 and wait_in_left
            right_to_go = bool(wait_in_right)
            if not left_to_go and not right_to_go:
                nxt = inf
                if work_in_left:
                    nxt = min(nxt, work_in_left[0][0])
                if work_in_right:
                    nxt = min(nxt, work_in_right[0][0])
                cur = nxt
                continue
            if right_to_go:
                i = -heappop(wait_in_right)
                cur += time[i][2]
                if n == 0 and not wait_in_right and not work_in_right:
                    return cur
                heappush(work_in_left, (cur + time[i][3], i))
            else:
                i = -heappop(wait_in_left)
                cur += time[i][0]
                n -= 1
                heappush(work_in_right, (cur + time[i][1], i))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
