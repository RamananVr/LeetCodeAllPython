---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2857.Count%20Pairs%20of%20Points%20With%20Distance%20k/README_EN.md
rating: 2081
source: Biweekly Contest 113 Q3
tags:
    - Bit Manipulation
    - Array
    - Hash Table
---

<!-- problem:start -->

# [2857. Count Pairs of Points With Distance k](https://leetcode.com/problems/count-pairs-of-points-with-distance-k)

## Description

<!-- description:start -->

<p>You are given a <strong>2D</strong> integer array <code>coordinates</code> and an integer <code>k</code>, where <code>coordinates[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> are the coordinates of the <code>i<sup>th</sup></code> point in a 2D plane.</p>

<p>We define the <strong>distance</strong> between two points <code>(x<sub>1</sub>, y<sub>1</sub>)</code> and <code>(x<sub>2</sub>, y<sub>2</sub>)</code> as <code>(x1 XOR x2) + (y1 XOR y2)</code> where <code>XOR</code> is the bitwise <code>XOR</code> operation.</p>

<p>Return <em>the number of pairs </em><code>(i, j)</code><em> such that </em><code>i &lt; j</code><em> and the distance between points </em><code>i</code><em> and </em><code>j</code><em> is equal to </em><code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can choose the following pairs:
- (0,1): Because we have (1 XOR 4) + (2 XOR 2) = 5.
- (2,3): Because we have (1 XOR 5) + (3 XOR 2) = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0
<strong>Output:</strong> 10
<strong>Explanation:</strong> Any two chosen pairs will have a distance of 0. There are 10 ways to choose two pairs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= coordinates.length &lt;= 50000</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumeration

We can use a hash table $cnt$ to count the occurrence of each point in the array $coordinates$.

Next, we enumerate each point $(x_2, y_2)$ in the array $coordinates$. Since the range of $k$ is $[0, 100]$, and the result of $x_1 \oplus x_2$ or $y_1 \oplus y_2$ is always greater than or equal to $0$, we can enumerate the result $a$ of $x_1 \oplus x_2$ in the range $[0,..k]$. Then, the result of $y_1 \oplus y_2$ is $b = k - a$. In this way, we can calculate the values of $x_1$ and $y_1$, and add the occurrence of $(x_1, y_1)$ to the answer.

The time complexity is $O(n \times k)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $coordinates$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        cnt = Counter()
        ans = 0
        for x2, y2 in coordinates:
            for a in range(k + 1):
                b = k - a
                x1, y1 = a ^ x2, b ^ y2
                ans += cnt[(x1, y1)]
            cnt[(x2, y2)] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
