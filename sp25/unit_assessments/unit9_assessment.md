---
title: CSCI 13300 SP 2025
author: "[Go to homepage](https://benrosenberg.info/teaching/sp25/csci13300.html)"
date: "Last updated: 2025-03-22"
css: ../../style.css
---

# Unit 9 Assessment

## Due date and submission

This assignment is due **April 5th** at 11:59 PM. Submit your solution on Brightspace, under the "Unit 9" assignment.

**Please copy your code into the text box, making sure to indent it properly with whitespace so that it appears the same as in IDLE or wherever you wrote the code. This will make it easier for me to grade.**

You can submit multiple times. I will only grade your last submission.

## Task

In this task, you will write a function `draw_ngon_triangles(n)` that works like this:

![`draw_ngon_triangles(10)`](draw_ngon_triangles_10.png)

![`draw_ngon_triangles(5)`](draw_ngon_triangles_5.png)

![`draw_ngon_triangles(25)`](draw_ngon_triangles_25.png)

As you can see above, the function draws a regular `n`-gon (a regular polygon with `n` sides), and fills the constituent triangles (formed with a side on the perimeter, and the center point) with colors that go from white to black.

In the below diagram, angle $\angle A$ is what is described below as the "center" angle, and angle $\angle B$ is what is described as the "outer" angle.

![Annotated version of `draw_ngon_triangles(5)`](annotated_draw_ngon_triangles_5.png)

- The center angle of each triangle will be `360/n`, because there are `n` triangles and 360 total degrees around the center.
- The outer angles of the triangle will be `(180 - center_angle)/2`, because the sum of angles in a triangle is 180 degrees, and the outer angles split the difference between the total angle sum and the center angle.
- Use `100` as the length of the lines going from the center to each outer vertex of the polygon.
- Use the function `calculate_side_length(n)` to get the side length for a given `n`:
  ```python
  import math

  def calculate_side_length(n):
      return 200 * math.sin(math.radians(360/n)/2)
  ```

Some turtle functions that you should use (you shouldn't need anything besides these):

- `colormode`
- `fillcolor`
- `begin_fill`
- `end_fill`
- `forward`
- `left`

# Notes

- It may be helpful to call `speed(0)` or `tracer(False)` towards the start of your code to make the turtle draw faster, as discussed in class.
- You should use `from turtle import *` as we did in class, not `import turtle` or `import turtle as t`.

You should be able to do all of the tasks with only the Python topics we covered in class so far.

If you want to use more complex functionality than what we discussed in class, the Python documentation may be helpful: [Python 3.10 documentation](https://docs.python.org/3.10/)

Additionally, the Python turtle documentation may be helpful: [Python 3.10 turtle documentation](https://docs.python.org/3.10/library/turtle.html)