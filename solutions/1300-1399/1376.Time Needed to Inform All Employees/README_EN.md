---
comments: true
difficulty: Medium
rating: 1561
source: Weekly Contest 179 Q3
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
---

<!-- problem:start -->

# [1376. Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees)

## Description

<!-- description:start -->

<p>A company has <code>n</code> employees with a unique ID for each employee from <code>0</code> to <code>n - 1</code>. The head of the company is the one with <code>headID</code>.</p>

<p>Each employee has one direct manager given in the <code>manager</code> array where <code>manager[i]</code> is the direct manager of the <code>i-th</code> employee, <code>manager[headID] = -1</code>. Also, it is guaranteed that the subordination relationships have a tree structure.</p>

<p>The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.</p>

<p>The <code>i-th</code> employee needs <code>informTime[i]</code> minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).</p>

<p>Return <em>the number of minutes</em> needed to inform all the employees about the urgent news.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1, headID = 0, manager = [-1], informTime = [0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The head of the company is the only employee in the company.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1376.Time%20Needed%20to%20Inform%20All%20Employees/images/graph.png" style="width: 404px; height: 174px;" />
<pre>
<strong>Input:</strong> n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= headID &lt; n</code></li>
	<li><code>manager.length == n</code></li>
	<li><code>0 &lt;= manager[i] &lt; n</code></li>
	<li><code>manager[headID] == -1</code></li>
	<li><code>informTime.length == n</code></li>
	<li><code>0 &lt;= informTime[i] &lt;= 1000</code></li>
	<li><code>informTime[i] == 0</code> if employee <code>i</code> has no subordinates.</li>
	<li>It is <strong>guaranteed</strong> that all the employees can be informed.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: DFS

<!-- thinking:start -->

> **Thinking**
>
> In a tree of managers, a message starts at the head; an edge costs that employee's inform time. $n \le 10^5$ forbids summing a path per leaf. After building the child list, $dfs(i)$ is the time for $i$ to inform its whole subtree: $\textit{informTime}[i]$ plus the slowest $dfs(j)$ among direct reports. The answer is $dfs(\textit{headID})$.

<!-- thinking:end -->

We first build an adjacent list $g$ according to the $manager$ array, where $g[i]$ represents all direct subordinates of employee $i$.

Next, we design a function $dfs(i)$, which means the time required for employee $i$ to notify all his subordinates (including direct subordinates and indirect subordinates), and then the answer is $dfs(headID)$.

In function $dfs(i)$, we need to traverse all direct subordinates $j$ of $i$. For each subordinate, employee $i$ needs to notify him, which takes $informTime[i]$ time, and his subordinates need to notify their subordinates, which takes $dfs(j)$ time. We take the maximum value of $informTime[i] + dfs(j)$ as the return value of function $dfs(i)$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of employees.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        def dfs(i: int) -> int:
            ans = 0
            for j in g[i]:
                ans = max(ans, dfs(j) + informTime[i])
            return ans

        g = defaultdict(list)
        for i, x in enumerate(manager):
            g[x].append(i)
        return dfs(headID)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Explicit Stack

<!-- thinking:start -->

> **Thinking**
>
> The reporting lines form a tree rooted at the head, and an edge costs that employee's inform time. With $n \le 10^5$, recursing from the head to score every subtree is too deep: a chain makes the call depth $n$.
>
> The time for employee $i$ to inform a whole subtree is $i$'s own inform time plus the slowest direct report. A leaf has no reports, so that time is $0$. The value depends only on results that are already known for the children.
>
> An explicit stack starts at $\textit{headID}$ and walks $(employee, state)$ in postorder. On entry we push the exit marker and then the reports, and on exit we store the maximum of $\textit{informTime}[i] + \textit{time}[j]$. The head's time is the answer.

<!-- thinking:end -->

We first build an adjacent list $g$ according to the $manager$ array, where $g[i]$ represents all direct subordinates of employee $i$.

The time for employee $i$ to inform the whole subtree is $\textit{informTime}[i]$ plus the maximum time among the direct reports, or $0$ when there are no reports. An explicit stack walks from $\textit{headID}$ in postorder and writes that time when the node is left. The answer is the head's time.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of employees.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        for i, x in enumerate(manager):
            if x != -1:
                g[x].append(i)
        time = [0] * n
        stk = [(headID, 0)]
        while stk:
            i, state = stk.pop()
            if state == 0:
                stk.append((i, 1))
                for j in g[i]:
                    stk.append((j, 0))
            else:
                ans = 0
                for j in g[i]:
                    ans = max(ans, time[j] + informTime[i])
                time[i] = ans
        return time[headID]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
