---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3822.Design%20Order%20Management%20System/README_EN.md
tags:
    - Design
    - Hash Table
---

<!-- problem:start -->

# [3822. Design Order Management System 🔒](https://leetcode.com/problems/design-order-management-system)

## Description

<!-- description:start -->

<p>You are asked to design a simple order management system for a trading platform.</p>

<p>Each order is associated with an <code>orderId</code>, an <code>orderType</code> (<code>&quot;buy&quot;</code> or <code>&quot;sell&quot;</code>), and a <code>price</code>.</p>

<p>An order is considered <strong>active</strong> unless it is canceled.</p>

<p>Implement the <code>OrderManagementSystem</code> class:</p>

<ul>
	<li><code>OrderManagementSystem()</code>: Initializes the order management system.</li>
	<li><code>void addOrder(int orderId, string orderType, int price)</code>: Adds a new <strong>active</strong> order with the given attributes. It is <strong>guaranteed</strong> that <code>orderId</code> is unique.</li>
	<li><code>void modifyOrder(int orderId, int newPrice)</code>: Modifies the <strong>price</strong> of an existing order. It is <strong>guaranteed</strong> that the order exists and is <em>active</em>.</li>
	<li><code>void cancelOrder(int orderId)</code>: Cancels an existing order. It is <strong>guaranteed</strong> that the order exists and is <em>active</em>.</li>
	<li><code>vector&lt;int&gt; getOrdersAtPrice(string orderType, int price)</code>: Returns the <code>orderId</code>s of all <strong>active</strong> orders that match the given <code>orderType</code> and <code>price</code>. If no such orders exist, return an empty list.</li>
</ul>

<p><strong>Note:</strong> The order of returned <code>orderId</code>s does not matter.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong><br />
<span class="example-io">[&quot;OrderManagementSystem&quot;, &quot;addOrder&quot;, &quot;addOrder&quot;, &quot;addOrder&quot;, &quot;getOrdersAtPrice&quot;, &quot;modifyOrder&quot;, &quot;modifyOrder&quot;, &quot;getOrdersAtPrice&quot;, &quot;cancelOrder&quot;, &quot;cancelOrder&quot;, &quot;getOrdersAtPrice&quot;]<br />
[[], [1, &quot;buy&quot;, 1], [2, &quot;buy&quot;, 1], [3, &quot;sell&quot;, 2], [&quot;buy&quot;, 1], [1, 3], [2, 1], [&quot;buy&quot;, 1], [3], [2], [&quot;buy&quot;, 1]]</span></p>

<p><strong>Output:</strong><br />
<span class="example-io">[null, null, null, null, [2, 1], null, null, [2], null, null, []] </span></p>

<p><strong>Explanation</strong></p>
OrderManagementSystem orderManagementSystem = new OrderManagementSystem();<br />
orderManagementSystem.addOrder(1, &quot;buy&quot;, 1); // A buy order with ID 1 is added at price 1.<br />
orderManagementSystem.addOrder(2, &quot;buy&quot;, 1); // A buy order with ID 2 is added at price 1.<br />
orderManagementSystem.addOrder(3, &quot;sell&quot;, 2); // A sell order with ID 3 is added at price 2.<br />
orderManagementSystem.getOrdersAtPrice(&quot;buy&quot;, 1); // Both buy orders (IDs 1 and 2) are active at price 1, so the result is <code>[2, 1]</code>.<br />
orderManagementSystem.modifyOrder(1, 3); // Order 1 is updated: its price becomes 3.<br />
orderManagementSystem.modifyOrder(2, 1); // Order 2 is updated, but its price remains 1.<br />
orderManagementSystem.getOrdersAtPrice(&quot;buy&quot;, 1); // Only order 2 is still an active buy order at price 1, so the result is <code>[2]</code>.<br />
orderManagementSystem.cancelOrder(3); // The sell order with ID 3 is canceled and removed from active orders.<br />
orderManagementSystem.cancelOrder(2); // The buy order with ID 2 is canceled and removed from active orders.<br />
orderManagementSystem.getOrdersAtPrice(&quot;buy&quot;, 1); // There are no active buy orders left at price 1, so the result is <code>[]</code>.</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= orderId &lt;= 2000</code></li>
	<li><code>orderId</code> is <strong>unique</strong> across all orders.</li>
	<li><code>orderType</code> is either <code>&quot;buy&quot;</code> or <code>&quot;sell&quot;</code>.</li>
	<li><code>1 &lt;= price &lt;= 10<sup>9</sup></code></li>
	<li>The total number of calls to <code>addOrder</code>, <code>modifyOrder</code>, <code>cancelOrder</code>, and <code>getOrdersAtPrice</code> does not exceed <font face="monospace">2000</font>.</li>
	<li>For <code>modifyOrder</code> and <code>cancelOrder</code>, the specified <code>orderId</code> is <strong>guaranteed</strong> to exist and be <em>active</em>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We use a hash table $\textit{orders}$ to store the type and price information of each order, where the key is the order ID and the value is a tuple $(\textit{orderType}, \textit{price})$. Additionally, we use another hash table $\textit{t}$ to store the list of order IDs corresponding to each $(\textit{orderType}, \textit{price})$, where the key is a tuple $(\textit{orderType}, \textit{price})$ and the value is the list of order IDs.

When calling $\texttt{addOrder}$, we add the order information to $\textit{orders}$ and append the order ID to the corresponding list in $\textit{t}$.

When calling $\texttt{modifyOrder}$, we first retrieve the order type and old price from $\textit{orders}$, then update the order's price information. Next, we remove the order ID from the corresponding list in $\textit{t}$ and add it to the list corresponding to the new price.

When calling $\texttt{cancelOrder}$, we retrieve the order type and price information from $\textit{orders}$, then remove the order ID from the corresponding list in $\textit{t}$ and delete the order from $\textit{orders}$.

When calling $\texttt{getOrdersAtPrice}$, we directly return the list of order IDs corresponding to the query in $\textit{t}$.

In the above operations, the time complexity for adding and retrieving the order ID list is $O(1)$, while the time complexity for removing an order ID from the list is $O(n)$, where $n$ is the length of the corresponding list. Since the total number of orders in the problem does not exceed $2000$, this method is efficient enough in practice. The space complexity is $O(m)$, where $m$ is the total number of orders.

<!-- tabs:start -->

#### Python3

```python
class OrderManagementSystem:

    def __init__(self):
        self.orders = {}
        self.t = defaultdict(list)

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.orders[orderId] = (orderType, price)
        self.t[(orderType, price)].append(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        orderType, price = self.orders[orderId]
        self.orders[orderId] = (orderType, newPrice)
        self.t[(orderType, price)].remove(orderId)
        self.t[(orderType, newPrice)].append(orderId)

    def cancelOrder(self, orderId: int) -> None:
        orderType, price = self.orders[orderId]
        del self.orders[orderId]
        self.t[(orderType, price)].remove(orderId)

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return self.t[(orderType, price)]

# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
