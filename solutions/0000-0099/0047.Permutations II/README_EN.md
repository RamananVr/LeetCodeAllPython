---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0047.Permutations%20II/README_EN.md
tags:
    - Array
    - Backtracking
    - Sorting
---

<!-- problem:start -->

# [47. Permutations II](https://leetcode.com/problems/permutations-ii)

## Description

<!-- description:start -->

<p>Given a collection of numbers, <code>nums</code>,&nbsp;that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Backtracking

We can first sort the array so that duplicate numbers are placed together, making it easier to remove duplicates.

Then, we design a function $\textit{dfs}(i)$, which represents the current number to be placed at the $i$-th position. The specific implementation of the function is as follows:

- If $i = n$, it means we have filled all positions, add the current permutation to the answer array, and then return.
- Otherwise, we enumerate the number $nums[j]$ for the $i$-th position, where the range of $j$ is $[0, n - 1]$. We need to ensure that $nums[j]$ has not been used and is different from the previously enumerated number to ensure that the current permutation is not duplicated. If the conditions are met, we can place $nums[j]$ and continue to recursively fill the next position by calling $\textit{dfs}(i + 1)$. After the recursive call ends, we need to mark $nums[j]$ as unused to facilitate subsequent enumeration.

In the main function, we first sort the array, then call $\textit{dfs}(0)$ to start filling from the 0th position, and finally return the answer array.

The time complexity is $O(n \times n!)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array. We need to perform $n!$ enumerations, and each enumeration requires $O(n)$ time to check for duplicates. Additionally, we need a marker array to mark whether each position has been used, so the space complexity is $O(n)$.

Similar problems:

- [46. Permutations](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0046.Permutations/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if i == n:
                ans.append(t[:])
                return
            for j in range(n):
                if vis[j] or (j and nums[j] == nums[j - 1] and not vis[j - 1]):
                    continue
                t[i] = nums[j]
                vis[j] = True
                dfs(i + 1)
                vis[j] = False

        n = len(nums)
        nums.sort()
        ans = []
        t = [0] * n
        vis = [False] * n
        dfs(0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
