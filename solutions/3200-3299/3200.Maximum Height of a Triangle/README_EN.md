---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3200.Maximum%20Height%20of%20a%20Triangle/README_EN.md
rating: 1451
source: Weekly Contest 404 Q1
tags:
    - Array
    - Enumeration
---

<!-- problem:start -->

# [3200. Maximum Height of a Triangle](https://leetcode.com/problems/maximum-height-of-a-triangle)

## Description

<!-- description:start -->

<p>You are given two integers <code>red</code> and <code>blue</code> representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1<sup>st</sup> row will have 1 ball, the 2<sup>nd</sup> row will have 2 balls, the 3<sup>rd</sup> row will have 3 balls, and so on.</p>

<p>All the balls in a particular row should be the <strong>same</strong> color, and adjacent rows should have <strong>different</strong> colors.</p>

<p>Return the <strong>maximum</strong><em> height of the triangle</em> that can be achieved.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">red = 2, blue = 4</span></p>

<p><strong>Output:</strong> 3</p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3200.Maximum%20Height%20of%20a%20Triangle/images/brb.png" style="width: 300px; height: 240px; padding: 10px;" /></p>

<p>The only possible arrangement is shown above.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">red = 2, blue = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3200.Maximum%20Height%20of%20a%20Triangle/images/br.png" style="width: 150px; height: 135px; padding: 10px;" /><br />
The only possible arrangement is shown above.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">red = 1, blue = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">red = 10, blue = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3200-3299/3200.Maximum%20Height%20of%20a%20Triangle/images/br.png" style="width: 150px; height: 135px; padding: 10px;" /><br />
The only possible arrangement is shown above.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= red, blue &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We can enumerate the color of the first row, then simulate the construction of the triangle, calculating the maximum height.

The time complexity is $O(\sqrt{n})$, where $n$ is the number of red and blue balls. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        ans = 0
        for k in range(2):
            c = [red, blue]
            i, j = 1, k
            while i <= c[j]:
                c[j] -= i
                j ^= 1
                ans = max(ans, i)
                i += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
