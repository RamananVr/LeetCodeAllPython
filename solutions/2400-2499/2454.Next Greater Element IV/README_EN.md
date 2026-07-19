---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2454.Next%20Greater%20Element%20IV/README_EN.md
rating: 2175
source: Biweekly Contest 90 Q4
tags:
    - Stack
    - Array
    - Binary Search
    - Sorting
    - Monotonic Stack
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2454. Next Greater Element IV](https://leetcode.com/problems/next-greater-element-iv)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array of non-negative integers <code>nums</code>. For each integer in <code>nums</code>, you must find its respective <strong>second greater</strong> integer.</p>

<p>The <strong>second greater</strong> integer of <code>nums[i]</code> is <code>nums[j]</code> such that:</p>

<ul>
	<li><code>j &gt; i</code></li>
	<li><code>nums[j] &gt; nums[i]</code></li>
	<li>There exists <strong>exactly one</strong> index <code>k</code> such that <code>nums[k] &gt; nums[i]</code> and <code>i &lt; k &lt; j</code>.</li>
</ul>

<p>If there is no such <code>nums[j]</code>, the second greater integer is considered to be <code>-1</code>.</p>

<ul>
	<li>For example, in the array <code>[1, 2, 4, 3]</code>, the second greater integer of <code>1</code> is <code>4</code>, <code>2</code> is <code>3</code>,&nbsp;and that of <code>3</code> and <code>4</code> is <code>-1</code>.</li>
</ul>

<p>Return<em> an integer array </em><code>answer</code><em>, where </em><code>answer[i]</code><em> is the second greater integer of </em><code>nums[i]</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,4,0,9,6]
<strong>Output:</strong> [9,6,6,-1,-1]
<strong>Explanation:</strong>
0th index: 4 is the first integer greater than 2, and 9 is the second integer greater than 2, to the right of 2.
1st index: 9 is the first, and 6 is the second integer greater than 4, to the right of 4.
2nd index: 9 is the first, and 6 is the second integer greater than 0, to the right of 0.
3rd index: There is no integer greater than 9 to its right, so the second greater integer is considered to be -1.
4th index: There is no integer greater than 6 to its right, so the second greater integer is considered to be -1.
Thus, we return [9,6,6,-1,-1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3]
<strong>Output:</strong> [-1,-1]
<strong>Explanation:</strong>
We return [-1,-1] since neither integer has any integer greater than it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Ordered Set

We can convert the elements in the array into pairs $(x, i)$, where $x$ is the value of the element and $i$ is the index of the element. Then sort by the value of the elements in descending order.

Next, we traverse the sorted array, maintaining an ordered set that stores the indices of the elements. When we traverse to the element $(x, i)$, the indices of all elements greater than $x$ are already in the ordered set. We only need to find the index $j$ of the next element after $i$ in the ordered set, then the element corresponding to $j$ is the second largest element of $x$. Then, we add $i$ to the ordered set. Continue to traverse the next element.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        arr = [(x, i) for i, x in enumerate(nums)]
        arr.sort(key=lambda x: -x[0])
        sl = SortedList()
        n = len(nums)
        ans = [-1] * n
        for _, i in arr:
            j = sl.bisect_right(i)
            if j + 1 < len(sl):
                ans[i] = nums[sl[j + 1]]
            sl.add(i)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

### Solution 2: Double Stacks

We maintain two decreasing monotonic stacks:

`stackOne`: stores elements that have not yet encountered any greater element to their right.

`stackTwo`: stores elements that have encountered exactly one greater element to their right.

Algorithm:

As we iterate through the array `nums`, for current element $nums[k]$, have these steps:

1. While `stackTwo` is not empty and its top element is less than $nums[k]$,
   these top elements have found their second next greater element.
   Pop them and record $nums[k]$ as the answer for their respective indices.

2. While `stackOne` is not empty and its top element is less than $nums[k]$,
   these top elements have found their first next greater element.
   Pop them to move them to a temporary list/vector called `transporter`.

3. Pop all elements from the back of `transporter` and push them onto `stackTwo`.
   These elements will naturally maintain the decreasing order in `stackTwo`.

4. Push current element $nums[k]$ into `stackOne` for future comparisons.

Our time complexity is $O(n)$, where $n$ is the length of the array nums.

This is because each element is pushed and popped across two stacks for at most 4 times in total.

Space complexity is $O(n)$, as all elements must be stored across two stacks.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        second_next_greater = [-1] * len(nums)

        stack_1: list[tuple[int, int]] = []  # Decreasing monotonic stacks: (num, idx).
        stack_2: list[tuple[int, int]] = []

        # Transport tuples from stack 1 to stack 2.
        transporter: list[tuple[int, int]] = []

        for idx, num in enumerate(nums):
            while stack_2 and stack_2[-1][0] < num:
                _, past_idx = stack_2.pop(-1)
                second_next_greater[past_idx] = num

            while stack_1 and stack_1[-1][0] < num:
                transporter.append(stack_1.pop(-1))

            while transporter:
                stack_2.append(transporter.pop(-1))  # Ensure decreasing monotonicity.
            stack_1.append((num, idx))

        return second_next_greater
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
