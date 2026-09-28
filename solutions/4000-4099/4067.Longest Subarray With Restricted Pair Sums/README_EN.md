---
comments: true
difficulty: Medium
---

<!-- problem:start -->

# [4067. Longest Subarray With Restricted Pair Sums](https://leetcode.com/problems/longest-subarray-with-restricted-pair-sums)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>A <strong>subarray</strong> <code>nums[l..r]</code> is valid if there are no three <strong>distinct</strong> indices <code>i</code>, <code>j</code>, and <code>k</code> such that <code>l &lt;= i, j, k &lt;= r</code> and:</p>

<ul>
	<li><code>nums[i] + nums[j] == nums[k]</code></li>
</ul>

<p>Return the <strong>maximum</strong> length of a valid subarray of <code>nums</code>.</p>

<p>A <strong>subarray</strong> is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5,3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Consider the subarray <code>[3, 5, 3]</code>. The pairs of elements at distinct indices have the following sums:</p>

<ul>
	<li><code>3 + 5 = 8</code></li>
	<li><code>3 + 3 = 6</code>, using the two different occurrences of 3</li>
	<li><code>5 + 3 = 8</code></li>
</ul>

<p>None of these sums is an element at the remaining index, so the subarray is valid.</p>

<p>Every subarray of length 4 contains 2, 3, and 5 at distinct indices, where <code>2 + 3 = 5</code>. Therefore, no longer valid subarray exists, and the answer is 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,4,5,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The sums obtained from every pair of elements at distinct indices are 7, 8, 9, 9, 10, and 11. None of these values appears at the remaining index, so the entire array is valid.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 500</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

<!-- thinking:start -->

> **Thinking**
>
> $n\le 1000$. Checking three indices inside every subarray adds another quadratic factor on top of the two endpoints and does not finish in time.
>
> Once $a+b=c$ occurs, every longer interval that contains it is also invalid, so the left end only moves right as the right end moves right. A newly added $x$ breaks the window only when it equals the sum of two values already inside, or the difference of two such values.
>
> Keep the number of pair sums and absolute differences in the window. If $x$ hits either count, delete elements from the left and remove the pairs they belong to. Each pair is inserted once and deleted once.

<!-- thinking:end -->

The window $\textit{nums}[l..r]$ is valid exactly when no three distinct indices have two elements summing to the third. An invalid segment stays invalid in every longer interval that contains it, so the left end only increases as the right end grows.

Let $m=\max(\textit{nums})$. $\textit{cntS}[s]$ is the number of pairs in the current window whose values sum to $s$, and $\textit{cntD}[d]$ is the number of pairs whose absolute difference is $d$. Sums are at most $2m$ and differences are at most $m$.

The value at the right end is $x$, and the window before it is added is $[l,r)$. Adding $x$ makes the window invalid exactly when some pair already sums to $x$, or some pair already differs by $x$. The first case means $x$ is the sum. The second means $x$ is an addend and the other two elements are still in the window. Every value is positive, so the absolute difference is enough.

While that happens, remove the left element $y$ and subtract the sums and differences of $y$ with each element that remains in $[l,r)$. After the window is valid again, add the sums and differences of $x$ with each element of $[l,r)$, and update the answer with $r-l+1$.

Each pair is inserted when the later end enters and deleted when the earlier end leaves. The time complexity is $O(n^2)$ and the space complexity is $O(m)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt_s = [0] * (mx << 1 | 1)
        cnt_d = [0] * (mx + 1)
        ans = l = 0

        for r, x in enumerate(nums):
            while cnt_s[x] > 0 or cnt_d[x] > 0:
                y = nums[l]
                l += 1
                for z in nums[l:r]:
                    cnt_s[y + z] -= 1
                    cnt_d[abs(y - z)] -= 1

            for y in nums[l:r]:
                cnt_s[x + y] += 1
                cnt_d[abs(x - y)] += 1

            ans = max(ans, r - l + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
