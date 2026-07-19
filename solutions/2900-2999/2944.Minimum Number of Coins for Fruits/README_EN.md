---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2944.Minimum%20Number%20of%20Coins%20for%20Fruits/README_EN.md
rating: 1708
source: Biweekly Contest 118 Q3
tags:
    - Queue
    - Array
    - Dynamic Programming
    - Monotonic Queue
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2944. Minimum Number of Coins for Fruits](https://leetcode.com/problems/minimum-number-of-coins-for-fruits)

## Description

<!-- description:start -->

<p>You are given an <strong>0-indexed</strong> integer array <code>prices</code> where <code>prices[i]</code> denotes the number of coins needed to purchase the <code>(i + 1)<sup>th</sup></code> fruit.</p>

<p>The fruit market has the following reward for each fruit:</p>

<ul>
	<li>If you purchase the <code>(i + 1)<sup>th</sup></code> fruit at <code>prices[i]</code> coins, you can get any number of the next <code>i</code> fruits for free.</li>
</ul>

<p><strong>Note</strong> that even if you <strong>can</strong> take fruit <code>j</code> for free, you can still purchase it for <code>prices[j - 1]</code> coins to receive its reward.</p>

<p>Return the <strong>minimum</strong> number of coins needed to acquire all the fruits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [3,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Purchase the 1<sup>st</sup> fruit with <code>prices[0] = 3</code> coins, you are allowed to take the 2<sup>nd</sup> fruit for free.</li>
	<li>Purchase the 2<sup>nd</sup> fruit with <code>prices[1] = 1</code> coin, you are allowed to take the 3<sup>rd</sup> fruit for free.</li>
	<li>Take the 3<sup>rd</sup> fruit for free.</li>
</ul>

<p>Note that even though you could take the 2<sup>nd</sup> fruit for free as a reward of buying 1<sup>st</sup> fruit, you purchase it to receive its reward, which is more optimal.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [1,10,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Purchase the 1<sup>st</sup> fruit with <code>prices[0] = 1</code> coin, you are allowed to take the 2<sup>nd</sup> fruit for free.</li>
	<li>Take the 2<sup>nd</sup> fruit for free.</li>
	<li>Purchase the 3<sup>rd</sup> fruit for <code>prices[2] = 1</code> coin, you are allowed to take the 4<sup>th</sup> fruit for free.</li>
	<li>Take the 4<sup>t</sup><sup>h</sup> fruit for free.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [26,18,6,12,49,7,45,45]</span></p>

<p><strong>Output:</strong> <span class="example-io">39</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Purchase the 1<sup>st</sup> fruit with <code>prices[0] = 26</code> coin, you are allowed to take the 2<sup>nd</sup> fruit for free.</li>
	<li>Take the 2<sup>nd</sup> fruit for free.</li>
	<li>Purchase the 3<sup>rd</sup> fruit for <code>prices[2] = 6</code> coin, you are allowed to take the 4<sup>th</sup>, 5<sup>th</sup> and 6<sup>th</sup> (the next three) fruits for free.</li>
	<li>Take the 4<sup>t</sup><sup>h</sup> fruit for free.</li>
	<li>Take the 5<sup>t</sup><sup>h</sup> fruit for free.</li>
	<li>Purchase the 6<sup>th</sup> fruit with <code>prices[5] = 7</code> coin, you are allowed to take the 8<sup>th</sup> and 9<sup>th</sup> fruit for free.</li>
	<li>Take the 7<sup>t</sup><sup>h</sup> fruit for free.</li>
	<li>Take the 8<sup>t</sup><sup>h</sup> fruit for free.</li>
</ul>

<p>Note that even though you could take the 6<sup>th</sup> fruit for free as a reward of buying 3<sup>rd</sup> fruit, you purchase it to receive its reward, which is more optimal.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 1000</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We define a function $\textit{dfs}(i)$ to represent the minimum number of coins needed to buy all the fruits starting from the $i$-th fruit. The answer is $\textit{dfs}(1)$.

The execution logic of the function $\textit{dfs}(i)$ is as follows:

- If $i \times 2 \geq n$, it means that buying the $(i - 1)$-th fruit is sufficient, and the remaining fruits can be obtained for free, so return $\textit{prices}[i - 1]$.
- Otherwise, we can buy fruit $i$, and then choose a fruit $j$ to start buying from the next $i + 1$ to $2i + 1$ fruits. Thus, $\textit{dfs}(i) = \textit{prices}[i - 1] + \min_{i + 1 \le j \le 2i + 1} \textit{dfs}(j)$.

To avoid redundant calculations, we use memoization to store the results that have already been computed. When encountering the same situation again, we directly return the result.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{prices}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i * 2 >= len(prices):
                return prices[i - 1]
            return prices[i - 1] + min(dfs(j) for j in range(i + 1, i * 2 + 2))

        return dfs(1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We can rewrite the memoization search in Solution 1 into a dynamic programming form.

Similar to Solution 1, we define $f[i]$ to represent the minimum number of coins needed to buy all the fruits starting from the $i$-th fruit. The answer is $f[1]$.

The state transition equation is $f[i] = \min_{i + 1 \le j \le 2i + 1} f[j] + \textit{prices}[i - 1]$.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{prices}$.

In the code implementation, we can directly use the $\textit{prices}$ array to store the $f$ array, thus optimizing the space complexity to $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        for i in range((n - 1) // 2, 0, -1):
            prices[i - 1] += min(prices[i : i * 2 + 1])
        return prices[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming + Monotonic Queue Optimization

Observing the state transition equation in Solution 2, we can see that for each $i$, we need to find the minimum value of $f[i + 1], f[i + 2], \cdots, f[2i + 1]$. As $i$ decreases, the range of these values also decreases. This is essentially finding the minimum value in a sliding window with a narrowing range, which can be optimized using a monotonic queue.

We calculate from back to front, maintaining a monotonically increasing queue $q$, where the queue stores indices. If the front element of $q$ is greater than $i \times 2 + 1$, it means that the elements after $i$ will not be used, so we dequeue the front element. If $i$ is not greater than $(n - 1) / 2$, we can add $\textit{prices}[q[0] - 1]$ to $\textit{prices}[i - 1]$, and then add $i$ to the back of the queue. If the fruit price corresponding to the back element of $q$ is greater than or equal to $\textit{prices}[i - 1]$, we dequeue the back element until the fruit price corresponding to the back element is less than $\textit{prices}[i - 1]$ or the queue is empty, then add $i$ to the back of the queue.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{prices}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        q = deque()
        for i in range(n, 0, -1):
            while q and q[0] > i * 2 + 1:
                q.popleft()
            if i <= (n - 1) // 2:
                prices[i - 1] += prices[q[0] - 1]
            while q and prices[q[-1] - 1] >= prices[i - 1]:
                q.pop()
            q.append(i)
        return prices[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
