---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2402.Meeting%20Rooms%20III/README_EN.md
rating: 2092
source: Weekly Contest 309 Q4
tags:
    - Array
    - Hash Table
    - Sorting
    - Simulation
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code>. There are <code>n</code> rooms numbered from <code>0</code> to <code>n - 1</code>.</p>

<p>You are given a 2D integer array <code>meetings</code> where <code>meetings[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> means that a meeting will be held during the <strong>half-closed</strong> time interval <code>[start<sub>i</sub>, end<sub>i</sub>)</code>. All the values of <code>start<sub>i</sub></code> are <strong>unique</strong>.</p>

<p>Meetings are allocated to rooms in the following manner:</p>

<ol>
	<li>Each meeting will take place in the unused room with the <strong>lowest</strong> number.</li>
	<li>If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the <strong>same</strong> duration as the original meeting.</li>
	<li>When a room becomes unused, meetings that have an earlier original <strong>start</strong> time should be given the room.</li>
</ol>

<p>Return<em> the <strong>number</strong> of the room that held the most meetings. </em>If there are multiple rooms, return<em> the room with the <strong>lowest</strong> number.</em></p>

<p>A <strong>half-closed interval</strong> <code>[a, b)</code> is the interval between <code>a</code> and <code>b</code> <strong>including</strong> <code>a</code> and <strong>not including</strong> <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= meetings.length &lt;= 10<sup>5</sup></code></li>
	<li><code>meetings[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>5</sup></code></li>
	<li>All the values of <code>start<sub>i</sub></code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Min-Heap)

We define two priority queues to represent idle meeting rooms and busy meeting rooms respectively. The idle meeting rooms $\textit{idle}$ are sorted by **index**; the busy meeting rooms $\textit{busy}$ are sorted by **end time and index**.

First, sort the meetings by start time, then iterate through the meetings. For each meeting:

- If there are busy meeting rooms with end time less than or equal to the current meeting's start time, add them to the idle meeting rooms queue $\textit{idle}$;
- If there are idle meeting rooms available, take the room with the smallest index from the idle queue $\textit{idle}$ and add it to the busy queue $\textit{busy}$;
- If there are no idle meeting rooms, find the room with the earliest end time and smallest index from the busy queue $\textit{busy}$, and add it back to the busy queue $\textit{busy}$.

The time complexity is $O(m (\log m + \log n))$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the number of meeting rooms and meetings respectively.

Similar problems:

- [1882. Process Tasks Using Servers](https://github.com/doocs/leetcode/blob/main/solution/1800-1899/1882.Process%20Tasks%20Using%20Servers/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        busy = []
        idle = list(range(n))
        heapify(idle)
        cnt = [0] * n
        for s, e in meetings:
            while busy and busy[0][0] <= s:
                heappush(idle, heappop(busy)[1])
            i = 0
            if idle:
                i = heappop(idle)
                heappush(busy, (e, i))
            else:
                time_end, i = heappop(busy)
                heappush(busy, (time_end + e - s, i))
            cnt[i] += 1
        ans = 0
        for i in range(n):
            if cnt[ans] < cnt[i]:
                ans = i
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
