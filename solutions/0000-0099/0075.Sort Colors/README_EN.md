---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0000-0099/0075.Sort%20Colors/README_EN.md
tags:
    - Array
    - Two Pointers
    - Bubble Sort
    - Sorting
    - Quick Sort
---

<!-- problem:start -->

# [75. Sort Colors](https://leetcode.com/problems/sort-colors)

## Description

<!-- description:start -->

<p>You are given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.</p>

<p>You must solve this problem without using the library&#39;s sort function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,2,1,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,1,1,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is either 0, 1, or 2.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Could you come up with a one-pass algorithm using only&nbsp;constant extra space?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Three Pointers

We define three pointers $i$, $j$, and $k$. Pointer $i$ is used to point to the rightmost boundary of the elements with a value of $0$ in the array, and pointer $j$ is used to point to the leftmost boundary of the elements with a value of $2$ in the array. Initially, $i=-1$, $j=n$. Pointer $k$ is used to point to the current element being traversed, initially $k=0$.

When $k < j$, we perform the following operations:

- If $nums[k] = 0$, then swap it with $nums[i+1]$, then increment both $i$ and $k$ by $1$;
- If $nums[k] = 2$, then swap it with $nums[j-1]$, then decrement $j$ by $1$;
- If $nums[k] = 1$, then increment $k$ by $1$.

After the traversal, the elements in the array are divided into three parts: $[0,i]$, $[i+1,j-1]$ and $[j,n-1]$.

The time complexity is $O(n)$, where $n$ is the length of the array. Only one traversal of the array is needed. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = -1, len(nums), 0
        while k < j:
            if nums[k] == 0:
                i += 1
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            elif nums[k] == 2:
                j -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                k += 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
