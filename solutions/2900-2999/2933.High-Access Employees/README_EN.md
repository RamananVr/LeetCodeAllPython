---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2933.High-Access%20Employees/README_EN.md
rating: 1536
source: Weekly Contest 371 Q2
tags:
    - Array
    - Hash Table
    - String
    - Sorting
---

<!-- problem:start -->

# [2933. High-Access Employees](https://leetcode.com/problems/high-access-employees)

## Description

<!-- description:start -->

<p>You are given a 2D <strong>0-indexed</strong> array of strings, <code>access_times</code>, with size <code>n</code>. For each <code>i</code> where <code>0 &lt;= i &lt;= n - 1</code>, <code>access_times[i][0]</code> represents the name of an employee, and <code>access_times[i][1]</code> represents the access time of that employee. All entries in <code>access_times</code> are within the same day.</p>

<p>The access time is represented as <strong>four digits</strong> using a <strong>24-hour</strong> time format, for example, <code>&quot;0800&quot;</code> or <code>&quot;2250&quot;</code>.</p>

<p>An employee is said to be <strong>high-access</strong> if he has accessed the system <strong>three or more</strong> times within a <strong>one-hour period</strong>.</p>

<p>Times with exactly one hour of difference are <strong>not</strong> considered part of the same one-hour period. For example, <code>&quot;0815&quot;</code> and <code>&quot;0915&quot;</code> are not part of the same one-hour period.</p>

<p>Access times at the start and end of the day are <strong>not</strong> counted within the same one-hour period. For example, <code>&quot;0005&quot;</code> and <code>&quot;2350&quot;</code> are not part of the same one-hour period.</p>

<p>Return <em>a list that contains the names of <strong>high-access</strong> employees with any order you want.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> access_times = [[&quot;a&quot;,&quot;0549&quot;],[&quot;b&quot;,&quot;0457&quot;],[&quot;a&quot;,&quot;0532&quot;],[&quot;a&quot;,&quot;0621&quot;],[&quot;b&quot;,&quot;0540&quot;]]
<strong>Output:</strong> [&quot;a&quot;]
<strong>Explanation:</strong> &quot;a&quot; has three access times in the one-hour period of [05:32, 06:31] which are 05:32, 05:49, and 06:21.
But &quot;b&quot; does not have more than two access times at all.
So the answer is [&quot;a&quot;].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> access_times = [[&quot;d&quot;,&quot;0002&quot;],[&quot;c&quot;,&quot;0808&quot;],[&quot;c&quot;,&quot;0829&quot;],[&quot;e&quot;,&quot;0215&quot;],[&quot;d&quot;,&quot;1508&quot;],[&quot;d&quot;,&quot;1444&quot;],[&quot;d&quot;,&quot;1410&quot;],[&quot;c&quot;,&quot;0809&quot;]]
<strong>Output:</strong> [&quot;c&quot;,&quot;d&quot;]
<strong>Explanation:</strong> &quot;c&quot; has three access times in the one-hour period of [08:08, 09:07] which are 08:08, 08:09, and 08:29.
&quot;d&quot; has also three access times in the one-hour period of [14:10, 15:09] which are 14:10, 14:44, and 15:08.
However, &quot;e&quot; has just one access time, so it can not be in the answer and the final answer is [&quot;c&quot;,&quot;d&quot;].</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> access_times = [[&quot;cd&quot;,&quot;1025&quot;],[&quot;ab&quot;,&quot;1025&quot;],[&quot;cd&quot;,&quot;1046&quot;],[&quot;cd&quot;,&quot;1055&quot;],[&quot;ab&quot;,&quot;1124&quot;],[&quot;ab&quot;,&quot;1120&quot;]]
<strong>Output:</strong> [&quot;ab&quot;,&quot;cd&quot;]
<strong>Explanation:</strong> &quot;ab&quot; has three access times in the one-hour period of [10:25, 11:24] which are 10:25, 11:20, and 11:24.
&quot;cd&quot; has also three access times in the one-hour period of [10:25, 11:24] which are 10:25, 10:46, and 10:55.
So the answer is [&quot;ab&quot;,&quot;cd&quot;].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= access_times.length &lt;= 100</code></li>
	<li><code>access_times[i].length == 2</code></li>
	<li><code>1 &lt;= access_times[i][0].length &lt;= 10</code></li>
	<li><code>access_times[i][0]</code> consists only of English small letters.</li>
	<li><code>access_times[i][1].length == 4</code></li>
	<li><code>access_times[i][1]</code> is in 24-hour time format.</li>
	<li><code>access_times[i][1]</code> consists only of <code>&#39;0&#39;</code> to <code>&#39;9&#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sorting

We use a hash table $d$ to store all access times of each employee, where the key is the employee's name, and the value is an integer array, representing all access times of the employee, which are the number of minutes from the start of the day at 00:00.

For each employee, we sort all their access times in ascending order. Then we traverse all access times of the employee. If there are three consecutive access times $t_1, t_2, t_3$ that satisfy $t_3 - t_1 < 60$, then the employee is a high-frequency visitor, and we add their name to the answer array.

Finally, we return the answer array.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the number of access records.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for name, t in access_times:
            d[name].append(int(t[:2]) * 60 + int(t[2:]))
        ans = []
        for name, ts in d.items():
            ts.sort()
            if any(ts[i] - ts[i - 2] < 60 for i in range(2, len(ts))):
                ans.append(name)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
