---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1601.Maximum%20Number%20of%20Achievable%20Transfer%20Requests/README_EN.md
rating: 2118
source: Weekly Contest 208 Q4
tags:
    - Bit Manipulation
    - Array
    - Backtracking
    - Enumeration
---

<!-- problem:start -->

# [1601. Maximum Number of Achievable Transfer Requests](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests)

## Description

<!-- description:start -->

<p>We have <code>n</code> buildings numbered from <code>0</code> to <code>n - 1</code>. Each building has a number of employees. It&#39;s transfer season, and some employees want to change the building they reside in.</p>

<p>You are given an array <code>requests</code> where <code>requests[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> represents an employee&#39;s request to transfer from building <code>from<sub>i</sub></code> to building <code>to<sub>i</sub></code>.</p>

<p><strong>All buildings are full</strong>, so a list of requests is achievable only if for each building, the <strong>net change in employee transfers is zero</strong>. This means the number of employees <strong>leaving</strong> is <strong>equal</strong> to the number of employees <strong>moving in</strong>. For example if <code>n = 3</code> and two employees are leaving building <code>0</code>, one is leaving building <code>1</code>, and one is leaving building <code>2</code>, there should be two employees moving to building <code>0</code>, one employee moving to building <code>1</code>, and one employee moving to building <code>2</code>.</p>

<p>Return <em>the maximum number of achievable requests</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1601.Maximum%20Number%20of%20Achievable%20Transfer%20Requests/images/move1.jpg" style="width: 600px; height: 406px;" />
<pre>
<strong>Input:</strong> n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
<strong>Output:</strong> 5
<strong>Explantion:</strong> Let&#39;s see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don&#39;t have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1601.Maximum%20Number%20of%20Achievable%20Transfer%20Requests/images/move2.jpg" style="width: 450px; height: 327px;" />
<pre>
<strong>Input:</strong> n = 3, requests = [[0,0],[1,2],[2,1]]
<strong>Output:</strong> 3
<strong>Explantion:</strong> Let&#39;s see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests. </pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= requests.length &lt;= 16</code></li>
	<li><code>requests[i].length == 2</code></li>
	<li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub> &lt; n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Enumeration

We note that the length of the room change request list does not exceed $16$. Therefore, we can use the method of binary enumeration to enumerate all room change request lists. Specifically, we can use a binary number of length $16$ to represent a room change request list, where the $i$-th bit being $1$ means the $i$-th room change request is selected, and $0$ means the $i$-th room change request is not selected.

We enumerate all binary numbers in the range of $[1, 2^{m})$, for each binary number $mask$, we first calculate how many $1$s are in its binary representation, denoted as $cnt$. If $cnt$ is larger than the current answer $ans$, then we judge whether $mask$ is a feasible room change request list. If it is, then we update the answer $ans$ with $cnt$. To judge whether $mask$ is a feasible room change request list, we only need to check whether the net inflow of each room is $0$.

The time complexity is $O(2^m \times (m + n))$, and the space complexity is $O(n)$, where $m$ and $n$ are the lengths of the room change request list and the number of rooms, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def check(mask: int) -> bool:
            cnt = [0] * n
            for i, (f, t) in enumerate(requests):
                if mask >> i & 1:
                    cnt[f] -= 1
                    cnt[t] += 1
            return all(v == 0 for v in cnt)

        ans = 0
        for mask in range(1 << len(requests)):
            cnt = mask.bit_count()
            if ans < cnt and check(mask):
                ans = cnt
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
