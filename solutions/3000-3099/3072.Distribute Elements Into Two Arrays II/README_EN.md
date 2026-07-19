---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3000-3099/3072.Distribute%20Elements%20Into%20Two%20Arrays%20II/README_EN.md
rating: 2052
source: Weekly Contest 387 Q4
tags:
    - Binary Indexed Tree
    - Segment Tree
    - Array
    - Simulation
---

<!-- problem:start -->

# [3072. Distribute Elements Into Two Arrays II](https://leetcode.com/problems/distribute-elements-into-two-arrays-ii)

## Description

<!-- description:start -->

<p>You are given a <strong>1-indexed</strong> array of integers <code>nums</code> of length <code>n</code>.</p>

<p>We define a function <code>greaterCount</code> such that <code>greaterCount(arr, val)</code> returns the number of elements in <code>arr</code> that are <strong>strictly greater</strong> than <code>val</code>.</p>

<p>You need to distribute all the elements of <code>nums</code> between two arrays <code>arr1</code> and <code>arr2</code> using <code>n</code> operations. In the first operation, append <code>nums[1]</code> to <code>arr1</code>. In the second operation, append <code>nums[2]</code> to <code>arr2</code>. Afterwards, in the <code>i<sup>th</sup></code> operation:</p>

<ul>
	<li>If <code>greaterCount(arr1, nums[i]) &gt; greaterCount(arr2, nums[i])</code>, append <code>nums[i]</code> to <code>arr1</code>.</li>
	<li>If <code>greaterCount(arr1, nums[i]) &lt; greaterCount(arr2, nums[i])</code>, append <code>nums[i]</code> to <code>arr2</code>.</li>
	<li>If <code>greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i])</code>, append <code>nums[i]</code> to the array with a <strong>lesser</strong> number of elements.</li>
	<li>If there is still a tie, append <code>nums[i]</code> to <code>arr1</code>.</li>
</ul>

<p>The array <code>result</code> is formed by concatenating the arrays <code>arr1</code> and <code>arr2</code>. For example, if <code>arr1 == [1,2,3]</code> and <code>arr2 == [4,5,6]</code>, then <code>result = [1,2,3,4,5,6]</code>.</p>

<p>Return <em>the integer array</em> <code>result</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3,3]
<strong>Output:</strong> [2,3,1,3]
<strong>Explanation:</strong> After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3<sup>rd</sup> operation, the number of elements greater than 3 is zero in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4<sup>th</sup> operation, the number of elements greater than 3 is zero in both arrays. As the length of arr2 is lesser, hence, append nums[4] to arr2.
After 4 operations, arr1 = [2,3] and arr2 = [1,3].
Hence, the array result formed by concatenation is [2,3,1,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,14,3,1,2]
<strong>Output:</strong> [5,3,1,2,14]
<strong>Explanation:</strong> After the first 2 operations, arr1 = [5] and arr2 = [14].
In the 3<sup>rd</sup> operation, the number of elements greater than 3 is one in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4<sup>th</sup> operation, the number of elements greater than 1 is greater in arr1 than arr2 (2 &gt; 1). Hence, append nums[4] to arr1.
In the 5<sup>th</sup> operation, the number of elements greater than 2 is greater in arr1 than arr2 (2 &gt; 1). Hence, append nums[5] to arr1.
After 5 operations, arr1 = [5,3,1,2] and arr2 = [14].
Hence, the array result formed by concatenation is [5,3,1,2,14].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3,3]
<strong>Output:</strong> [3,3,3,3]
<strong>Explanation:</strong> At the end of 4 operations, arr1 = [3,3] and arr2 = [3,3].
Hence, the array result formed by concatenation is [3,3,3,3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Discretization + Binary Indexed Tree

We can use two binary indexed trees `tree1` and `tree2` to maintain the number of elements in `arr1` and `arr2` that are less than or equal to a certain number. Each time, we query the number of elements that are less than or equal to the current number in the binary indexed tree, then the number of elements that are greater than the current number is the length of the current array minus the query result. Then we can decide which array to add the current number to based on this difference.

Since the range of numbers given in the problem is very large, we need to discretize these numbers. We can sort these numbers and remove duplicates, then use binary search to find the position of each number in the sorted array.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array `nums`.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    __slots__ = "n", "c"

    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        st = sorted(set(nums))
        m = len(st)
        tree1 = BinaryIndexedTree(m + 1)
        tree2 = BinaryIndexedTree(m + 1)
        tree1.update(bisect_left(st, nums[0]) + 1, 1)
        tree2.update(bisect_left(st, nums[1]) + 1, 1)
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for x in nums[2:]:
            i = bisect_left(st, x) + 1
            a = len(arr1) - tree1.query(i)
            b = len(arr2) - tree2.query(i)
            if a > b:
                arr1.append(x)
                tree1.update(i, 1)
            elif a < b:
                arr2.append(x)
                tree2.update(i, 1)
            elif len(arr1) <= len(arr2):
                arr1.append(x)
                tree1.update(i, 1)
            else:
                arr2.append(x)
                tree2.update(i, 1)
        return arr1 + arr2
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
