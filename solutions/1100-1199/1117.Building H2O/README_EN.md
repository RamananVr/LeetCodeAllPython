---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1117.Building%20H2O/README_EN.md
tags:
    - 多线程
---

<!-- problem:start -->

# [1117. Building H2O](https://leetcode.com/problems/building-h2o)

## Description

<!-- description:start -->

<p>There are two kinds of threads: <code>oxygen</code> and <code>hydrogen</code>. Your goal is to group these threads to form water molecules.</p>

<p>There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given <code>releaseHydrogen</code> and <code>releaseOxygen</code> methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.</p>

<p>In other words:</p>

<ul>
	<li>If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads.</li>
	<li>If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.</li>
</ul>

<p>We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up with. The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.</p>

<p>Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> water = &quot;HOH&quot;
<strong>Output:</strong> &quot;HHO&quot;
<strong>Explanation:</strong> &quot;HOH&quot; and &quot;OHH&quot; are also valid answers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> water = &quot;OOHHHH&quot;
<strong>Output:</strong> &quot;HHOHHO&quot;
<strong>Explanation:</strong> &quot;HOHHHO&quot;, &quot;OHHHHO&quot;, &quot;HHOHOH&quot;, &quot;HOHHOH&quot;, &quot;OHHHOH&quot;, &quot;HHOOHH&quot;, &quot;HOHOHH&quot; and &quot;OHHOHH&quot; are also valid answers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 * n == water.length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>water[i]</code> is either <code>&#39;H&#39;</code> or <code>&#39;O&#39;</code>.</li>
	<li>There will be exactly <code>2 * n</code> <code>&#39;H&#39;</code> in <code>water</code>.</li>
	<li>There will be exactly <code>n</code> <code>&#39;O&#39;</code> in <code>water</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
from threading import Semaphore

class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(0)

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        self.h.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.h._value == 0:
            self.o.release()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        self.o.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h.release(2)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
