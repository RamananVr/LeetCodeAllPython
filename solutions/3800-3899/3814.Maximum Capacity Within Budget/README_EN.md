---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3814.Maximum%20Capacity%20Within%20Budget/README_EN.md
rating: 1796
source: Weekly Contest 485 Q2
tags:
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [3814. Maximum Capacity Within Budget](https://leetcode.com/problems/maximum-capacity-within-budget)

## Description

<!-- description:start -->

<p>You are given two integer arrays <code>costs</code> and <code>capacity</code>, both of length <code>n</code>, where <code>costs[i]</code> represents the purchase cost of the <code>i<sup>th</sup></code> machine and <code>capacity[i]</code> represents its performance capacity.</p>

<p>You are also given an integer <code>budget</code>.</p>

<p>You may select <strong>at most two distinct</strong> machines such that the <strong>total cost</strong> of the selected machines is <strong>strictly less</strong> than <code>budget</code>.</p>

<p>Return the <strong>maximum</strong> achievable total capacity of the selected machines.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose two machines with <code>costs[0] = 4</code> and <code>costs[3] = 3</code>.</li>
	<li>The total cost is <code>4 + 3 = 7</code>, which is strictly less than <code>budget = 8</code>.</li>
	<li>The maximum total capacity is <code>capacity[0] + capacity[3] = 1 + 7 = 8</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">costs = [3,5,7,4], capacity = [2,4,3,6], budget = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose one machine with <code>costs[3] = 4</code>.</li>
	<li>The total cost is 4, which is strictly less than <code>budget = 7</code>.</li>
	<li>The maximum total capacity is <code>capacity[3] = 6</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">costs = [2,2,2], capacity = [3,5,4], budget = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose two machines with <code>costs[1] = 2</code> and <code>costs[2] = 2</code>.</li>
	<li>The total cost is <code>2 + 2 = 4</code>, which is strictly less than <code>budget = 5</code>.</li>
	<li>The maximum total capacity is <code>capacity[1] + capacity[2] = 5 + 4 = 9</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == costs.length == capacity.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= costs[i], capacity[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= budget &lt;= 2 * 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Ordered Set

We first filter out all machines with costs less than the budget and sort them by cost in ascending order, recording them in the array $\textit{arr}$, where $\textit{arr}[i] = (\textit{costs}[i], \textit{capacity}[i])$. If $\textit{arr}$ is empty, we cannot buy any machine, so we return $0$.

Otherwise, we can obtain the machine with the maximum capacity in $\textit{arr}$ and initialize the answer with this capacity.

Next, we use a two-pointer approach to iterate through pairs of machines in $\textit{arr}$, using an ordered set $\textit{remain}$ to maintain the capacities of all currently available machines. Initially, $\textit{remain}$ contains the capacities of all machines in $\textit{arr}$.

We use pointers $i$ and $j$ pointing to the beginning and end of $\textit{arr}$, respectively. For each $i$, we remove $\textit{arr}[i]$ from $\textit{remain}$, and then move pointer $j$ until $\textit{arr}[i].\textit{cost} + \textit{arr}[j].\textit{cost} < \textit{budget}$. During this process, we remove the machines that do not satisfy the condition from $\textit{remain}$. At this point, any machine in $\textit{remain}$ can be bought together with $\textit{arr}[i]$. We take the machine with the maximum capacity from $\textit{remain}$, add its capacity to $\textit{arr}[i]$'s capacity, and update the answer. Finally, we return the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of machines.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        arr = []
        for a, b in zip(costs, capacity):
            if a < budget:
                arr.append((a, b))
        if not arr:
            return 0
        arr.sort()
        remain = SortedList()
        for i, (_, b) in enumerate(arr):
            remain.add((b, i))
        i, j = 0, len(arr) - 1
        ans = remain[-1][0]
        while i < j:
            remain.discard((arr[i][1], i))
            while i < j and arr[i][0] + arr[j][0] >= budget:
                remain.discard((arr[j][1], j))
                j -= 1
            if remain:
                ans = max(ans, arr[i][1] + remain[-1][0])
            i += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
