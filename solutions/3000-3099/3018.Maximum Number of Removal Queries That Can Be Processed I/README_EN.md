---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3000-3099/3018.Maximum%20Number%20of%20Removal%20Queries%20That%20Can%20Be%20Processed%20I/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3018. Maximum Number of Removal Queries That Can Be Processed I 🔒](https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array <code>nums</code> and a <strong>0-indexed</strong> array <code>queries</code>.</p>

<p>You can do the following operation at the beginning <strong>at most once</strong>:</p>

<ul>
	<li>Replace <code>nums</code> with a <span data-keyword="subsequence-array">subsequence</span> of <code>nums</code>.</li>
</ul>

<p>We start processing queries in the given order; for each query, we do the following:</p>

<ul>
	<li>If the first <strong>and</strong> the last element of <code>nums</code> is <strong>less than</strong> <code>queries[i]</code>, the processing of queries <strong>ends</strong>.</li>
	<li>Otherwise, we choose either the first <strong>or</strong> the last element of <code>nums</code> if it is <strong>greater than or equal to</strong> <code>queries[i]</code>, and we <strong>remove</strong> the chosen element from <code>nums</code>.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of queries that can be processed by doing the operation optimally.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], queries = [1,2,3,4,6]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We don&#39;t do any operation and process the queries as follows:
1- We choose and remove nums[0] since 1 &lt;= 1, then nums becomes [2,3,4,5].
2- We choose and remove nums[0] since 2 &lt;= 2, then nums becomes [3,4,5].
3- We choose and remove nums[0] since 3 &lt;= 3, then nums becomes [4,5].
4- We choose and remove nums[0] since 4 &lt;= 4, then nums becomes [5].
5- We can not choose any elements from nums since they are not greater than or equal to 5.
Hence, the answer is 4.
It can be shown that we can&#39;t process more than 4 queries.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,2], queries = [2,2,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We don&#39;t do any operation and process the queries as follows:
1- We choose and remove nums[0] since 2 &lt;= 2, then nums becomes [3,2].
2- We choose and remove nums[1] since 2 &lt;= 2, then nums becomes [3].
3- We choose and remove nums[0] since 3 &lt;= 3, then nums becomes [].
Hence, the answer is 3.
It can be shown that we can&#39;t process more than 3 queries.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,3], queries = [4,3,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> First we replace nums with the subsequence of nums [4,3].
Then we can process the queries as follows:
1- We choose and remove nums[0] since 4 &lt;= 4, then nums becomes [3].
2- We choose and remove nums[0] since 3 &lt;= 3, then nums becomes [].
3- We can not process any more queries since nums is empty.
Hence, the answer is 2.
It can be shown that we can&#39;t process more than 2 queries.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= queries.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], queries[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the maximum number of queries we can handle when the numbers in the interval $[i, j]$ have not been deleted yet.

Consider $f[i][j]$:

- If $i > 0$, the value of $f[i][j]$ can be transferred from $f[i - 1][j]$. If $nums[i - 1] \ge queries[f[i - 1][j]]$, we can choose to delete $nums[i - 1]$. Therefore, we have $f[i][j] = f[i - 1][j] + (nums[i - 1] \ge queries[f[i - 1][j]])$.
- If $j + 1 < n$, the value of $f[i][j]$ can be transferred from $f[i][j + 1]$. If $nums[j + 1] \ge queries[f[i][j + 1]]$, we can choose to delete $nums[j + 1]$. Therefore, we have $f[i][j] = f[i][j + 1] + (nums[j + 1] \ge queries[f[i][j + 1]])$.
- If $f[i][j] = m$, we can directly return $m$.

The final answer is $\max\limits_{0 \le i < n} f[i][i] + (nums[i] \ge queries[f[i][i]])$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        m = len(queries)
        for i in range(n):
            for j in range(n - 1, i - 1, -1):
                if i:
                    f[i][j] = max(
                        f[i][j], f[i - 1][j] + (nums[i - 1] >= queries[f[i - 1][j]])
                    )
                if j + 1 < n:
                    f[i][j] = max(
                        f[i][j], f[i][j + 1] + (nums[j + 1] >= queries[f[i][j + 1]])
                    )
                if f[i][j] == m:
                    return m
        return max(f[i][i] + (nums[i] >= queries[f[i][i]]) for i in range(n))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
