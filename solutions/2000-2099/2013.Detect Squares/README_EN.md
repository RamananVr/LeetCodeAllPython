---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2013.Detect%20Squares/README_EN.md
rating: 1841
source: Weekly Contest 259 Q3
tags:
    - Design
    - Array
    - Hash Table
    - Counting
    - Data Stream
---

<!-- problem:start -->

# [2013. Detect Squares](https://leetcode.com/problems/detect-squares)

## Description

<!-- description:start -->

<p>You are given a stream of points on the X-Y plane. Design an algorithm that:</p>

<ul>
	<li><strong>Adds</strong> new points from the stream into a data structure. <strong>Duplicate</strong> points are allowed and should be treated as different points.</li>
	<li>Given a query point, <strong>counts</strong> the number of ways to choose three points from the data structure such that the three points and the query point form an <strong>axis-aligned square</strong> with <strong>positive area</strong>.</li>
</ul>

<p>An <strong>axis-aligned square</strong> is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.</p>

<p>Implement the <code>DetectSquares</code> class:</p>

<ul>
	<li><code>DetectSquares()</code> Initializes the object with an empty data structure.</li>
	<li><code>void add(int[] point)</code> Adds a new point <code>point = [x, y]</code> to the data structure.</li>
	<li><code>int count(int[] point)</code> Counts the number of ways to form <strong>axis-aligned squares</strong> with point <code>point = [x, y]</code> as described above.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2013.Detect%20Squares/images/image.png" style="width: 869px; height: 504px;" />
<pre>
<strong>Input</strong>
[&quot;DetectSquares&quot;, &quot;add&quot;, &quot;add&quot;, &quot;add&quot;, &quot;count&quot;, &quot;count&quot;, &quot;add&quot;, &quot;count&quot;]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
<strong>Output</strong>
[null, null, null, null, 1, 0, null, 2]

<strong>Explanation</strong>
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
// - The first, second, and third points
detectSquares.count([14, 8]); // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]); // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
// - The first, second, and third points
// - The first, third, and fourth points

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>point.length == 2</code></li>
	<li><code>0 &lt;= x, y &lt;= 1000</code></li>
	<li>At most <code>3000</code> calls <strong>in total</strong> will be made to <code>add</code> and <code>count</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We can use a hash table $cnt$ to maintain all the information of the points, where $cnt[x][y]$ represents the count of point $(x, y)$.

When calling the $add(x, y)$ method, we increase the value of $cnt[x][y]$ by $1$.

When calling the $count(x_1, y_1)$ method, we need to get three other points to form an axis-aligned square. We can enumerate the point $(x_2, y_1)$ that is parallel to the $x$-axis and at a distance $d$ from $(x_1, y_1)$. If such a point exists, based on these two points, we can determine the other two points as $(x_1, y_1 + d)$ and $(x_2, y_1 + d)$, or $(x_1, y_1 - d)$ and $(x_2, y_1 - d)$. We can add up the number of schemes for these two situations.

In terms of time complexity, the time complexity of calling the $add(x, y)$ method is $O(1)$, and the time complexity of calling the $count(x_1, y_1)$ method is $O(n)$; the space complexity is $O(n)$. Here, $n$ is the number of points in the data stream.

<!-- tabs:start -->

#### Python3

```python
class DetectSquares:
    def __init__(self):
        self.cnt = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.cnt[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        if x1 not in self.cnt:
            return 0
        ans = 0
        for x2 in self.cnt.keys():
            if x2 != x1:
                d = x2 - x1
                ans += self.cnt[x2][y1] * self.cnt[x1][y1 + d] * self.cnt[x2][y1 + d]
                ans += self.cnt[x2][y1] * self.cnt[x1][y1 - d] * self.cnt[x2][y1 - d]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
