---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1470.Shuffle%20the%20Array/README_EN.md
rating: 1120
source: Weekly Contest 192 Q1
tags:
    - Array
---

<!-- problem:start -->

# [1470. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array)

## Description

<!-- description:start -->

<p>Given the array <code>nums</code> consisting of <code>2n</code> elements in the form <code>[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]</code>.</p>

<p><em>Return the array in the form</em> <code>[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>

<strong>Input:</strong> nums = [2,5,1,3,4,7], n = 3

<strong>Output:</strong> [2,3,5,4,1,7] 

<strong>Explanation:</strong> Since x<sub>1</sub>=2, x<sub>2</sub>=5, x<sub>3</sub>=1, y<sub>1</sub>=3, y<sub>2</sub>=4, y<sub>3</sub>=7 then the answer is [2,3,5,4,1,7].

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>

<strong>Input:</strong> nums = [1,2,3,4,4,3,2,1], n = 4

<strong>Output:</strong> [1,4,2,3,3,2,4,1]

</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>

<strong>Input:</strong> nums = [1,1,2,2], n = 2

<strong>Output:</strong> [1,2,1,2]

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>1 &lt;= n &lt;= 500</code></li>

    <li><code>nums.length == 2n</code></li>

    <li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We traverse the indices $i$ in the range $[0, n)$. Each time, we take $\textit{nums}[i]$ and $\textit{nums}[i+n]$ and place them sequentially into the answer array.

After the traversal is complete, we return the answer array.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for pair in zip(nums[:n], nums[n:]) for x in pair]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
