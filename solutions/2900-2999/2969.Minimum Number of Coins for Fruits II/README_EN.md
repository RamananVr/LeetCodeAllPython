---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2969.Minimum%20Number%20of%20Coins%20for%20Fruits%20II/README_EN.md
tags:
    - Queue
    - Array
    - Dynamic Programming
    - Monotonic Queue
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2969. Minimum Number of Coins for Fruits II 🔒](https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii)

## Description

<!-- description:start -->

<p>You are at a fruit market with different types of exotic fruits on display.</p>

<p>You are given a <strong>1-indexed</strong> array <code>prices</code>, where <code>prices[i]</code> denotes the number of coins needed to purchase the <code>i<sup>th</sup></code> fruit.</p>

<p>The fruit market has the following offer:</p>

<ul>
	<li>If you purchase the <code>i<sup>th</sup></code> fruit at <code>prices[i]</code> coins, you can get the next <code>i</code> fruits for free.</li>
</ul>

<p><strong>Note</strong> that even if you <strong>can</strong> take fruit <code>j</code> for free, you can still purchase it for <code>prices[j]</code> coins to receive a new offer.</p>

<p>Return <em>the <strong>minimum</strong> number of coins needed to acquire all the fruits</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [3,1,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can acquire the fruits as follows:
- Purchase the 1<sup>st</sup> fruit with 3 coins, and you are allowed to take the 2<sup>nd</sup> fruit for free.
- Purchase the 2<sup>nd</sup> fruit with 1 coin, and you are allowed to take the 3<sup>rd</sup> fruit for free.
- Take the 3<sup>rd</sup> fruit for free.
Note that even though you were allowed to take the 2<sup>nd</sup> fruit for free, you purchased it because it is more optimal.
It can be proven that 4 is the minimum number of coins needed to acquire all the fruits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,10,1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can acquire the fruits as follows:
- Purchase the 1<sup>st</sup> fruit with 1 coin, and you are allowed to take the 2<sup>nd</sup> fruit for free.
- Take the 2<sup>nd</sup> fruit for free.
- Purchase the 3<sup>rd</sup> fruit for 1 coin, and you are allowed to take the 4<sup>th</sup> fruit for free.
- Take the 4<sup>t</sup><sup>h</sup> fruit for free.
It can be proven that 2 is the minimum number of coins needed to acquire all the fruits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i]$ as the minimum number of coins needed to buy all fruits starting from the $i$th fruit. So the answer is $f[1]$.

The state transition equation is $f[i] = \min_{i + 1 \le j \le 2i + 1} f[j] + prices[i - 1]$.

In implementation, we calculate from back to front, and we can directly perform state transition on the array $prices$, which can save space.

The time complexity of the above method is $O(n^2)$. Since the scale of $n$ in this problem reaches $10^5$, it will time out.

We observe the state transition equation and find that for each $i$, we need to find the minimum value of $f[i + 1], f[i + 2], \cdots, f[2i + 1]$, and as $i$ decreases, the range of these values is also decreasing. This is actually finding the minimum value of a monotonically narrowing sliding window, and we can use a monotonic queue to optimize.

We calculate from back to front, maintain a monotonically increasing queue $q$, and the queue stores the index. If the head element of $q$ is greater than $i \times 2 + 1$, it means that the elements after $i$ will not be used, so we dequeue the head element. If $i$ is not greater than $(n - 1) / 2$, then we can add $prices[q[0] - 1]$ to $prices[i - 1]$, and then add $i$ to the tail of the queue. If the price of the fruit corresponding to the tail element of $q$ is greater than or equal to $prices[i - 1]$, then we dequeue the tail element until the price of the fruit corresponding to the tail element is less than $prices[i - 1]$ or the queue is empty, and then add $i$ to the tail of the queue.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array $prices$.

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
