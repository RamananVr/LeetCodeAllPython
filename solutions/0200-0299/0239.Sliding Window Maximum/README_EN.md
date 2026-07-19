---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0239.Sliding%20Window%20Maximum/README_EN.md
tags:
    - Queue
    - Array
    - Sliding Window
    - Monotonic Queue
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)

## Description

<!-- description:start -->

<p>You are given an array of integers&nbsp;<code>nums</code>, there is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the max sliding window</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [3,3,5,5,6,7]
<strong>Explanation:</strong> 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Max-Heap)

We can use a priority queue (max-heap) to maintain the maximum value in the sliding window.

First, add the first $k-1$ elements to the priority queue. Then, starting from the $k$-th element, add the new element to the priority queue and check if the top element of the heap is out of the window. If it is, remove the top element. Then, add the top element of the heap to the result array.

The time complexity is $O(n \times \log k)$, and the space complexity is $O(k)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-v, i) for i, v in enumerate(nums[: k - 1])]
        heapify(q)
        ans = []
        for i in range(k - 1, len(nums)):
            heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heappop(q)
            ans.append(-q[0][0])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Monotonic Queue

To find the maximum value in a sliding window, a common method is to use a monotonic queue.

We can maintain a queue $q$ that is monotonically decreasing from the front to the back, storing the indices of the elements. As we traverse the array $\textit{nums}$, for the current element $\textit{nums}[i]$, we first check if the front element of the queue is out of the window. If it is, we remove the front element. Then, we compare the current element $\textit{nums}[i]$ with the elements at the back of the queue. If the elements at the back are less than or equal to the current element, we remove them until the element at the back is greater than the current element or the queue is empty. Then, we add the index of the current element to the queue. At this point, the front element of the queue is the maximum value of the current sliding window. Note that we add the front element of the queue to the result array when the index $i$ is greater than or equal to $k-1$.

The time complexity is $O(n)$, and the space complexity is $O(k)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, x in enumerate(nums):
            if q and i - q[0] >= k:
                q.popleft()
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
