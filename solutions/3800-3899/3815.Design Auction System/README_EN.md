---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3815.Design%20Auction%20System/README_EN.md
rating: 1853
source: Weekly Contest 485 Q3
---

<!-- problem:start -->

# [3815. Design Auction System](https://leetcode.com/problems/design-auction-system)

## Description

<!-- description:start -->

<p>You are asked to design an auction system that manages bids from multiple users in real time.</p>

<p>Each bid is associated with a <code>userId</code>, an <code>itemId</code>, and a <code>bidAmount</code>.</p>

<p>Implement the <code>AuctionSystem</code> class:​​​​​​​</p>

<ul>
	<li><code>AuctionSystem()</code>: Initializes the <code>AuctionSystem</code> object.</li>
	<li><code>void addBid(int userId, int itemId, int bidAmount)</code>: Adds a new bid for <code>itemId</code> by <code>userId</code> with <code>bidAmount</code>. If the same <code>userId</code> <strong>already</strong> has a bid on <code>itemId</code>, <strong>replace</strong> it with the new <code>bidAmount</code>.</li>
	<li><code>void updateBid(int userId, int itemId, int newAmount)</code>: Updates the existing bid of <code>userId</code> for <code>itemId</code> to <code>newAmount</code>. It is <strong>guaranteed</strong> that this bid <em>exists</em>.</li>
	<li><code>void removeBid(int userId, int itemId)</code>: Removes the bid of <code>userId</code> for <code>itemId</code>. It is <strong>guaranteed</strong> that this bid <em>exists</em>.</li>
	<li><code>int getHighestBidder(int itemId)</code>: Returns the <code>userId</code> of the <strong>highest</strong> bidder for <code>itemId</code>. If multiple users have the <strong>same highest</strong> <code>bidAmount</code>, return the user with the <strong>highest</strong> <code>userId</code>. If no bids exist for the item, return -1.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong><br />
<span class="example-io">[&quot;AuctionSystem&quot;, &quot;addBid&quot;, &quot;addBid&quot;, &quot;getHighestBidder&quot;, &quot;updateBid&quot;, &quot;getHighestBidder&quot;, &quot;removeBid&quot;, &quot;getHighestBidder&quot;, &quot;getHighestBidder&quot;]<br />
[[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]]</span></p>

<p><strong>Output:</strong><br />
<span class="example-io">[null, null, null, 2, null, 1, null, 1, -1] </span></p>

<p><strong>Explanation</strong></p>
AuctionSystem auctionSystem = new AuctionSystem(); // Initialize the Auction system<br />
auctionSystem.addBid(1, 7, 5); // User 1 bids 5 on item 7<br />
auctionSystem.addBid(2, 7, 6); // User 2 bids 6 on item 7<br />
auctionSystem.getHighestBidder(7); // return 2 as User 2 has the highest bid<br />
auctionSystem.updateBid(1, 7, 8); // User 1 updates bid to 8 on item 7<br />
auctionSystem.getHighestBidder(7); // return 1 as User 1 now has the highest bid<br />
auctionSystem.removeBid(2, 7); // Remove User 2&#39;s bid on item 7<br />
auctionSystem.getHighestBidder(7); // return 1 as User 1 is the current highest bidder<br />
auctionSystem.getHighestBidder(3); // return -1 as no bids exist for item 3</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId, itemId &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= bidAmount, newAmount &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>5 * 10<sup>4</sup></code> total calls to <code>addBid</code>, <code>updateBid</code>, <code>removeBid</code>, and <code>getHighestBidder</code>.</li>
	<li>The input is generated such that for <code>updateBid</code> and <code>removeBid</code>, the bid from the given <code>userId</code> for the given <code>itemId</code> will be valid.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Ordered Set

We define two hash tables. `items` is used to store all bid information for each item, where `items[itemId]` stores an ordered set. Each element in the set is a tuple `(bidAmount, userId)`, representing a user's bid amount for that item. Since we need to quickly retrieve the user with the highest bid, this ordered set needs to be sorted by bid amount in ascending order. If bid amounts are identical, they are sorted by user ID in ascending order. The other hash table `users` is used to store the bid information of each user for each item, where `users[userId][itemId]` stores the user's bid amount for that item.

For the `addBid(userId, itemId, bidAmount)` operation, we first check if the user has already placed a bid on the item. If they have, we call the `removeBid(userId, itemId)` method to remove the original bid; then we add the new bid information to `users` and `items`.

For the `updateBid(userId, itemId, newAmount)` operation, we first retrieve the user's original bid amount for the item from `users`, then remove the corresponding tuple `(oldAmount, userId)` from `items`, add the new bid information to `items`, and update the bid amount in `users`.

For the `removeBid(userId, itemId)` operation, we first retrieve the user's original bid amount for the item from `users`, then remove the corresponding tuple `(oldAmount, userId)` from `items`, and finally delete the user's bid information for that item from `users`.

For the `getHighestBidder(itemId)` operation, we first check if `items[itemId]` is empty. If it is, we return -1; otherwise, we return the user ID of the last element in the ordered set, which corresponds to the highest bidder.

In terms of time complexity, each operation takes $O(\log m)$ time, where $m$ is the number of bids for the current item. The space complexity is $O(n)$, where $n$ is the total number of bids.

<!-- tabs:start -->

#### Python3

```python
class AuctionSystem:

    def __init__(self):
        self.items = defaultdict(SortedList)
        self.users = {}

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if userId not in self.users:
            self.users[userId] = {}
        if itemId in self.users[userId]:
            self.removeBid(userId, itemId)
        self.users[userId][itemId] = bidAmount
        self.items[itemId].add((bidAmount, userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        oldAmount = self.users[userId][itemId]
        self.items[itemId].remove((oldAmount, userId))
        self.items[itemId].add((newAmount, userId))
        self.users[userId][itemId] = newAmount

    def removeBid(self, userId: int, itemId: int) -> None:
        oldAmount = self.users[userId][itemId]
        self.items[itemId].remove((oldAmount, userId))
        self.users[userId].pop(itemId)

    def getHighestBidder(self, itemId: int) -> int:
        ls = self.items[itemId]
        return -1 if not ls else ls[-1][1]

# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
