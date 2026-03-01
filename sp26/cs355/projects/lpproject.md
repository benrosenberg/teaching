---
title: CSCI 35500 SP 2026
author: "[Go to homepage](https://benrosenberg.info/teaching/sp26/cs355/index.html)"
date: "Last updated: 2026-03-01"
css: "../../../style.css"
toc: true
---

# CS 355 LP Project: Airport MCF

![A beautiful plane flying through the sky](images/beautiful_plane.png)

This is the first project we will have in CS 355, on linear programming and OR-Tools. Due dates and other information will be available on the course website. Please ask any questions you have about this project in class.

## Problem statement

You are in charge of moving products from one set of US cities to another set of US cities. (All of these cities will have their own airports.) However, you are only allowed to use preexisting shipping routes.

You are given a list of trips that can be taken between US airports. Each trip will have a capacity (in pounds) that the route can transfer, based on the largest amount that was transferred in a one month period, over the 9 months from January 2025 to September 2025. There is also a distance associated with each trip, given in miles. Lastly, you will be given the amounts of inventory that you have in each starting city, along with the amount of inventory that you need to send to each destination. (These amounts will tie out.)

Your job is to determine how to move the inventory to the destinations as efficiently as possible.

Here is some sample data (most important columns, first 5 rows):

| source | target | capacity  | dist   | src_lat | src_lon  | dst_lat | dst_lon  | src_city     | dst_city      |
|--------|--------|-----------|--------|---------|----------|---------|----------|--------------|---------------|
| AAF    | OCF    | 3450.0    | 173.0  | 29.7275 | -85.0274 | 29.1725 | -82.2241 | Apalachicola | Ocala         |
| AAF    | SUA    | 3450.0    | 341.0  | 29.7275 | -85.0274 | 27.1816 | -80.2210 | Apalachicola | Stuart        |
| ABE    | ACK    | 3450.0    | 285.0  | 40.6517 | -75.4427 | 41.2531 | -70.0602 | Allentown    | Nantucket     |
| ABE    | ACY    | 46051.0   | 94.0   | 40.6517 | -75.4427 | 39.4575 | -74.5772 | Allentown    | Atlantic City |
| ABE    | AFW    | 3813000.0 | 1318.0 | 40.6517 | -75.4427 | 32.9904 | -97.3194 | Allentown    | Fort Worth    |

Latitude and longitude for both source and target cities are included if you want to plot your route.

## Instructions

### Task

You must:

1. Model the minimum cost flow problem as a linear program.
   - Use one or more Markdown cells in the Jupyter notebook you submit to describe this model in mathematical notation as we have done in class.
2. Use Python to implement your MCF model and solve it based on the inputs you were given and the route data provided.

Some specifics on the task:

- "As efficiently as possible" means minimizing the total distance that each pound of inventory travels (i.e., $\sum (\text{flow}\times\text{distance})$)
- You must respect the capacity limits of each route. However, it's very likely that you won't get anywhere near the capacity limits for some routes, as they are very high, and you are only shipping 100 pounds of inventory total (see below).

### Inputs

You will be given a list of 5 source airports and 10 destination airports. These sets will not have any overlap, so you don't need to worry about that edge case. Along with these source and destination airports, you will be given numbers for supply and demand for each of the source and destination airports respectively, which should each add to 100 for demand (or -100 for supply).

This data will come as a CSV file with columns like this (this is just an example, your data will be different):

| type   | airport | flow |
|:-------|:--------|-----:|
| source | RDU     |    8 |
| source | BLD     |   38 |
| ...    | ...     |  ... |
| sink   | FOD     |  -10 |
| sink   | CEZ     |  -22 |

Notes on your input data:

- You will all get different problem instances (different source nodes/inventory amounts/sink nodes)
- Your problem instances should all be feasible, so if you get that they are infeasible you probably have an issue with your constraints
- You may want to use pandas to read and process the CSV

You will also be given the full dataset as described above, with information on available routes, and the capacity and distance of each route. The only columns you really need to use are `source`, `target`, `capacity`, and `dist`.

### Submission

Submit a Jupyter notebook to Brightspace that has the following in it:

- In a Markdown cell (or multiple Markdown cells): your LP formulation for the MCF problem
- A brief description of how you chose to map the problem to the MCF model
- An OR-Tools implementation of the model, using the input data
- Clear indication of the objective value that you obtained for your problem

## Requirements

For each of the following requirements that you do not follow, you will lose 5 points:

- You must model this as a min cost flow problem
- You must use OR-Tools with linear programming (not integer programming or any other solving method)
- You must submit a Jupyter notebook (.ipynb format)
- You must give the constraints as part of your submission, in the Markdown cells of the notebook
- I should not need to run your file on my end, it should have all the outputs "pre-run" and included in your file
- You must use Python in the Jupyter notebook, not R or Julia or any other language

## Submission/grading

Submit your Jupyter notebook file to Brightspace.

Grading:

- 20% MCF formulation
  - You must describe the MCF problem and how it can be modeled as a linear program, using the same formal notation as we did in class for similar linear program models.
- 20% description of how you mapped this problem to the MCF
  - Describe your decision variables, constraints, and objective for this problem.
- 40% OR-Tools implementation
  - You must have successfully run the code using OR-Tools to get these points, and obtained some solution to the problem that makes sense.
- 10% correct solution
  - I have a solver, the output of which I will compare to your solution.
  - If your objective value is within 5% of the objective value I calculated (e.g., my solver calculated 100 and your solution was in the range [95, 105]), you get these points.

## AI tools/external resources reminder

Use whatever resources you feel comfortable with.

There are no restrictions.

