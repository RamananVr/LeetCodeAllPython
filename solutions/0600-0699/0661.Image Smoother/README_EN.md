---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0661.Image%20Smoother/README_EN.md
tags:
    - Array
    - Matrix
---

<!-- problem:start -->

# [661. Image Smoother](https://leetcode.com/problems/image-smoother)

## Description

<!-- description:start -->

<p>An <strong>image smoother</strong> is a filter of the size <code>3 x 3</code> that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0661.Image%20Smoother/images/smoother-grid.jpg" style="width: 493px; height: 493px;" />
<p>Given an <code>m x n</code> integer matrix <code>img</code> representing the grayscale of an image, return <em>the image after applying the smoother on each cell of it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0661.Image%20Smoother/images/smooth-grid.jpg" style="width: 613px; height: 253px;" />
<pre>
<strong>Input:</strong> img = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[0,0,0],[0,0,0],[0,0,0]]
<strong>Explanation:</strong>
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0661.Image%20Smoother/images/smooth2-grid.jpg" style="width: 613px; height: 253px;" />
<pre>
<strong>Input:</strong> img = [[100,200,100],[200,50,200],[100,200,100]]
<strong>Output:</strong> [[137,141,137],[141,138,141],[137,141,137]]
<strong>Explanation:</strong>
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == img.length</code></li>
	<li><code>n == img[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= img[i][j] &lt;= 255</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Direct Traversal

We create a 2D array $\textit{ans}$ of size $m \times n$, where $\textit{ans}[i][j]$ represents the smoothed value of the cell in the $i$-th row and $j$-th column of the image.

For $\textit{ans}[i][j]$, we traverse the cell in the $i$-th row and $j$-th column of $\textit{img}$ and its surrounding 8 cells, calculate their sum $s$ and count $cnt$, then compute the average value $s / cnt$ and store it in $\textit{ans}[i][j]$.

After the traversal, we return $\textit{ans}$.

The time complexity is $O(m \times n)$, where $m$ and $n$ are the number of rows and columns of $\textit{img}$, respectively. Ignoring the space consumption of the answer array, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = cnt = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n:
                            cnt += 1
                            s += img[x][y]
                ans[i][j] = s // cnt
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
