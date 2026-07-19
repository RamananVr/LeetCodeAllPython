---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0346.Moving%20Average%20from%20Data%20Stream/README_EN.md
tags:
    - Design
    - Queue
    - Array
    - Data Stream
---

<!-- problem:start -->

# [346. Moving Average from Data Stream 🔒](https://leetcode.com/problems/moving-average-from-data-stream)

## Description

<!-- description:start -->

<p>Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.</p>

<p>Implement the&nbsp;<code>MovingAverage</code> class:</p>

<ul>
	<li><code>MovingAverage(int size)</code> Initializes&nbsp;the object with the size of the window <code>size</code>.</li>
	<li><code>double next(int val)</code> Returns the moving average of the last <code>size</code> values of the stream.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MovingAverage&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;]
[[3], [1], [10], [3], [5]]
<strong>Output</strong>
[null, 1.0, 5.5, 4.66667, 6.0]

<strong>Explanation</strong>
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= size &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup> &lt;= val &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>next</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Circular Array

We define a variable $\textit{s}$ to calculate the sum of the last $\textit{size}$ elements, and a variable $\textit{cnt}$ to record the total number of current elements. Additionally, we use an array $\textit{data}$ of length $\textit{size}$ to record the value of each element at each position.

When calling the $\textit{next}$ function, we first calculate the index $i$ where $\textit{val}$ should be stored, then update the sum $s$, set the value at index $i$ to $\textit{val}$, and increment the element count by one. Finally, we return the value of $\frac{s}{\min(\textit{cnt}, \textit{size})}$.

The time complexity is $O(1)$, and the space complexity is $O(n)$, where $n$ is the integer $\textit{size}$ given in the problem.

<!-- tabs:start -->

#### Python3

```python
class MovingAverage:

    def __init__(self, size: int):
        self.s = 0
        self.data = [0] * size
        self.cnt = 0

    def next(self, val: int) -> float:
        i = self.cnt % len(self.data)
        self.s += val - self.data[i]
        self.data[i] = val
        self.cnt += 1
        return self.s / min(self.cnt, len(self.data))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Queue

We can use a queue $\textit{q}$ to store the last $\textit{size}$ elements, and a variable $\textit{s}$ to record the sum of these $\textit{size}$ elements.

When calling the $\textit{next}$ function, we first check if the length of the queue $\textit{q}$ is equal to $\textit{size}$. If it is, we dequeue the front element of the queue $\textit{q}$ and update the value of $\textit{s}$. Then we enqueue $\textit{val}$ and update the value of $\textit{s}$. Finally, we return the value of $\frac{s}{\text{len}(q)}$.

The time complexity is $O(1)$, and the space complexity is $O(n)$, where $n$ is the integer $\textit{size}$ given in the problem.

<!-- tabs:start -->

#### Python3

```python
class MovingAverage:
    def __init__(self, size: int):
        self.n = size
        self.s = 0
        self.q = deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.n:
            self.s -= self.q.popleft()
        self.q.append(val)
        self.s += val
        return self.s / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
