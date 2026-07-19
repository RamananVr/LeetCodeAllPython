---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1090.Largest%20Values%20From%20Labels/README_EN.md
rating: 1501
source: Weekly Contest 141 Q2
tags:
    - Greedy
    - Array
    - Hash Table
    - Counting
    - Sorting
---

<!-- problem:start -->

# [1090. Largest Values From Labels](https://leetcode.com/problems/largest-values-from-labels)

## Description

<!-- description:start -->

<p>You are given <code>n</code> item&#39;s value and label as two integer arrays <code>values</code> and <code>labels</code>. You are also given two integers <code>numWanted</code> and <code>useLimit</code>.</p>

<p>Your task is to find a subset of items with the <strong>maximum sum</strong> of their values such that:</p>

<ul>
	<li>The number of items is <strong>at most</strong> <code>numWanted</code>.</li>
	<li>The number of items with the same label is <strong>at most</strong> <code>useLimit</code>.</li>
</ul>

<p>Return the maximum sum.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>The subset chosen is the first, third, and fifth items with the sum of values 5 + 3 + 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The subset chosen is the first, second, and third items with the sum of values 5 + 4 + 3.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>The subset chosen is the first and fourth items with the sum of values 9 + 7.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == values.length == labels.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= values[i], labels[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= numWanted, useLimit &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        ans = num = 0
        cnt = Counter()
        for v, l in sorted(zip(values, labels), reverse=True):
            if cnt[l] < useLimit:
                cnt[l] += 1
                num += 1
                ans += v
                if num == numWanted:
                    break
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
