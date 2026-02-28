"""
Budget Mate, is a program that allows me to budget my monthly income.
Because my monthly income fluctuates, Budget Mate is designed to calculate my
personal income based on a variation of the 50/30/20 rule (Debt/Needs/Wants).
"""
# Imports the BudgetCalculator class from the helper.py file.
from projects.budget_mate.core.budget_allocator import BudgetAllocator

def main():
    budget = BudgetAllocator()
    budget.run_budget_mate()

if __name__ == "__main__":
    main()  # Ensures main() only runs if program is executed directly.

