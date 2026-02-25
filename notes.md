# Budget Mate: A Program Designed Around Money Management

## What is Budget Mate?
* Budget Mate, is a program that allows me to budget my monthly income.
Because my monthly income fluctuates, Budget Mate is designed to calculate my
personal income based on a variation of the 50/30/20 rule (Debt/Needs/Wants).

## Extended App Capabilities
* ~~Budget Mate will allow me to enter more than one source of income~~
* ~~Budget Mate will allow me to add more income to current income amount for the current month~~
* ~~Budget Mate provides output consisting of their newly added earnings, total earnings, and updated category 
    allocations~~
<<<<<<< HEAD
* Add a way for the user to be able to make changes to their earnings in case they enter the wrong income amount(s)
* Create a new method that greets the user
* Create a new method that displays a user-friendly menu when called
  * This will require method invocation (one method calls another method)
* Add a feature that allows a user to enter his/her name:
  * If their name exists, ask the user if they would like to continue adding to their saved monthly_budget.json file
  * If their name does NOT exist, ask if they would like to create a new account
  * Basically, allow user to login or signup depending on whether or not the user's name is recognized upon opening 
    .json file 
=======
* ~~Create a new method that greets the user~~
* ~~Create a new method that displays a user-friendly menu when called~~
  * ~~This will require method invocation (one method calls another method)~~
>>>>>>> ad58e41 (Extended budget_mate_calculator.py capabilities. Also updated notes.md)

## Refactoring Budget Mate
* ~~Cleanup the 'display_budget_summary' method when displaying updated earnings total amount & category allocations~~
* There are two bugs in the 'display_menu' method:
  * A ValueError occurs only if there is no data in the monthly_budget.json file
  * Another is a LogicalError that occurs when option 2 from the menu is selected - the 'display_method_summary' is
    called 2x