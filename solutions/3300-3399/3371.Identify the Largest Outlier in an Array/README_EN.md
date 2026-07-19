---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3300-3399/3371.Identify%20the%20Largest%20Outlier%20in%20an%20Array/README_EN.md
rating: 1643
source: Weekly Contest 426 Q2
tags:
    - Array
    - Hash Table
    - Counting
    - Enumeration
---

<!-- problem:start -->

# [3371. Identify the Largest Outlier in an Array](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>. This array contains <code>n</code> elements, where <strong>exactly</strong> <code>n - 2</code> elements are <strong>special</strong><strong> numbers</strong>. One of the remaining <strong>two</strong> elements is the <em>sum</em> of these <strong>special numbers</strong>, and the other is an <strong>outlier</strong>.</p>

<p>An <strong>outlier</strong> is defined as a number that is <em>neither</em> one of the original special numbers <em>nor</em> the element representing the sum of those numbers.</p>

<p><strong>Note</strong> that special numbers, the sum element, and the outlier must have <strong>distinct</strong> indices, but <em>may </em>share the <strong>same</strong> value.</p>

<p>Return the <strong>largest</strong><strong> </strong>potential<strong> outlier</strong> in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-2,-1,-3,-6,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1,1,5,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li>The input is generated such that at least <strong>one</strong> potential outlier exists in <code>nums</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumeration

We use a hash table $\textit{cnt}$ to record the frequency of each element in the array $\textit{nums}$.

Next, we enumerate each element $x$ in the array $\textit{nums}$ as a possible outlier. For each $x$, we calculate the sum $t$ of all elements in the array $\textit{nums}$ except $x$. If $t$ is not even, or half of $t$ is not in $\textit{cnt}$, then $x$ does not meet the condition, and we skip this $x$. Otherwise, if $x$ is not equal to half of $t$, or $x$ appears more than once in $\textit{cnt}$, then $x$ is a possible outlier, and we update the answer.

After enumerating all elements, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = sum(nums)
        cnt = Counter(nums)
        ans = -inf
        for x, v in cnt.items():
            t = s - x
            if t % 2 or cnt[t // 2] == 0:
                continue
            if x != t // 2 or v > 1:
                ans = max(ans, x)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
