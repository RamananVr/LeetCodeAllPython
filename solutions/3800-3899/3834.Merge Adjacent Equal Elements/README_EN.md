---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3834.Merge%20Adjacent%20Equal%20Elements/README_EN.md
rating: 1428
source: Weekly Contest 488 Q2
tags:
    - Stack
    - Array
    - Simulation
---

<!-- problem:start -->

# [3834. Merge Adjacent Equal Elements](https://leetcode.com/problems/merge-adjacent-equal-elements)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>You must <strong>repeatedly</strong> apply the following merge operation until no more changes can be made:</p>

<ul>
	<li>If any <strong>two adjacent elements are equal</strong>, choose the <strong>leftmost</strong> such adjacent pair in the current array and replace them with a single element equal to their <strong>sum</strong>.</li>
</ul>

<p>After each merge operation, the array size <strong>decreases</strong> by 1. Repeat the process on the updated array until no more changes can be made.</p>

<p>Return the final array after all possible merge operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,4]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The middle two elements are equal and merged into <code>1 + 1 = 2</code>, resulting in <code>[3, 2, 2]</code>.</li>
	<li>The last two elements are equal and merged into <code>2 + 2 = 4</code>, resulting in <code>[3, 4]</code>.</li>
	<li>No adjacent equal elements remain. Thus, the answer is <code>[3, 4]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[8]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The first two elements are equal and merged into <code>2 + 2 = 4</code>, resulting in <code>[4, 4]</code>.</li>
	<li>The first two elements are equal and merged into <code>4 + 4 = 8</code>, resulting in <code>[8]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,7,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,7,5]</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no adjacent equal elements in the array, so no operations are performed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code>​​​​​​​</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

We can use a stack to simulate the process of merging adjacent equal elements.

Define a stack $\textit{stk}$ to store the current processed array elements. Traverse each element $x$ of the input array $\textit{nums}$ and push it onto the stack. Then check if the top two elements of the stack are equal. If they are equal, pop them and push their sum back onto the stack. Repeat this process until the top two elements of the stack are no longer equal. Finally, the elements in the stack are the final merged array.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(n)$, which is used to store the elements in the stack.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stk = []
        for x in nums:
            stk.append(x)
            while len(stk) > 1 and stk[-1] == stk[-2]:
                stk.append(stk.pop() + stk.pop())
        return stk
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
