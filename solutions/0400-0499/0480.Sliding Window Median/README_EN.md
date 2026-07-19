---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0480.Sliding%20Window%20Median/README_EN.md
tags:
    - Array
    - Hash Table
    - Sliding Window
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median)

## Description

<!-- description:start -->

<p>The <strong>median</strong> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.</p>

<ul>
	<li>For examples, if <code>arr = [2,<u>3</u>,4]</code>, the median is <code>3</code>.</li>
	<li>For examples, if <code>arr = [1,<u>2,3</u>,4]</code>, the median is <code>(2 + 3) / 2 = 2.5</code>.</li>
</ul>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. There is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the median array for each window in the original array</em>. Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
<strong>Explanation:</strong> 
Window position                Median
---------------                -----
[<strong>1  3  -1</strong>] -3  5  3  6  7        1
 1 [<strong>3  -1  -3</strong>] 5  3  6  7       -1
 1  3 [<strong>-1  -3  5</strong>] 3  6  7       -1
 1  3  -1 [<strong>-3  5  3</strong>] 6  7        3
 1  3  -1  -3 [<strong>5  3  6</strong>] 7        5
 1  3  -1  -3  5 [<strong>3  6  7</strong>]       6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,2,3,1,4,2], k = 3
<strong>Output:</strong> [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dual Priority Queues (Min-Heap and Max-Heap) + Lazy Deletion

We can use two priority queues (min-heap and max-heap) to maintain the elements in the current window. One priority queue stores the smaller half of the elements, and the other priority queue stores the larger half of the elements. This way, the median of the current window is either the average of the top elements of the two heaps or one of the top elements.

We design a class $\textit{MedianFinder}$ to maintain the elements in the current window. This class includes the following methods:

- `add_num(num)`: Adds $\textit{num}$ to the current window.
- `find_median()`: Returns the median of the elements in the current window.
- `remove_num(num)`: Removes $\textit{num}$ from the current window.
- `prune(pq)`: If the top element of the heap is in the lazy deletion dictionary $\textit{delayed}$, it pops the top element from the heap and decrements its lazy deletion count. If the lazy deletion count of the element becomes zero, it removes the element from the lazy deletion dictionary.
- `rebalance()`: If the number of elements in the smaller half exceeds the number of elements in the larger half by $2$, it moves the top element of the larger half to the smaller half. If the number of elements in the smaller half is less than the number of elements in the larger half, it moves the top element of the larger half to the smaller half.

In the `add_num(num)` method, we first consider adding $\textit{num}$ to the smaller half. If $\textit{num}$ is greater than the top element of the larger half, we add $\textit{num}$ to the larger half. Then we call the `rebalance()` method to ensure that the size difference between the two priority queues does not exceed $1$.

In the `remove_num(num)` method, we increment the lazy deletion count of $\textit{num}$. Then we compare $\textit{num}$ with the top element of the smaller half. If $\textit{num}$ is less than or equal to the top element of the smaller half, we update the size of the smaller half and call the `prune()` method to ensure that the top element of the smaller half is not in the lazy deletion dictionary. Otherwise, we update the size of the larger half and call the `prune()` method to ensure that the top element of the larger half is not in the lazy deletion dictionary.

In the `find_median()` method, if the current window size is odd, we return the top element of the smaller half; otherwise, we return the average of the top elements of the smaller half and the larger half.

In the `prune(pq)` method, if the top element of the heap is in the lazy deletion dictionary, it pops the top element from the heap and decrements its lazy deletion count. If the lazy deletion count of the element becomes zero, it removes the element from the lazy deletion dictionary.

In the `rebalance()` method, if the number of elements in the smaller half exceeds the number of elements in the larger half by $2$, it moves the top element of the larger half to the smaller half. If the number of elements in the smaller half is less than the number of elements in the larger half, it moves the top element of the larger half to the smaller half.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class MedianFinder:
    def __init__(self, k: int):
        self.k = k
        self.small = []
        self.large = []
        self.delayed = defaultdict(int)
        self.small_size = 0
        self.large_size = 0

    def add_num(self, num: int):
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
            self.small_size += 1
        else:
            heappush(self.large, num)
            self.large_size += 1
        self.rebalance()

    def find_median(self) -> float:
        return -self.small[0] if self.k & 1 else (-self.small[0] + self.large[0]) / 2

    def remove_num(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.rebalance()

    def prune(self, pq: List[int]):
        sign = -1 if pq is self.small else 1
        while pq and sign * pq[0] in self.delayed:
            self.delayed[sign * pq[0]] -= 1
            if self.delayed[sign * pq[0]] == 0:
                self.delayed.pop(sign * pq[0])
            heappop(pq)

    def rebalance(self):
        if self.small_size > self.large_size + 1:
            heappush(self.large, -heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            heappush(self.small, -heappop(self.large))
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        finder = MedianFinder(k)
        for x in nums[:k]:
            finder.add_num(x)
        ans = [finder.find_median()]
        for i in range(k, len(nums)):
            finder.add_num(nums[i])
            finder.remove_num(nums[i - k])
            ans.append(finder.find_median())
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Ordered Set

We can use two ordered sets to maintain the elements in the current window. The ordered set $l$ stores the smaller half of the elements in the current window, and the ordered set $r$ stores the larger half of the elements.

We traverse the array $\textit{nums}$. For each element $x$, we add it to the ordered set $r$, then move the smallest element in the ordered set $r$ to the ordered set $l$. If the size of the ordered set $l$ is greater than the size of the ordered set $r$ by more than $1$, we move the largest element in the ordered set $l$ to the ordered set $r$.

If the total number of elements in the current window is $k$ and the size is odd, the maximum value in the ordered set $l$ is the median. If the size of the current window is even, the average of the maximum value in the ordered set $l$ and the minimum value in the ordered set $r$ is the median. Then, we remove the leftmost element of the window and continue traversing the array.

The time complexity is $O(n \log k)$, and the space complexity is $O(k)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = SortedList()
        r = SortedList()
        ans = []
        for i, x in enumerate(nums):
            r.add(x)
            l.add(r.pop(0))
            while len(l) - len(r) > 1:
                r.add(l.pop())
            j = i - k + 1
            if j >= 0:
                ans.append(l[-1] if k & 1 else (l[-1] + r[0]) / 2)
                if nums[j] in l:
                    l.remove(nums[j])
                else:
                    r.remove(nums[j])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
