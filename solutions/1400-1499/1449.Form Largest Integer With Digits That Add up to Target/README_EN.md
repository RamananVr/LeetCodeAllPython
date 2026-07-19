---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1449.Form%20Largest%20Integer%20With%20Digits%20That%20Add%20up%20to%20Target/README_EN.md
rating: 1927
source: Biweekly Contest 26 Q4
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [1449. Form Largest Integer With Digits That Add up to Target](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target)

## Description

<!-- description:start -->

<p>Given an array of integers <code>cost</code> and an integer <code>target</code>, return <em>the <strong>maximum</strong> integer you can paint under the following rules</em>:</p>

<ul>
	<li>The cost of painting a digit <code>(i + 1)</code> is given by <code>cost[i]</code> (<strong>0-indexed</strong>).</li>
	<li>The total cost used must be equal to <code>target</code>.</li>
	<li>The integer does not have <code>0</code> digits.</li>
</ul>

<p>Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return <code>&quot;0&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> cost = [4,3,2,5,6,7,2,5,5], target = 9
<strong>Output:</strong> &quot;7772&quot;
<strong>Explanation:</strong> The cost to paint the digit &#39;7&#39; is 2, and the digit &#39;2&#39; is 3. Then cost(&quot;7772&quot;) = 2*3+ 3*1 = 9. You could also paint &quot;977&quot;, but &quot;7772&quot; is the largest number.
<strong>Digit    cost</strong>
  1  -&gt;   4
  2  -&gt;   3
  3  -&gt;   2
  4  -&gt;   5
  5  -&gt;   6
  6  -&gt;   7
  7  -&gt;   2
  8  -&gt;   5
  9  -&gt;   5
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> cost = [7,6,5,5,5,6,8,7,8], target = 12
<strong>Output:</strong> &quot;85&quot;
<strong>Explanation:</strong> The cost to paint the digit &#39;8&#39; is 7, and the digit &#39;5&#39; is 5. Then cost(&quot;85&quot;) = 7 + 5 = 12.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> cost = [2,4,6,2,4,6,4,4,4], target = 5
<strong>Output:</strong> &quot;0&quot;
<strong>Explanation:</strong> It is impossible to paint any integer with total cost equal to target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>cost.length == 9</code></li>
	<li><code>1 &lt;= cost[i], target &lt;= 5000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        f = [[-inf] * (target + 1) for _ in range(10)]
        f[0][0] = 0
        g = [[0] * (target + 1) for _ in range(10)]
        for i, c in enumerate(cost, 1):
            for j in range(target + 1):
                if j < c or f[i][j - c] + 1 < f[i - 1][j]:
                    f[i][j] = f[i - 1][j]
                    g[i][j] = j
                else:
                    f[i][j] = f[i][j - c] + 1
                    g[i][j] = j - c
        if f[9][target] < 0:
            return "0"
        ans = []
        i, j = 9, target
        while i:
            if j == g[i][j]:
                i -= 1
            else:
                ans.append(str(i))
                j = g[i][j]
        return "".join(ans)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
