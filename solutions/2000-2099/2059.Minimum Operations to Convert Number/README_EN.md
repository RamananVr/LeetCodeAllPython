---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2059.Minimum%20Operations%20to%20Convert%20Number/README_EN.md
rating: 1849
source: Weekly Contest 265 Q3
tags:
    - Breadth-First Search
    - Array
---

<!-- problem:start -->

# [2059. Minimum Operations to Convert Number](https://leetcode.com/problems/minimum-operations-to-convert-number)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> containing <strong>distinct</strong> numbers, an integer <code>start</code>, and an integer <code>goal</code>. There is an integer <code>x</code> that is initially set to <code>start</code>, and you want to perform operations on <code>x</code> such that it is converted to <code>goal</code>. You can perform the following operation repeatedly on the number <code>x</code>:</p>

<p>If <code>0 &lt;= x &lt;= 1000</code>, then for any index <code>i</code> in the array (<code>0 &lt;= i &lt; nums.length</code>), you can set <code>x</code> to any of the following:</p>

<ul>
	<li><code>x + nums[i]</code></li>
	<li><code>x - nums[i]</code></li>
	<li><code>x ^ nums[i]</code> (bitwise-XOR)</li>
</ul>

<p>Note that you can use each <code>nums[i]</code> any number of times in any order. Operations that set <code>x</code> to be out of the range <code>0 &lt;= x &lt;= 1000</code> are valid, but no more operations can be done afterward.</p>

<p>Return <em>the <strong>minimum</strong> number of operations needed to convert </em><code>x = start</code><em> into </em><code>goal</code><em>, and </em><code>-1</code><em> if it is not possible</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,4,12], start = 2, goal = 12
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can go from 2 &rarr; 14 &rarr; 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5,7], start = 0, goal = -4
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can go from 0 &rarr; 3 &rarr; -4 with the following 2 operations. 
- 0 + 3 = 3
- 3 - 7 = -4
Note that the last operation sets x out of the range 0 &lt;= x &lt;= 1000, which is valid.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,8,16], start = 0, goal = 1
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no way to convert 0 into 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i], goal &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= start &lt;= 1000</code></li>
	<li><code>start != goal</code></li>
	<li>All the integers in <code>nums</code> are distinct.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        op1 = lambda x, y: x + y
        op2 = lambda x, y: x - y
        op3 = lambda x, y: x ^ y
        ops = [op1, op2, op3]
        vis = [False] * 1001
        q = deque([(start, 0)])
        while q:
            x, step = q.popleft()
            for num in nums:
                for op in ops:
                    nx = op(x, num)
                    if nx == goal:
                        return step + 1
                    if 0 <= nx <= 1000 and not vis[nx]:
                        q.append((nx, step + 1))
                        vis[nx] = True
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        def next(x):
            res = []
            for num in nums:
                res.append(x + num)
                res.append(x - num)
                res.append(x ^ num)
            return res

        q = deque([start])
        vis = {start}
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                x = q.popleft()
                for y in next(x):
                    if y == goal:
                        return ans
                    if 0 <= y <= 1000 and y not in vis:
                        vis.add(y)
                        q.append(y)
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        def next(x):
            res = []
            for num in nums:
                res.append(x + num)
                res.append(x - num)
                res.append(x ^ num)
            return res

        def extend(m1, m2, q):
            for _ in range(len(q)):
                x = q.popleft()
                step = m1[x]
                for y in next(x):
                    if y in m1:
                        continue
                    if y in m2:
                        return step + 1 + m2[y]
                    if 0 <= y <= 1000:
                        m1[y] = step + 1
                        q.append(y)
            return -1

        m1, m2 = {start: 0}, {goal: 0}
        q1, q2 = deque([start]), deque([goal])
        while q1 and q2:
            t = extend(m1, m2, q1) if len(q1) <= len(q2) else extend(m2, m1, q2)
            if t != -1:
                return t
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
