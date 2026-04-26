---
title: CSCI 35500 SP 2026
author: "[Go to homepage](https://benrosenberg.info/teaching/sp26/cs355/index.html)"
date: "Last updated: 2026-04-26"
css: "../../../style.css"
toc: true
---

# CS 355 ILP Project: Sudoku

This is the second (and last) project we will have in CS 355, on integer linear programming and OR-Tools. Due dates and other information will be available on the course website. Please ask any questions you have about this project in class.

## Problem statement

In this project you will solve a Sudoku puzzle using integer linear programming. You will be given a specific puzzle to solve, and you will need to define an ILP formulation to model Sudoku and pass your problem in to verify that it works.

If you are unfamiliar with Sudoku, you can read about the puzzle on Wikipedia: [Wikipedia page for Sudoku](https://en.wikipedia.org/wiki/Sudoku)

The goal of Sudoku is to fill in every empty box with numbers, so that for every row, column, and (outlined) 3x3 box, each number from 1 to 9 is used exactly once.

For an example, try out the Sudoku generator and solver linked under the section on Inputs below.

## Instructions

### Task

You must:

1. Model the general Sudoku problem as a linear program.
   - Use one or more Markdown cells in the Jupyter notebook you submit to describe this model in mathematical notation as we have done in class.
   - **DO NOT ONLY MODEL YOUR INPUT.** If I generate another Sudoku problem, I should be able to pass it into your model without any changes to your formulation. Make your model sufficiently generic that this is possible, if you hardcode your input problem you will receive no credit for the formulation component.
     - A good benchmark for whether you have hardcoded your input or not is the ability to make a Python function that I can pass the list format of any given Sudoku puzzle to and receive an output without making any changes to your model code. Something like `solve_sudoku(puzzle)` should work.
2. Use Python to implement your model and solve the Sudoku puzzle you were given as an input.

### Inputs

You can get your input data here: [Sudoku generator](utils/sudoku.html)

To get your input, type your EMPLID into the Seed field and hit "Generate New". Make sure you double check that you have typed your EMPLID correctly, as I will be grading based on whether your solution matches the expected result - a typo in your EMPLID could result in a completely different Sudoku puzzle.

This will generate a new Sudoku puzzle for you to use. You will probably want to pass the Python list format to your solver because it's easier to work with.

You can (and should) check your puzzle solution by comparing it to the output given by the "Solve an ASCII puzzle" utility.

### Submission

Submit a Jupyter notebook to Brightspace that has the following in it:

- In a Markdown cell (or multiple Markdown cells): your ILP formulation for the Sudoku problem
- A brief description of how your formulation models each of the Sudoku constraints
- An OR-Tools implementation of the model, run against your input data
- Clear indication of the solution that you obtained for your puzzle, so that I can compare it against the expected result

## Requirements

For each of the following requirements that you do not follow, you will lose 5 points:

- You must model this as an ILP
- You must use OR-Tools with integer linear programming (not linear programming or any other solving method)
- You must submit a Jupyter notebook (.ipynb format)
- You must give the constraints as part of your submission, in the Markdown cells of the notebook
- I should not need to run your file on my end, it should have all the outputs "pre-run" and included in your file
- You must use Python in the Jupyter notebook, not R or Julia or any other language

## Submission/grading

Submit your Jupyter notebook file to Brightspace.

Grading:

- 50% Sudoku formulation/description of your problem model
  - You must describe the Sudoku problem and how it can be modeled as an integer linear program, using the same formal notation as we did in class for similar integer linear program models.
  - Describe your decision variables, constraints, and objective for this problem.
- 40% OR-Tools implementation
  - You must have successfully run the code using OR-Tools to get these points, and obtained some solution to the problem that makes sense.
- 10% correct solution
  - I will compare your solution to the one given by the "Solve an ASCII puzzle" utility.
  - If your solution is exactly the same, you get these points. (You can and should check to make sure this is the case, using the same utility.)

## AI tools/external resources reminder

Use whatever resources you feel comfortable with.

There are no restrictions.

