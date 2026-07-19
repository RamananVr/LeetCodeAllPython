---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1360.Number%20of%20Days%20Between%20Two%20Dates/README_EN.md
rating: 1421
source: Weekly Contest 177 Q1
tags:
    - Math
    - String
---

<!-- problem:start -->

# [1360. Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates)

## Description

<!-- description:start -->

<p>Write a program to count the number of days between two dates.</p>

<p>The two dates are given as strings, their format is <code>YYYY-MM-DD</code>&nbsp;as shown in the examples.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> date1 = "2019-06-29", date2 = "2019-06-30"
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> date1 = "2020-01-15", date2 = "2019-12-31"
<strong>Output:</strong> 15
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given dates are valid&nbsp;dates between the years <code>1971</code> and <code>2100</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Mathematics

First, we define a function `isLeapYear(year)` to determine whether the given year `year` is a leap year. If it is a leap year, return `true`, otherwise return `false`.

Next, we define another function `daysInMonth(year, month)` to calculate the total number of days in the given year `year` and month `month`. We can use an array `days` to store the number of days in each month, where `days[1]` represents the number of days in February. If it is a leap year, it is $29$ days, otherwise it is $28$ days.

Then, we define another function `calcDays(date)` to calculate the number of days from the given date `date` to `1971-01-01`. We can use `date.split("-")` to split the date `date` into year `year`, month `month`, and day `day` by `-`. Then we can use a loop to calculate the total number of days from `1971` to `year`, then calculate the total number of days from January to `month`, and finally add `day` days.

Finally, we only need to return the absolute value of `calcDays(date1) - calcDays(date2)`.

The time complexity is $O(y + m)$, where $y$ represents the number of years from the given date to `1971-01-01`, and $m$ represents the number of months of the given date. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def daysInMonth(year: int, month: int) -> int:
            days = [
                31,
                28 + int(isLeapYear(year)),
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31,
            ]
            return days[month - 1]

        def calcDays(date: str) -> int:
            year, month, day = map(int, date.split("-"))
            days = 0
            for y in range(1971, year):
                days += 365 + int(isLeapYear(y))
            for m in range(1, month):
                days += daysInMonth(year, m)
            days += day
            return days

        return abs(calcDays(date1) - calcDays(date2))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
