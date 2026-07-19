---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1185.Day%20of%20the%20Week/README_EN.md
rating: 1382
source: Weekly Contest 153 Q2
tags:
    - Math
---

<!-- problem:start -->

# [1185. Day of the Week](https://leetcode.com/problems/day-of-the-week)

## Description

<!-- description:start -->

<p>Given a date, return the corresponding day of the week for that date.</p>

<p>The input is given as three integers representing the <code>day</code>, <code>month</code> and <code>year</code> respectively.</p>

<p>Return the answer as one of the following values&nbsp;<code>{&quot;Sunday&quot;, &quot;Monday&quot;, &quot;Tuesday&quot;, &quot;Wednesday&quot;, &quot;Thursday&quot;, &quot;Friday&quot;, &quot;Saturday&quot;}</code>.</p>

<p><strong>Note:</strong> January 1, 1971 was a Friday.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> day = 31, month = 8, year = 2019
<strong>Output:</strong> &quot;Saturday&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> day = 18, month = 7, year = 1999
<strong>Output:</strong> &quot;Sunday&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> day = 15, month = 8, year = 1993
<strong>Output:</strong> &quot;Sunday&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given dates are valid dates between the years <code>1971</code> and <code>2100</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Zeller's Congruence

We can use Zeller's Congruence to calculate the day of the week. Zeller's Congruence is as follows:

$$
w = (\left \lfloor \frac{c}{4} \right \rfloor - 2c + y + \left \lfloor \frac{y}{4} \right \rfloor + \left \lfloor \frac{13(m+1)}{5} \right \rfloor + d - 1) \bmod 7
$$

Where:

- `w`: Day of the week (starting from Sunday)
- `c`: First two digits of the year
- `y`: Last two digits of the year
- `m`: Month (the range of m is from 3 to 14, that is, in Zeller's Congruence, January and February of a certain year are considered as the 13th and 14th month of the previous year. For example, January 1, 2003 is considered as the 1st day of the 13th month of 2002)
- `d`: Day
- `⌊⌋`: Floor function (round down)
- `mod`: Modulo operation

The time complexity is $O(1)$, and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime('%A')
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        if m < 3:
            m += 12
            y -= 1
        c = y // 100
        y = y % 100
        w = (c // 4 - 2 * c + y + y // 4 + 13 * (m + 1) // 5 + d - 1) % 7
        return [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ][w]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
