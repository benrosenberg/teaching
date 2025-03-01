---
title: CSCI 13300 SP 2025
author: "[Go to homepage](https://benrosenberg.info/teaching/sp25/csci13300.html)"
date: "Last updated: 2025-02-28"
css: ../../style.css
---

# Unit 6 Assessment

## Due date and submission

This assignment is due **March 15th** at 11:59 PM. Submit your solution on BrightSpace, under the "Unit 6" assignment.

**Please copy your code into the text box, making sure to indent it properly with whitespace so that it appears the same as in IDLE or wherever you wrote the code. This will make it easier for me to grade.**

You can submit multiple times. I will only grade your last submission.

## Data

This assignment uses the CPI data we saw in class, from this link: [https://futureboy.us/frinkdata/cpiai.txt](https://futureboy.us/frinkdata/cpiai.txt)

You should download the data using the `urllib` method we saw in class, not manually.

# Instructions

## Task

In this task, we are going to write a program test6.py that reports Consumer Price Index and its average value for any year selected by the user. 

Additionally, the user will be able to choose the months of the year they want to display. The program will have to use list comprehension for transforming the list of months into the list of corresponding CPI values.

Below are some sample queries, which is how your program should appear when the final version is run. The results are given in `monospace`, the user input is given in **bold**, and some comments (not input by the user) are given in *italics*.

> Enter query: **1950**
> 
> `[23.5, 23.5, 23.6, 23.6, 23.7, 23.8, 24.1, 24.3, 24.4, 24.6, 24.7, 25.0] 24.066666666666666`
>
> 
> Enter query: **1950 5 6**        *(May and June of 1950)*
> 
> `[23.7, 23.8] 23.75`
>
> 
> Enter query: **1950 1 3 5 7**        *(January, March, May, and July of 1950)*
> 
> `[23.5, 23.6, 23.7, 24.1] 23.725`
>
> 
> Enter query:

### Step by step

1. Use urllib.request to download CPI data from [https://futureboy.us/frinkdata/cpiai.txt](https://futureboy.us/frinkdata/cpiai.txt).
2. Provide a user interface to look up the CPI values for any year. The program should read a year number from the keyboard and print out the list of CPI values for that year. After that, it should print out the average CPI for that year (by computing the average of the reported list).

```plaintext
Enter query: 1950
[23.5, 23.5, 23.6, 23.6, 23.7, 23.8, 24.1, 24.3, 24.4, 24.6, 24.7, 25.0] 24.066666666666666

Enter query: 2000
[168.8, 169.8, 171.2, 171.3, 171.5, 172.4, 172.8, 172.8, 173.7, 174.0, 174.1, 174.0] 172.19999999999996

Enter query:
```

3. Enhance the program by allowing the user to specify the list of months they want to see. A valid query may in addition to the year number contain a list of month numbers separated by spaces.
For example, `1950 1 3 5 7` requests the data for January, March, May, and July of 1950. If the months are not specified, report full year. The average should be computed only for the reported months.

```plaintext
Enter query: 1950
[23.5, 23.5, 23.6, 23.6, 23.7, 23.8, 24.1, 24.3, 24.4, 24.6, 24.7, 25.0] 24.066666666666666

Enter query: 1950 1 3 5 7
[23.5, 23.6, 23.7, 24.1] 23.725

Enter query: 1950 5 6
[23.7, 23.8] 23.75

Enter query:
```

4. Finally, edit your program to use **list comprehension** when transforming the list of month numbers into the list of corresponding CPI values.

# Notes

- Don’t worry what happens if the user enters invalid year or invalid month numbers.
- To find the list of months requested by the user, you will have to split the user input into a list of strings. If the length of the list is equal to 1, it contains only a year number and you have to report full year. Otherwise, the remaining elements of the list are the month numbers, use slicing to extract these numbers.

You should be able to do all of the tasks with only the Python topics we covered in class so far.

If you want to use more complex functionality than what we discussed in class, the Python documentation may be helpful: [Python 3.10 documentation](https://docs.python.org/3.10/)