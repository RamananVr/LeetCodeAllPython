---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3709.Design%20Exam%20Scores%20Tracker/README_EN.md
rating: 1647
source: Biweekly Contest 167 Q3
tags:
    - Design
    - Array
    - Binary Search
    - Prefix Sum
---

<!-- problem:start -->

# [3709. Design Exam Scores Tracker](https://leetcode.com/problems/design-exam-scores-tracker)

## Description

<!-- description:start -->

<p>Alice frequently takes exams and wants to track her scores and calculate the total scores over specific time periods.</p>

<p>Implement the <code>ExamTracker</code> class:</p>

<ul>
	<li><code>ExamTracker()</code>: Initializes the <code>ExamTracker</code> object.</li>
	<li><code>void record(int time, int score)</code>: Alice takes a new exam at time <code>time</code> and achieves the score <code>score</code>.</li>
	<li><code>long long totalScore(int startTime, int endTime)</code>: Returns an integer that represents the <strong>total</strong> score of all exams taken by Alice between <code>startTime</code> and <code>endTime</code> (inclusive). If there are no recorded exams taken by Alice within the specified time interval, return 0.</li>
</ul>

<p>It is guaranteed that the function calls are made in chronological order. That is,</p>

<ul>
	<li>Calls to <code>record()</code> will be made with <strong>strictly increasing</strong> <code>time</code>.</li>
	<li>Alice will never ask for total scores that require information from the future. That is, if the latest <code>record()</code> is called with <code>time = t</code>, then <code>totalScore()</code> will always be called with <code>startTime &lt;= endTime &lt;= t</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong><br />
<span class="example-io">[&quot;ExamTracker&quot;, &quot;record&quot;, &quot;totalScore&quot;, &quot;record&quot;, &quot;totalScore&quot;, &quot;totalScore&quot;, &quot;totalScore&quot;, &quot;totalScore&quot;]<br />
[[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]</span></p>

<p><strong>Output:</strong><br />
<span class="example-io">[null, null, 98, null, 98, 197, 0, 99] </span></p>

<p><strong>Explanation</strong></p>
ExamTracker examTracker = new ExamTracker();<br />
examTracker.record(1, 98); // Alice takes a new exam at time 1, scoring 98.<br />
examTracker.totalScore(1, 1); // Between time 1 and time 1, Alice took 1 exam at time 1, scoring 98. The total score is 98.<br />
examTracker.record(5, 99); // Alice takes a new exam at time 5, scoring 99.<br />
examTracker.totalScore(1, 3); // Between time 1 and time 3, Alice took 1 exam at time 1, scoring 98. The total score is 98.<br />
examTracker.totalScore(1, 5); // Between time 1 and time 5, Alice took 2 exams at time 1 and 5, scoring 98 and 99. The total score is <code>98 + 99 = 197</code>.<br />
examTracker.totalScore(3, 4); // Alice did not take any exam between time 3 and time 4. Therefore, the answer is 0.<br />
examTracker.totalScore(2, 5); // Between time 2 and time 5, Alice took 1 exam at time 5, scoring 99. The total score is 99.</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= time &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= score &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= startTime &lt;= endTime &lt;= t</code>, where <code>t</code> is the value of <code>time</code> from the most recent call of <code>record()</code>.</li>
	<li>Calls of <code>record()</code> will be made with <strong>strictly increasing</strong> <code>time</code>.</li>
	<li>After <code>ExamTracker()</code>, the first function call will always be <code>record()</code>.</li>
	<li>At most <code>10<sup>5</sup></code> calls will be made in total to <code>record()</code> and <code>totalScore()</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum + Binary Search

We use an array $\textit{times}$ to store the time points of each exam, and another array $\textit{pre}$ to store the prefix sums, where $\textit{pre}[i]$ represents the total score of the first $i$ exams. For each call to $\texttt{record}(time, score)$, we add $time$ to $\textit{times}$ and add the last element of $\textit{pre}$ plus $score$ to $\textit{pre}$.

For each call to $\texttt{totalScore}(startTime, endTime)$, we use binary search to find the first position $l$ in $\textit{times}$ that is greater than or equal to $startTime$ and the first position $r$ that is greater than $endTime$, then return $\textit{pre}[r-1] - \textit{pre}[l-1]$.

The time complexity is $O(\log n)$, where $n$ is the number of exams. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class ExamTracker:

    def __init__(self):
        self.times = [0]
        self.pre = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.pre.append(self.pre[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.times, startTime) - 1
        r = bisect_left(self.times, endTime + 1) - 1
        return self.pre[r] - self.pre[l]

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
