---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3748.Count%20Stable%20Subarrays/README_EN.md
rating: 2209
source: Weekly Contest 476 Q4
tags:
    - Array
    - Binary Search
    - Prefix Sum
---

<!-- problem:start -->

# [3748. Count Stable Subarrays](https://leetcode.com/problems/count-stable-subarrays)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>A <strong><span data-keyword="subarray-nonempty">subarray</span></strong> of <code>nums</code> is called <strong>stable</strong> if it contains <strong>no inversions</strong>, i.e., there is no pair of indices <code>i &lt; j</code> such that <code>nums[i] &gt; nums[j]</code>.</p>

<p>You are also given a <strong>2D integer array</strong> <code>queries</code> of length <code>q</code>, where each <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> represents a query. For each query <code>[l<sub>i</sub>, r<sub>i</sub>]</code>, compute the number of <strong>stable subarrays</strong> that lie entirely within the segment <code>nums[l<sub>i</sub>..r<sub>i</sub>]</code>.</p>

<p>Return an integer array <code>ans</code> of length <code>q</code>, where <code>ans[i]</code> is the answer to the <code>i<sup>th</sup></code> query.​​​​​​​​​​​​​​</p>

<p><strong>Note</strong>:</p>

<ul>
	<li>A single element subarray is considered stable.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,3,4]</span></p>

<p><strong>Explanation:</strong>​​​​​</p>

<ul>
	<li>For <code>queries[0] = [0, 1]</code>, the subarray is <code>[nums[0], nums[1]] = [3, 1]</code>.

    <ul>
    	<li>The stable subarrays are <code>[3]</code> and <code>[1]</code>. The total number of stable subarrays is 2.</li>
    </ul>
    </li>
    <li>For <code>queries[1] = [1, 2]</code>, the subarray is <code>[nums[1], nums[2]] = [1, 2]</code>.
    <ul>
    	<li>The stable subarrays are <code>[1]</code>, <code>[2]</code>, and <code>[1, 2]</code>. The total number of stable subarrays is 3.</li>
    </ul>
    </li>
    <li>For <code>queries[2] = [0, 2]</code>, the subarray is <code>[nums[0], nums[1], nums[2]] = [3, 1, 2]</code>.
    <ul>
    	<li>The stable subarrays are <code>[3]</code>, <code>[1]</code>, <code>[2]</code>, and <code>[1, 2]</code>. The total number of stable subarrays is 4.</li>
    </ul>
    </li>

</ul>

<p>Thus, <code>ans = [2, 3, 4]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2], queries = [[0,1],[0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>queries[0] = [0, 1]</code>, the subarray is <code>[nums[0], nums[1]] = [2, 2]</code>.

    <ul>
    	<li>The stable subarrays are <code>[2]</code>, <code>[2]</code>, and <code>[2, 2]</code>. The total number of stable subarrays is 3.</li>
    </ul>
    </li>
    <li>For <code>queries[1] = [0, 0]</code>, the subarray is <code>[nums[0]] = [2]</code>.
    <ul>
    	<li>The stable subarray is <code>[2]</code>. The total number of stable subarrays is 1.</li>
    </ul>
    </li>

</ul>

<p>Thus, <code>ans = [3, 1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt;= nums.length - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segmented Counting

According to the problem description, a stable subarray is defined as a subarray without inversion pairs, meaning the elements in the subarray are arranged in non-decreasing order. Therefore, we can divide the array into several non-decreasing segments, using an array $\text{seg}$ to record the starting position of each segment. At the same time, we need a prefix sum array $\text{s}$ to record the number of stable subarrays within each segment.

Then, for each query $[l, r]$, there may be 3 cases:

1. The query interval $[l, r]$ is completely contained within a single segment. In this case, the number of stable subarrays can be directly calculated using the formula $\frac{(k + 1) \cdot k}{2}$, where $k = r - l + 1$.
2. The query interval $[l, r]$ spans multiple segments. In this case, we need to separately calculate the number of stable subarrays in the left incomplete segment, the right incomplete segment, and the complete segments in the middle, then add them together to get the final result.

The time complexity is $O((n + q) \log n)$, where $n$ is the length of the array and $q$ is the number of queries. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countStableSubarrays(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        s = [0]
        l, n = 0, len(nums)
        seg = []
        for r, x in enumerate(nums):
            if r == n - 1 or x > nums[r + 1]:
                seg.append(l)
                k = r - l + 1
                s.append(s[-1] + (1 + k) * k // 2)
                l = r + 1
        ans = []
        for l, r in queries:
            i = bisect_right(seg, l)
            j = bisect_right(seg, r) - 1
            if i > j:
                k = r - l + 1
                ans.append((1 + k) * k // 2)
            else:
                a = seg[i] - l
                b = r - seg[j] + 1
                ans.append((1 + a) * a // 2 + s[j] - s[i] + (1 + b) * b // 2)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
